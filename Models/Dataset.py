import numpy as np 
import json 
import pickle
import gensim 
import keras
from keras.models import load_model

from gensim.models import Word2Vec

from matplotlib import pyplot as plt

from Sent2Vec import sent2vec,embedding_model

from DatasetUtils import * 

DATASET_PATH = "dataset.json"


"read the json file"

question_list = []

answers_file = open('answers_updated.pickle','rb')
answers      = pickle.load(answers_file)


irrelevent_answers = [
            
            "Hey!",

            "Hello",

            "Fine",

            "Good",

            "Nice to meet you too",

            "I am doing good, What about you?",

            "Good morning",

            "The sky's up but I'm fine thanks. What about you"

]    



answers_list = answers['answers']+irrelevent_answers

print(len(answers_list))

json_file = open(DATASET_PATH)
data      = json.load(json_file)

labels = list(data.keys())

question_list = []
for label in labels:

    question_list+=data[label]


bag,sentences = create_bag(question_list)

X = []
Y = []


question_dict = {}

i=0

for label in labels:


    
    question_dict[label] = []

    """ create the context labels """
    y = np.zeros(len(labels))
    y[labels.index(label)]=1

    for ques in data[label]:

        vect = create_vector(get_words(ques),bag)
        X.append(vect)
        Y.append(y)

        dict_ques = {"vector":vect,"answer":answers_list[i]}

        question_dict[label].append(dict_ques)
        i+=1

""" creating word2vec model """

data_word2vec = []
for label in labels:


    
    

    """ create the context labels """
    for ques in data[label]:

        words = get_words(ques)
        data_word2vec.append(ques)


model1 = gensim.models.Word2Vec(data_word2vec, min_count = 1,size = 100, window = 5)


file = open('data_7.pickle','wb')

"""
data_p = {
    "question_dict" : question_dict,
    "bow" : bag
}

pickle.dump(data_p,file)
"""
"""
X = np.array(X)
Y = np.array(Y)

print(X.shape,Y.shape)

model = sent2vec(len(bag),20,len(labels))

MODEL_PATH = 'sent_to_vec_7.h5'

num_epochs = 100

history = model.fit(X,[X,Y],epochs=num_epochs)
model.save(MODEL_PATH)

embed = embedding_model(model,3)
embed.save('Embedder_7.h5')

loss = list(history.history['loss'])
itr  = np.arange(num_epochs)

plt.figure()
plt.plot(itr,loss)
plt.show()
"""

import numpy as np 
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity


stopwords = set(stopwords.words('english'))

def get_vector(input_text,model,bag):

    
    words = word_tokenize(input_text)
    word_list = []
    for word in words:

        if word.lower() not in stopwords:

            word_list.append(word.lower())

    word_list = list(set(word_list))

    """ create the vector embedding with the model """

    vocabsize = len(bag)
    vect = np.zeros(vocabsize)

    for word in word_list:

        if word in bag:

            index = bag.index(word)
            vect[index]=1
    print(vect)
    vect_embedding,context = model.predict(vect.reshape(-1,len(bag)))
    return vect_embedding,context         

def get_response_from_bot(message,model,bag,labels,question_dict):

    #model.summary()
    vect,context = get_vector(message,model,bag)

    cont = labels[np.argmax(context)]

    max_similarity = 0
    response = ""

    print(cont)
    
    for questions in question_dict[cont]:

        vect_ques = questions['vector'][0]
        simi = cosine_similarity(vect,vect_ques.reshape(-1,20))

        print(simi) 
        if simi[0][0]>max_similarity:
            max_similarity = simi[0][0]
            response = questions["answer"]
    
    

    return response


model = load_model('Embedder_7.h5')







correct=0
for i  in range(len(question_list)):

    response = get_response_from_bot(question_list[i],model,bag,labels,question_dict)

    if response == answers_list[i]:

        correct+=1

print(len(answers_list))
print(correct)        
    
                            





