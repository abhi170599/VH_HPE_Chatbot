import gensim 
from gensim.models import Word2Vec 
import json
import nltk 
from nltk.tokenize import word_tokenize
import numpy as np
import pickle
 
from Encoder_Decoder import EncoderDecoder
from DatasetUtils import get_words
from matplotlib import pyplot as plt 

question_list = []

with open('dataset.json') as json_file:

    data = json.load(json_file)

    for label in list(data.keys()):

        for ques in data[label]:

            question_list.append(get_words(ques))


#print(len(question_list))

model = Word2Vec(question_list, min_count = 1,size = 50, window = 5)


max_length = 0
for ques in question_list:

    if len(ques)>max_length:
        max_length = len(ques)

print(max_length)


def get_sequence(input_text):

    vector_sequence = []

    if len(input_text)>0:
        for word in input_text:

            try:
               vect = model[word]
           
           

            except:
               vect = np.zeros((1,50))

            vector_sequence.append(vect)
    else:

        vect = np.zeros(50)
        vector_sequence.append(vect)        

    return np.array(vector_sequence)






def padding_sequence(sequence,max_length,vocabsize):

    """ Pad the sequences to increase their length to the max_sequence_length """

    seq_length = sequence.shape[0]

    added_vecs = np.zeros((max_length-seq_length,vocabsize))

    #print(sequence.shape)
    #print(added_vecs.shape)

    #print("\n\n")

    sequence   = np.concatenate((sequence,added_vecs),axis=0)

    return sequence


X = []
Y = []

with open('dataset.json') as json_file:
    

    
    data = json.load(json_file)

    labels = list(data.keys())
    for label in list(data.keys()):

        y = np.zeros(len(data.keys()))
        y[labels.index(label)]=1
        

        for ques in data[label]:

            ques_words = get_words(ques)

            vect_seq = get_sequence(ques_words)

            #print(vect_seq)
            #print(vect_seq.shape)
            if(vect_seq.shape==(0,)):
                print(ques)

            vect_seq = padding_sequence(vect_seq,max_length,50)

            X.append(vect_seq)
            Y.append(y)


X = np.array(X)
Y = np.array(Y)
"""
model.save('Word2Vec.model')
"""
print(X.shape)
print(Y.shape)


seq2seq = EncoderDecoder((13,50),8)
seq2seq.summary()

history = seq2seq.fit(X,[X,Y],epochs=50)

itr = np.arange(50)
loss = history.history['loss']

plt.figure()
plt.plot(itr,loss)
plt.show()






          


