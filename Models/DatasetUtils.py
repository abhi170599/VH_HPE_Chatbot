import numpy as np
import nltk 
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
import keras 
from keras.models import load_model






model = load_model('Embedder_7.h5')


stopwords = set(stopwords.words('english'))
stemmer = LancasterStemmer()

model.summary()

"""
arr = np.random.rand(1,213)

vect,context = model.predict(arr)

print(vect,context)
"""

def get_words(input_text):

    words = word_tokenize(input_text)
    
    word_list = []
    for word in words:

        if word.lower() not in stopwords:

            word_list.append(word.lower())
    

    return list(set(word_list))        

    




def padding_sequence(sequence,max_length,vocabsize):

    """ Pad the sequences to increase their length to the max_sequence_length """

    seq_length = sequence.shape[0]

    added_vecs = np.zeros((max_length-seq_length,vocabsize))

    sequence   = np.concatenate((sequence,added_vecs),axis=0)

    return sequence


def create_sequence(input_text):

    words = get_words(input_text)

    sequence = []

    





""" creating dataset for sent2vec model """


def create_bag(inputs):

    bag = []
    sents = []
    
    for text in inputs:

        words = get_words(text)
        sents.append(words)

        for word in words:
            if word not in bag:
                bag.append(word)

    return bag,sents




def create_vector(input_sentence,bag):

    vocabsize = len(bag)
    vect = np.zeros(vocabsize)

    for word in input_sentence:

        if word in bag:

            index = bag.index(word)
            vect[index]=1

    vect_embedding = model.predict(vect.reshape(-1,len(bag)))
    return vect_embedding 


def get_sent_vecs(sentences,bag):

    vecs = []
    for sent in sentences:

        vec = create_vector(sent,bag)
         
        vecs.append(vec)


    return vecs    


















