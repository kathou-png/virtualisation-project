from flask import Flask, request
from Answer import Answer
from Participation import Participation
from Question import Question
from answerSummary import answerSummary
from db_utils import *
from flask_cors import CORS

from jwt_utils import build_token
import json

import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	size = get_quiz_size()
	scores = get_quiz_info()
	return {"size": size, "scores": scores}, 200


@app.route('/login', methods=['GET', 'POST'])
def Login():
	payload = request.get_json()
	if(payload['password'] == "Vive l'ESIEE !"):
		token = build_token()
		return {"token": str(token)}, 200
	else :
		return '', 401


"""
Step 1 : Get the json given in the body of the request
Step 2 : Put the json's values into the right database's columns 
"""
@app.route('/questions', methods=['GET','POST'])
def PostQuestion():
	if(request.headers.get('Authorization')):
		#Get the body(json) of the question
		#Transform it into our python object
		q1 = Question()
		q1.json_to_object(request.get_json())
		#Put the python object into the database
		insert_question_into_bd(q1)

		#Get the json of the answers
		a1 = Answer()
		answer = request.get_json()['possibleAnswers']
		for i in range(len(answer)):
			#Transform it into our python object
			a1.json_to_object(request.get_json(), i)
			#Put the python object into the database
			insert_answer_into_bd(a1)
		return '', 200
	else:
		return '', 401

"""
Step 1 : Request the database to select the question and its answer with the position given in param
Step 2 : Transform the database result to a python object
Step 3 : Return the json value of the python object
"""
@app.route('/questions/<position>', methods=['GET'])
def GetQuestionNumber(position):
	entire_question_json = select_question_with_position(position)
	if(entire_question_json['title'] != ""):
		return select_question_with_position(position), 200
	else :
		#Question not found
		return '', 404

@app.route('/questions/<position>', methods=['DELETE'])
def DeleteQuestion(position):
	if(request.headers.get('Authorization')):
		if(delete_question_with_position(position) == True):
			return '', 204
		else:
			# Non existing question
			return '', 404
	else:
		# Non authorized
		return '', 401

@app.route('/questions/<position>', methods=['PUT'])
def UpdateQuestion(position):
	if(request.headers.get('Authorization')):
		q1 = Question()
		q1.json_to_object(request.get_json())
		if(update_question_with_position(q1, position) == True):
			return '', 200
		else:
			# Non existing question
			return '', 404
	else:
		# Non authorized
		return '', 401



########## PARTICIPATIONS ##########

@app.route('/participations', methods=['GET', 'POST'])
def PostParticipation():
	if(request.get_json()):

		p1 = Participation()
		p1.json_to_object(request.get_json())
		participation_length = len(p1.answers_input)
		if (verify_participation_completion(participation_length) == True):
			print("Correct participation")


			i = 1
			for ans in p1.answers_input:
				answerIsCorrect = False
				if( select_correct_answer_position(i) == ans):
					answerIsCorrect = True

				data = {'correctAnswerPosition' : select_correct_answer_position(i), 'wasCorrect': answerIsCorrect}
				data_str = json.dumps(data)
				data_json = json.loads(data_str)

				p1.answersSummaries.append(data_json)
				i += 1


			print(str(p1.countCorrect()))
			p1.score = p1.countCorrect()
			
			p1.print()

			insert_participationResult_into_bd(p1)
			return(p1.object_to_json())
		else:
			#incorrect participation
			print("incorrect participation")
			return '', 400
	else:
		print("incorrect json")
		return '', 401




@app.route('/participations', methods=['DELETE'])
def DeleteAllParticipations():
	if(request.headers.get('Authorization')):
		delete_all_participations()
		return '', 204
	else:
		# Non authorized
		return '', 401


if __name__ == "__main__":
    app.run()	