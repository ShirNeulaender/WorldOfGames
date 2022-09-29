from Live import set_difficulty
difficulty = set_difficulty()
from Utils import SCORES_FILE_NAME
import os


def check_if_file_exits():
    if os.path.isfile(SCORES_FILE_NAME) is not True:
        f = open(SCORES_FILE_NAME, "a")
        f.close()


def add_score():
    check_if_file_exits()
    points_of_winning = (difficulty * 3) + 5
    score_file = open(SCORES_FILE_NAME, "r")
    try:
        sum_score = int(score_file.read())
    except ValueError:
        sum_score = 0
    score_file.close()
    score_file = open(SCORES_FILE_NAME, "w")
    score_file.write(str(sum_score + points_of_winning))
