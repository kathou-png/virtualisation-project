import json
from Answer import Answer
from answerSummary import answerSummary

class Participation:
    """Participation constructor
        values can be null
        takes params : player_name : le nom du joueur qui poste son questionnaire
        answers : la liste des positions de réponses choisies dans l’ordre des questions du quiz
    """
    def __init__(self, playerName = "", score = 0, answersSummaries = [], date = ""):
        self.playerName = playerName
        self.score = score

        self.answersSummaries = answersSummaries
        self.date = date

    
    """Put the json data into the python Participation
    """
    def json_to_object(self, request_json):
        self.playerName = request_json['playerName']

        #answerSummary.json_to_object(request_json)
        self.answers_input = request_json['answers']
        self.answersSummaries.clear()
        


    """Returns the json version of the Participation
    """
    def object_to_json(self):
        return {"playerName" : self.playerName, "score" : self.score , "answersSummaries" : self.answersSummaries}
        """
        answersSummaries : [
        {
            correctAnswerPosition : 2,
            wasCorrect : true
        },
        {
            correctAnswerPosition : 1,
            wasCorrect : false
        },....

        {
            correctAnswerPosition : 3,
            wasCorrect : true
        }
        ],
        playerName : "Anton",
        score : 4
        """
        return data_json

    def countCorrect(self):
        sum = 0
        for ans in self.answersSummaries:
            if(ans['wasCorrect'] == True):
                sum += 1
        return sum

    def print(self):
        print(
            "-------------------------" \
            + "\n playerName : " + self.playerName \
            + "\n score : " + str(self.score) \
            + "\n-------------------------"    
        )
        print("answersSummaries : ")
        print(self.answersSummaries)
