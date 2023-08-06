import string

def count_words(sentence):
    
    sentence = sentence.replace("\n", " ").replace("\t", " ").replace("_", " ").replace(",", " ").lower()
    # sentence = sentence.replace("\t", " ")
    # sentence = sentence.replace("_", " ")
    # sentence = sentence.replace(",", " ").lower()
    # sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    words = sentence.split(" ")
    words = [word.rstrip(string.punctuation).lstrip(string.punctuation) for word in words]

    dict_result = {} 
    for word in words:
        if word != "":
            dict_result[word] = words.count(word)

    return dict_result

# print(count_words("car: carpet as java: javascript!!&@$%^&")) # {"car": 1, "carpet": 1, "as": 1, "java": 1, "javascript": 1}
# print(count_words("one,two,three"))                           # {"one": 1, "two": 1, "three": 1}
# print(count_words("one,\ntwo,\nthree"))                         # {"one": 1, "two": 1, "three": 1}
# print(count_words("go Go GO Stop stop"))                        # {"go": 3, "stop": 2}
# print(count_words("'First: don't laugh. Then: don't cry. You're getting it.'"))     
            # {
            #     "first": 1,
            #     "don't": 2,
            #     "laugh": 1,
            #     "then": 1,
            #     "cry": 1,
            #     "you're": 1,
            #     "getting": 1,
            #     "it": 1,
            # }
# print(count_words("rah rah ah ah ah	roma roma ma	ga ga oh la la	want your bad romance"))
            # {
            #     "rah": 2,
            #     "ah": 3,
            #     "roma": 2,
            #     "ma": 1,
            #     "ga": 2,
            #     "oh": 1,
            #     "la": 2,
            #     "want": 1,
            #     "your": 1,
            #     "bad": 1,
            #     "romance": 1,
            # }
print(count_words("hey,my_spacebar_is_broken")) # {'hey': 1, 'my': 1, 'spacebar': 1, 'is': 1, 'broken': 1}
