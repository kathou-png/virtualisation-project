# Exemple de création de classe en python
# from asyncio.windows_events import NULL
from cgitb import text
import json
from Answer import Answer


class Question:
    """Question constructor
    values can be null
    takes params : title (str), text(str), position(int), image(str), possibleAnswers(list<Answer in json>)
    """
    def __init__(self, title = "", text = "", position = 0, image = "", possibleAnswers = []):
        self.title = title
        self.text = text
        self.position = position
        self.image = image
        self.possibleAnswers = possibleAnswers


    """Put the json data into the python Question
    Put all the information : text, title, image, position
    Fill the possibleAnswers' list with the json of all the questions
    """
    def json_to_object(self, request_json):
        self.text = request_json['text']
        self.title = request_json['title']
        self.image = request_json['image']
        self.position = request_json['position']
        
        self.possibleAnswers.clear()
        a1 = Answer()
        for i in range(len(request_json['possibleAnswers'])):
            a1.json_to_object(request_json, i)
            self.possibleAnswers.append({ "text" : a1.text, "isCorrect" : a1.isCorrect })



    """Returns the json version of the Question
    """
    def object_to_json(self):
        return {"text" : self.text, "title": self.title, "image" : self.image, "position" : self.position , "possibleAnswers" : self.possibleAnswers}

    def print(self):
        print(
            "-------------------------" \
            + "\n text : " + self.text \
            + "\n title : " + self.title \
            + "\n image : " + self.image \
            + "\n position : " + str(self.position) \
            + "\n-------------------------"    
            )
    
    def print_with_answers(self):
        print(
            "-------------------------" \
            + "\n text : " + self.text \
            + "\n title : " + self.title \
            + "\n image : " + self.image \
            + "\n position : " + str(self.position) \
            + "\n-------------------------"    
            )
        print("Answers : ")
        print(self.possibleAnswers)