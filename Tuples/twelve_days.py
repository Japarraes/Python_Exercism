lyrics_song = (
        ('first', 'and a Partridge in a Pear Tree'),
        ('second', 'two Turtle Doves'),
        ('third', 'three French Hens'),
        ('fourth', 'four Calling Birds'),
        ('fifth', 'five Gold Rings'),
        ('sixth', 'six Geese-a-Laying'),
        ('seventh', 'seven Swans-a-Swimming'),
        ('eighth', 'eight Maids-a-Milking'),
        ('ninth', 'nine Ladies Dancing'),
        ('tenth', 'ten Lords-a-Leaping'),
        ('eleventh', 'eleven Pipers Piping'),
        ('twelfth', 'twelve Drummers Drumming')
    )

def recite(start_verse, end_verse):

    # return [f"On the {lyrics_song[n][0]} day of Christmas my true love gave to me: "
    #         f"{', '.join(lyrics_song[i][1] for i in range(n, 1, -1))}"
    #         f"{', and ' if n > 1 else ''}{lyrics_song[1][1]}."
    #         for n in range(start_verse-1, end_verse)]
    result = []
    for n in range(start_verse, (end_verse + 1)):
        header = f"On the {lyrics_song[n-1][0]} day of Christmas my true love gave to me: "
        items = ", ".join([lyrics_song[i][1] for i in reversed(range(n))])
        
        if n == 1:
            items = items.replace('and ', '')

        result.append(header + items + ".")

    return result

# print(recite(1, 1))
# expected = [
#             "On the first day of Christmas my true love gave to me: "
#             "a Partridge in a Pear Tree."
#         ]
# print(recite(2, 2))
# expected = [
#             "On the second day of Christmas my true love gave to me: "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
# print(recite(3, 3))
# expected = [
#             "On the third day of Christmas my true love gave to me: "
#             "three French Hens, "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
# print(recite(4, 4))
# expected = [
#             "On the fourth day of Christmas my true love gave to me: "
#             "four Calling Birds, "
#             "three French Hens, "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
# print(recite(5, 5))
# expected = [
#             "On the fifth day of Christmas my true love gave to me: "
#             "five Gold Rings, "
#             "four Calling Birds, "
#             "three French Hens, "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
# print(recite(6, 6))
# expected = [
#             "On the sixth day of Christmas my true love gave to me: "
#             "six Geese-a-Laying, "
#             "five Gold Rings, "
#             "four Calling Birds, "
#             "three French Hens, "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
# print(recite(7, 7))
# expected = [
#             "On the seventh day of Christmas my true love gave to me: "
#             "seven Swans-a-Swimming, "
#             "six Geese-a-Laying, "
#             "five Gold Rings, "
#             "four Calling Birds, "
#             "three French Hens, "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
# print(recite(8, 8))        
# expected = [
#             "On the eighth day of Christmas my true love gave to me: "
#             "eight Maids-a-Milking, "
#             "seven Swans-a-Swimming, "
#             "six Geese-a-Laying, "
#             "five Gold Rings, "
#             "four Calling Birds, "
#             "three French Hens, "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
# print(recite(9, 9))
# expected = [
#             "On the ninth day of Christmas my true love gave to me: "
#             "nine Ladies Dancing, "
#             "eight Maids-a-Milking, "
#             "seven Swans-a-Swimming, "
#             "six Geese-a-Laying, "
#             "five Gold Rings, "
#             "four Calling Birds, "
#             "three French Hens, "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
# print(recite(10, 10))
# expected = [
#             "On the tenth day of Christmas my true love gave to me: "
#             "ten Lords-a-Leaping, "
#             "nine Ladies Dancing, "
#             "eight Maids-a-Milking, "
#             "seven Swans-a-Swimming, "
#             "six Geese-a-Laying, "
#             "five Gold Rings, "
#             "four Calling Birds, "
#             "three French Hens, "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
# print(recite(11, 11))
# expected = [
#             "On the eleventh day of Christmas my true love gave to me: "
#             "eleven Pipers Piping, "
#             "ten Lords-a-Leaping, "
#             "nine Ladies Dancing, "
#             "eight Maids-a-Milking, "
#             "seven Swans-a-Swimming, "
#             "six Geese-a-Laying, "
#             "five Gold Rings, "
#             "four Calling Birds, "
#             "three French Hens, "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
# print(recite(12, 12))
# expected = [
#             "On the twelfth day of Christmas my true love gave to me: "
#             "twelve Drummers Drumming, "
#             "eleven Pipers Piping, "
#             "ten Lords-a-Leaping, "
#             "nine Ladies Dancing, "
#             "eight Maids-a-Milking, "
#             "seven Swans-a-Swimming, "
#             "six Geese-a-Laying, "
#             "five Gold Rings, "
#             "four Calling Birds, "
#             "three French Hens, "
#             "two Turtle Doves, "
#             "and a Partridge in a Pear Tree."
#         ]
print(recite(1, 3))
# expected = [recite(n, n)[0] for n in range(1, 4)]
# print(recite(4, 6))
# expected = [recite(n, n)[0] for n in range(4, 7)]
# print(recite(1, 12))
# expected = [recite(n, n)[0] for n in range(1, 13)]
