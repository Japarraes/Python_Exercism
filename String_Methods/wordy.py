def answer(question):
    
    question = question.replace("What is ", "")
    question = question.replace("?", "")
    question = question.replace("plus", "+")
    question = question.replace("minus", "-")
    question = question.replace("multiplied by", "*")
    question = question.replace("divided by", "/")
    question = question.split(" ")
    question.insert(0, "(")
    question.insert(4, ")")
    
    # Check is the question contains an unknown operation.
    for word in question:
        if word.isalpha() and word not in ("What", "is"):
            raise ValueError("unknown operation")

    # Evaluate operation and Check is the question is malformed or invalid.
    try:
        return eval(" ".join(question))
    except:
        raise ValueError("syntax error")

    
# print(answer("What is 5?"))                                     # 5
# print(answer("What is 1 plus 1?"))                              # 2
# print(answer("What is 53 plus 2?"))                             # 55
# print(answer("What is -1 plus -10?"))                           # -11)
# print(answer("What is 123 plus 45678?"))                        # 45801
# print(answer("What is 4 minus -12?"))                           # 16
# print(answer("What is -3 multiplied by 25?"))                   # -75
# print(answer("What is 33 divided by -3?"))                      # -11
# print(answer("What is 1 plus 1 plus 1?"))                       # 3
# print(answer("What is 1 plus 5 minus -2?"))                     # 8
# print(answer("What is 20 minus 4 minus 13?"))                   # 3
# print(answer("What is 17 minus 6 plus 3?"))                     # 14
# print(answer("What is 2 multiplied by -2 multiplied by 3?"))    # -12
print(answer("What is -3 plus 7 multiplied by -2?"))            # -8
# print(answer("What is -12 divided by 2 divided by -3?"))        # 2
# print(answer("What is 52 cubed?"))                              #"unknown operation"
# print(answer("Who is the President of the United States?"))     #"unknown operation"
# print(answer("What is 1 plus?"))                                #"syntax error"
# print(answer("What is 1 plus 2 1?"))                            #"syntax error"