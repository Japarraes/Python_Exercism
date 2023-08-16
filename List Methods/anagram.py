def find_anagrams(word, candidates):
    
    # # Create sorted list from word in lower case
    # list_word = sorted(list(word.lower()))

    # # List to save anagrams
    # result = []

    # for candidate in candidates:
    #     # Check word and candidate to anagram are not the same word
    #     if candidate.lower() != word.lower():

    #         # Created sorted list from candidate in lower case 
    #         list_candidate = sorted(list(candidate.lower()))

    #         # if both lists are the same, candidate is an anagram
    #         if list_candidate == list_word:
    #             result.append(candidate)

    # return result

    return [
        candidate
        for candidate in candidates
        if candidate.lower() != word.lower() and 
            sorted(candidate.lower()) == sorted(word.lower())
    ]



candidates = ["patter"]
print(find_anagrams("tapper", candidates))          # []
# candidates = ["Eons", "ONES"]
# print(find_anagrams("nose", candidates))          # ["Eons", "ONES"]
# candidates = ["dog", "goody"]
# print(find_anagrams("good", candidates))          # []
# candidates = ["lemons", "cherry", "melons"]
# print(find_anagrams("solemn", candidates))          # ["lemons", "melons"]