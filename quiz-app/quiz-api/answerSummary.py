"""
- **answersSummaries** : tableau de type answerSummary, dont chaque entrée donne, dans l’ordre des questions du quiz :
    - correctAnswerPosition : position de la réponse correcte à la question
    - wasCorrect : état de la réponse fournie par le joueur
"""
import json
from db_utils import select_correct_answer_position


class answerSummary:
    """answerSummary constructor
    values can be null
    """
    def __init__(self, correctAnswerPosition = 0, wasCorrect  = False):
        self.correctAnswerPosition = correctAnswerPosition
        self.wasCorrect = wasCorrect


    """Put the json data into the python Answer
    answers = [1,2,3,1....]
    """
    def json_to_object(self, request_json, indice):
        correctAnswerPos = select_correct_answer_position(indice)
        #if for question at indice, the json answer is the same as the correct answer_number then the player answered well
        if(request_json()['answers'][indice] == correctAnswerPos):
            isCorrect = True
        else:
            isCorrect = False
        self.correctAnswerPosition = correctAnswerPos
        self.wasCorrect = isCorrect


    """Returns the json version of the Answer
    In the database, isCorrect is True
    we transform it to "true" and then to true
    """
    def object_to_json(self):
        temp_bool = False
        if(self.wasCorrect == "False"):
            temp_bool = False
        else:
            temp_bool = True
        
        data = {'correctAnswerPosition' : self.correctAnswerPosition, 'wasCorrect': temp_bool}

        data_str = json.dumps(data)
        data_json = json.loads(data_str)

        return data_json

    def print(self):
        print(
            "-------------------------" \
            + "\n correctAnswerPosition : " + str(self.correctAnswerPosition) \
            + "\n wasCorrect : " + str(self.wasCorrect) \
            + "\n-------------------------"    
            )