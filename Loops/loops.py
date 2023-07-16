"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    
    list_round = []
    while student_scores:
        list_round.append(round(student_scores.pop()))
    
    return list_round

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    
    return count

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    
    return best_scores

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    incr = round((highest - 40)/4)
    interval = []
    for i in range(4):
        interval.append(41 + (i * incr))
    
    return interval

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    list_rank = []
    for index, score in enumerate(student_scores):
        list_rank.append(f"{index+1}. {student_names[index]}: {score}")
    
    return list_rank

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    list_first = []
    for student in student_info:
        if student[1] == 100:
            return student

    return list_first

# print(round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))
# print(count_failed_students([89, 85, 42, 57, 90, 100, 95, 48, 70, 96]))
# print(above_threshold([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 78))
# print(letter_grades(97))
# print(student_ranking([88, 73], ['Paul', 'Ernest']))
print(perfect_score([['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100]]))