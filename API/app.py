from flask import Flask, request, jsonify, render_template, redirect
import os
import json
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_jwt_extended import (

    JWTManager, jwt_required, create_access_token, get_jwt_identity
)

import gensim 
from gensim.summarization.summarizer import summarize 

import numpy as np
import keras
from keras.models import load_model
import warnings 

import pickle
warnings.filterwarnings("ignore")

from flask_cors import CORS

from database import db_session
from models import User,Chathead,Message

from Utils.Embedder import get_response_from_bot
from Utils.language import lang_to_eng,eng_to_lang



app = Flask(__name__)
CORS(app)

file = open('Utils/data_7_updated.pickle','rb')
data = pickle.load(file)

bag = data['bow']
question_dict = data['question_dict']
labels = list(question_dict.keys())

print("\n\n............... Loaded Utitlities ..........................")

model = load_model("Utils/Embedder_7.h5")
model.summary()

vect = np.random.rand(1,224)
arr  = model.predict(vect)
print(arr)

print("\n\n................ Loaded Model ..........................")

""" reading the question file """

question_file = open('Utils/dataset.json')
questions = json.load(question_file)

print("\n\n.................. Loaded the Questions ...................")

SUPPORTED_LANGUAGES = ['en','fr','ta','hi']


""" setting up the JWT """
app.config['JWT_SECRET_KEY'] = 'abhisheksagnikyashrahul'
jwt = JWTManager(app)



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    return jsonify("Pong")


#user signup endpoint
@app.route('/signup',methods=['POST'])
def signup():

    data = request.get_json()
    username = data.get("username")
    password = generate_password_hash(data.get("password"))

    
    try:

        new_user = User(username=username,password=password)
        db_session.add(new_user)
        db_session.commit()
    
    except:

        return jsonify({

                "status"  : "error",
                "message" : "signup failed"

        })


    return jsonify({

        "status"  : "success",
        "message" : "Signed Up successfuly"
    }),201        


#user login endpoint
@app.route('/signin',methods=['POST'])
def signin():

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password,password):

        return jsonify({

             "status"  : "failed",
             "message" : "Failed to signin"

        })

    #generating a token
    access_token = create_access_token(identity=username)

    return jsonify({


          "status"  : "success",
          "message" : "login successful",
          "data"    : {

                     "id"       : user.id,
                     "token"    : access_token,
                     "username" : user.username
          }
      }),200    



#activating a chat head
@app.route('/chat',methods=["POST","DELETE"])
@jwt_required
def activate_chat():

    request_data = request.get_json()
    user         = request_data.get('user','')

    #check if there is a chathead with this user
    flag = False

    chat = Chathead.query.filter(Chathead.user_id==user).first()

    if not chat:
        
        flag = True
        try:

            new_chat_head = Chathead()
            new_chat_head.user_id = user
            db_session.add(new_chat_head)
            db_session.commit()

            

              


        except:

            return jsonify({

                "status"  : "error",
                "message" : "chat creation failed"
            })

    chat = Chathead.query.filter(Chathead.user_id==user).first()
    
    if flag:
        """ if new chat is formed enter a welcome message """
        new_message = Message(message="Hey! I am a chatbot",chat=chat.id)
        new_message.user = user
        new_message.from_bot=1              #the message is from bot
    
        db_session.add(new_message)
        db_session.commit()


    return jsonify({

        "status"  : "success",
        "message" : "chat creation successful",
        "chat_id" : chat.id
    })


# endpoint to send a message

@app.route("/send",methods=["POST"])
@jwt_required
def send_message():

    request_data = request.get_json()
    user         = request_data.get('user','')
    message      = request_data.get('message','')
    chat         = request_data.get('chat')

    '''create new message'''

    new_message = Message(message=message,chat=chat)
    new_message.user = user
    new_message.from_bot=0
    
    db_session.add(new_message)
    db_session.commit()

    """ TODO : get the response of the message 
    from the model and create a new message
    """

    responses = get_response_from_bot(message,model,bag,labels,question_dict)
    new_message = Message(message=responses,chat=chat)
    new_message.user = user                                    #the responses are from chatbot
    new_message.from_bot = 1

    db_session.add(new_message)
    db_session.commit()


    return jsonify({

        "status":"success",
        "message":"message sent successfuly"
    })


""" to get response of a messgae """
@app.route("/get_response",methods=["POST"])
@jwt_required
def get_response():

    request_data = request.get_json()
    user         = request_data.get('user','')
    message      = request_data.get('message','')
    chat         = request_data.get('chat')

    lang,message_eng = lang_to_eng(message)

    print(lang,message_eng)

    '''create new message'''

    new_message = Message(message=message_eng,chat=chat)
    new_message.user = user
    new_message.from_bot=0
    
    db_session.add(new_message)
    db_session.commit()

    """ TODO : get the response of the message 
    from the model and create a new message
    """
    
    responses,similar,context  = get_response_from_bot(message_eng,model,bag,labels,question_dict,2,questions)
    #summarized = summarize(responses)

    if lang in SUPPORTED_LANGUAGES:
        responses = eng_to_lang(responses,lang)
        
    new_message = Message(message=responses,chat=chat)
    new_message.user = user                                    #the responses are from chatbot
    new_message.from_bot = 1

    db_session.add(new_message)
    db_session.commit()


    try:

        return jsonify({
          
        "message":responses,
        "similar":similar,
        "context":context,
        "status" : "success"

        })

    except:

        return jsonify({
          
        "status":"faliure",
        "message":"could not get response"

    })






    



#getting user messages
@app.route('/get_message/<chat_id>')
@jwt_required
def user_messages(chat_id):

    messages = Message.query.filter(Message.chat == chat_id).all()

    return jsonify([

          {

            "id"      : message.id,
            "message" : message.message,
            "chat" :  message.chat,
            "user"    : message.user,
            "bot"     : message.from_bot
          }
          for message in messages
      
    ])

"""
def get_response(message):

    return "this is the response"
"""
    

""" run the application """
if __name__ == "__main__":
    app.run(debug=True)

