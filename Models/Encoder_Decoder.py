import keras 
from keras.layers import Bidirectional,LSTM,Dense,Lambda,Input,Flatten,TimeDistributed
from keras.models import Model
import keras.backend as K


import tensorflow as tf 

import numpy as np


def mean(x):

    return K.mean(x,axis=1,keepdims=True)

def sum_layers(x):

    return K.sum(x,axis=1,keepdims=True)





def EncoderDecoder(input_shape,num_class):

    
    inp = Input(shape=input_shape)
    """ encoding and dimensionality reduction """

    e1        = Bidirectional(LSTM(40,return_sequences=True,activation='relu'),merge_mode='concat')(inp)
    #e2        = LSTM(25,return_sequences=True,activation='relu')(e1)
    

    encoded   = TimeDistributed(Dense(10,activation='relu'))(e1)


    """ decoding part and restoration """
    #d1      = LSTM(20,return_sequences=True,activation='relu')(encoded)
    #d2      = LSTM(30,return_sequences=True,activation='relu')(d1)

    decoded = Bidirectional(LSTM(25,return_sequences=True,name="decoded",activation='relu'),merge_mode='concat',name="decoded")(encoded) 
    
    
    """ the category branch to predict the context of input """

    #merged  = Lambda(sum_layers,output_shape=(1,10))(encoded)
    #out_cat = Lambda(lambda x:x[:,0],name="embedding")(merged)

    flat     = Flatten()(encoded)
    #dens1    = Dense(20,activation='relu')(flat)
    #dens2    = Dense(10,activation="relu")(dens1)
    category = Dense(num_class,activation='softmax',name="context")(flat)

    
    model = Model(inp,[decoded,category])

    losses = {

         "decoded":"mae",
         "context":"categorical_crossentropy"

    }

    metrics = {

        "decoded":"mae",
        "context":"accuracy"
    }

    loss_weigths = {

           "decoded":1,
           "context":10

    }

    model.compile(optimizer='adam',loss=losses,metrics=metrics,loss_weights=[1,100])

    return model 

    """ return the embedding and the category """
    #return out_cat,category,decoded
"""
model = EncoderDecoder()
model.summary()

X = []
Y = []

for i in range(100):

     sent = np.random.rand(20,20)
     X.append(sent)
    

     y = np.random.rand(3)
     Y.append(y) 

X = np.array(X)
Y = np.array(Y)

model.fit(X,[X,Y],epochs=100)
"""






     
