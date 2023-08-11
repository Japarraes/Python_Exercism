from functools import reduce

OPERATORS = {'+': (lambda x, y: x + y),
            '-': (lambda x, y: x - y),
            '*': (lambda x, y: x * y),
            '/': (lambda x, y: x // y)}

def dup(stack):
    if not stack:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.append(stack[-1])
    return stack

def drop(stack):
    if not stack:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.pop()
    return stack

def swap(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.insert(len(stack)-2, stack.pop())
    return stack

def over(stack):
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    stack.append(stack[-2])
    return stack

STACK_MANIPULATION = {'DUP': dup,
                        'DROP': drop,
                        'SWAP': swap,
                        'OVER': over
                        }

class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
        message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

def evaluate(input_data):
    
    stack = []
    user_stack = {}

    for input in input_data:
        if input[0] == ":":     # User definition --> ": word-name definition ;"
            # Function: save in dictionary word-name: definition
            name, value = get_user_defined(input, user_stack)
            user_stack[name] = value
        else:
            # Function: save in List 
            stack = evaluate_stack(input, user_stack)
    
    return stack

def evaluate_stack(input, user_stack):
    
    nums = []
    result = 0
    first = True
    elements = input.split()

    for element in elements:
        if element.upper() in user_stack:
            
            for stack in user_stack[element.upper()]:
                if stack.isdigit():
                    nums.append(int(stack))
                
                elif stack in OPERATORS:
                    result = operation_stack(stack, nums)
                    first = False
                    nums.clear()

                elif stack in STACK_MANIPULATION:
                    manipulation_stack(stack, nums)
            
        elif element.isalpha():
            if element.upper() in STACK_MANIPULATION:
                nums = manipulation_stack(element.upper(), nums)
            else:
                raise ValueError("undefined operation")
            
        elif len(element) > 1 or element.isdigit():
            nums.append(int(element))

        else:
            if first and element in OPERATORS:
                
                # Check errors
                if len(nums) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                if nums[len(nums)-1] == 0 and element == '/':
                    raise ZeroDivisionError("divide by zero")
                
                first = False
                result = reduce(OPERATORS.get(element), nums)
            else:
                if element in OPERATORS:
                    nums.insert(0, result)
                    result = operation_stack(element, nums)

            nums.clear()

    return [result] if not first else nums

def get_user_defined(inputs, user_defined):
    
    inputs = inputs[1:-1].split()
    name = inputs[0].upper()
    if name.isdigit() or (name[0] == '-' and name[1:].isdigit()):
            raise ValueError('illegal operation')
    value = [v.upper() for v in inputs[1:]]
    i = 0
    while i < len(value):
        if value[i] in user_defined:
            value = value[:i] + user_defined[value[i]] + value[i+1:]
        i += 1
    
    return name, value

def operation_stack(stack, nums):
    match stack:
        case '+':
            result = reduce(OPERATORS.get('+'), nums)
        case '-':
            result = reduce(OPERATORS.get('-'), nums)
        case '*':
            result = reduce(OPERATORS.get('*'), nums)
        case '/':
            # Check division by zero
            if nums[len(nums)-1] == 0 and stack == '/':
                raise ZeroDivisionError("divide by zero")
            result = reduce(OPERATORS.get('/'), nums)
    
    return result

def manipulation_stack(stack, nums):
    match stack:
        case 'DUP':
            nums = dup(nums)
        case 'DROP':
            nums = drop(nums)
        case 'SWAP':
            nums = swap(nums)
        case 'OVER':
            nums = over(nums)

    return nums

# print(evaluate(["foo"]))                                      # [12]
# print(evaluate([": + * ;", "3 4 +"]))                         # [12]
# print(evaluate([": countup 1 2 3 ;", "countup"]))             # [1, 2, 3]
# print(evaluate([": dup-twice dup dup ;", "1 dup-twice"]))     # [1, 1, 1]
# print(evaluate(["1 swap"]))                                   # [1, 3, 2]
# print(evaluate(["1 2 over"]))                                 # [1, 3, 2]
# print(evaluate(["1 2 3 swap"]))                               # [1, 3, 2]
# print(evaluate(["1 2 drop"]))                                 # [1]
# print(evaluate(["1 dup"]))                                    # [1, 1]
# print(evaluate(["4 0 /"]))                                    # "divide by zero"
# print(evaluate(["1 /"]))                                      # "Insufficient number of items in stack"
# print(evaluate(["3 4 -"]))                                    # [-1]
# print(evaluate(["-1 -2 -3 -4 -5"]))                           # [-1, -2, -3, -4, -5]
# print(evaluate(["1 2 3 4 5"]))                                # [1, 2, 3, 4, 5]
# print(evaluate(["2 4 * 3 /"]))                                # [2]
print(evaluate(["1 2 + 4 -"]))                                # [-1]
# print(evaluate([": swap dup ;", "1 swap"]))