def response(hey_bob):

    question = hey_bob.strip()

    if not question:
        return "Fine. Be that way!"
    elif question[-1] == "?":
        if question.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure"
    elif question.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever"
 