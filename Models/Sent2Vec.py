import keras 
from keras.layers import Dense,Input
from keras.models import Model,load_model 



def sent2vec(vocabsize,outputdim,num_cat):

    inp = Input(shape=(vocabsize,))

    """ encoding part """

    en1 = Dense(100,activation='relu')(inp)
    en2 = Dense(50,activation="relu")(en1)
    

    encoded = Dense(outputdim,activation='relu')(en2)

    de1 = Dense(50,activation='relu')(encoded)
    de2 = Dense(100,activation='relu')(de1)

    decoded = Dense(vocabsize,activation='sigmoid',name="decoded")(de2)

    """ category part """

    ca1 = Dense(20,activation="relu")(encoded)
    ca2 = Dense(10,activation="relu")(ca1)
    cat = Dense(num_cat,activation="softmax",name="context")(ca2)
  
    model = Model(inp,[decoded,cat])

    losses = {

           "decoded":"mse",
           "context":"categorical_crossentropy"  

    }

    metrics = {

          "decoded":"mse",
          "context":"acc" 


    }

    model.compile(optimizer='adam',loss=losses,metrics=metrics)

    return model  

def embedding_model(model,layer_num):

    #model = load_model(model_path)

    embed = Model(model.input,[model.layers[layer_num].output,model.layers[len(model.layers)-1].output])
    
    return embed