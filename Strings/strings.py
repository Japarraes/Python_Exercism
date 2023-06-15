def adjective_to_verb(sentence, index):

    words = sentence.split()
    words[index] += "en"

    #return words[index]
    return words[index].replace(".", "")

print(adjective_to_verb("His expression went dark.", -1))