import nltk 
from nltk.tokenize import word_tokenize


""" word level trie """

class TreiNode:


    def __init__(self):

        """ Dictionary containing the next of all words """         
        self.next = {}
        
        

        
        """ Marker to determine if the node belongs to a complete question """  
        self.question_marker = False

    def add_item(self,question):

        """ add a new question to the data structure """

         
        if(len(question)==0):

            self.question_marker = True
            return
        key = question[0]
        question = question[1:]

        if key in self.next.keys():
            self.next[key].add_item(question)
        
        else:

            new_node = TreiNode()
            self.next[key]=new_node
            new_node.add_item(question)




    def dfs(self,sofar=None):

        if self.next.keys()==[]:

            print("Match : ",sofar)
            return

        elif self.question_marker==True:
             
             print("Match : ",sofar)


        for key in self.next.keys():
            self.next[key].dfs(sofar+key)


    def search(self,string,sofar=[]):

        if len(string) > 0:

            key = string[0]
            string = string[1:]
            if key in self.next.keys():
                sofar = sofar + key
                self.next[key].search(string,sofar)

            else:
                print ("No match")
		
        else:

            if self.word_marker == True:
                print( "Match:",sofar)

            for key in self.next.keys():
                self.next[key].dfs(sofar+key)


















