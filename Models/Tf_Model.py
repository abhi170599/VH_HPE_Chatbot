import tensorflow as tf 
import numpy as np 

from Encoder_Decoder import EncoderDecoder 


VOCAB_SIZE = 10
NUM_CATEGORY = 3



X = []
Y = []

for i in range(100):

     sent = np.random.rand(3,VOCAB_SIZE)
     X.append(sent)
    

     y = np.random.rand(3)
     Y.append(y) 

X = np.array(X)
Y = np.array(Y)



input_sequence = tf.placeholder(tf.float32,shape=[None,None,VOCAB_SIZE])
category       = tf.placeholder(tf.float32,shape=[None,NUM_CATEGORY])


vector,cat,decode = EncoderDecoder(input_sequence)


#mse loss for the encoder decoder
mse_loss = tf.compat.v1.losses.mean_squared_error(input_sequence,decode)

#crossentropy loss for the context
category_loss = tf.compat.v1.losses.softmax_cross_entropy(category,cat)

#total loss

total_loss    = tf.reduce_mean(tf.add(mse_loss,category_loss))

optimizer = tf.train.AdadeltaOptimizer(learning_rate=0.1).minimize(total_loss)


saver = tf.train.Saver()

MODEL_NAME = 'Chatbot'


init = tf.global_variables_initializer()


with tf.Session() as sess:

    sess.run(init)

    for epoch in range(10):

        loss = sess.run([total_loss],feed_dict={input_sequence:X,category:Y})
            
            

        print("Epoch : {}  Loss : {}".format(epoch,loss[0]))    


