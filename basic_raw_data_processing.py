#This is used for taking text formatted like the following and making it ready to be used with the qti builder file's functions. This formatting is perfect for multiple choice.

"""1. What is a good question?
A. Not this one.
B. Not this one.
C. Not this one.
D. Not this one.
E. Some other question.
2. What is a good question?
A. Not this one.
B. Not this one.
C. Not this one.
D. Not this one.
E. Some other question.
"""

#It may also look like this. This would be good for creating various essay questions (Canvas's question type for short-answer and long-anwer questions.
"""1. What do you think about this question?
2. What do you think about question 2?
3. What do you think about question 3?
3. What do you think about question 4?
"""

#I've also created multiple answer questions from text like this.
"""1. some word
a related word
an unrelated word
an unrelated word
an unrelated word
a related word
an unrelated word
"""

from re import sub
def break_into_individual_questions(raw_data):
    return sub("[0-9]+\.","æ",raw_data).split("æ")
def clean_up_spacing(array_of_raw_data):
    return list(map(lambda x: sub(r"\t"," ",x.strip()),array_of_raw_data))
def split_by_line_breaks(array):
    return list(map(lambda x: sub(r"\n{1,}","@",x).split("@"),array))
