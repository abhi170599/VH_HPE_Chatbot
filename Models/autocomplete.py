import numpy as np 
import nltk

from nltk.tokenize import word_tokenize
import pickle 
import json

from trei import TreiNode

questions_list = []

with open("dataset.json") as json_file:
    data = json.load(json_file)

    for label in list(data.keys()):

        questions_list+=data[label]



def get_all_questions_in_words(questions_list):

    questions = []

    for ques in questions_list:

        questions.append(word_tokenize(ques))

    return questions



questions = get_all_questions_in_words(questions_list)

#print(questions)
root = TreiNode()

for ques in questions:

    root.add_item(ques)


input_ques = input('Enter a word')

root.search(input_ques)
















