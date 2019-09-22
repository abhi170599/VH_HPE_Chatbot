from Sent2Vec import sent2vec,embedding_model 
import numpy as np 

from Create_Data import create_bag,get_sent_vecs,create_vector

inputs = [
    
    "What are the advantages of HPE OneView",
    "What is a software-defined approach to lifecycle management",
    "Can I customize functionality and integrate HPE OneView with my existing tools and environment", 
    "Does HPE provide integration kits for customers who do not wish to develop their own", 
    "Is HPE OneView a refresh to existing HPE infrastructure management tools or a brand-new design", 
    "What capabilities does HPE OneView offer", 
    "How is HPE OneView licensed"
]             


bag,sentences = create_bag(inputs)
vecs          = get_sent_vecs(sentences,bag)



"""
q = "tell me advantages of  HPE OneView"

query_vector = create_vector(get_words(q),bag)

print(query_vector)
"""



MODEL_PATH = 'sent2vec.h5'

model = sent2vec(len(bag),10)
model.fit(np.array(vecs),np.array(vecs),epochs=200)
model.save(MODEL_PATH)


model_2 = embedding_model(MODEL_PATH,3)
model_2.summary()

model_2.save('embedder.h5')

