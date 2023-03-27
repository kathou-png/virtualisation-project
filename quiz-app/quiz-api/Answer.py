# Exemple de création de classe en python
from cgitb import text
import json


class Answer:
    """Answer constructor
    values can be null
    takes params : question_number (int), text(str), isCorrect(str), answer_number(int))
    """
    def __init__(self, question_number = 0, text = "", isCorrect = "", answer_number = 0):
        self.question_number = question_number
        self.text = text
        self.isCorrect = isCorrect
        self.answer_number = answer_number

    """Put the json data into the python Answer
    Put all the information : question_number, text, isCorrect, position, answer_number (not used ?)

    request_json['possibleAnswers'][indice]['isCorrect'] is true in json but True in python
    It is inserted as True 
    """
    def json_to_object(self, request_json, indice):
        self.question_number = request_json['position']
        self.text = request_json['possibleAnswers'][indice]['text']
        self.isCorrect = request_json['possibleAnswers'][indice]['isCorrect']
        self.answer_number = indice + 1

    """Returns the json version of the Answer
    In the database, isCorrect is True
    we transform it to "true" and then to true
    """
    def object_to_json(self):
        temp_bool = False
        if(self.isCorrect == "False"):
            temp_bool = False
        else:
            temp_bool = True
        
        data = {'text' : self.text, 'isCorrect': temp_bool}

        data_str = json.dumps(data)
        data_json = json.loads(data_str)

        return data_json

    def print(self):
        print(
            "-------------------------" \
            + "\n question_number : " + str(self.question_number) \
            + "\n text : " + self.text \
            + "\n isCorrect : " + str(self.isCorrect) \
            + "\n answer_number : " + str(self.answer_number) \
            + "\n-------------------------"    
            )