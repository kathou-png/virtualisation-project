import json
import sqlite3
from Answer import Answer

from datetime import datetime

from Question import Question

def get_quiz_size():
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    select_result = cur.execute(f"SELECT COUNT(DISTINCT position) FROM question")
    output = select_result.fetchall()

    cur.execute("commit")

    return output[0][0]

def get_quiz_info():
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    select_result = cur.execute(f"SELECT * from participation order by score DESC")
    output = select_result.fetchall()
    scores = []
    for ans in output :
        name = ans[1]
        score = ans[2]
        date = ans[3]

        data = {'playerName' : name, 'score' : score, 'date' : date}
        data_str = json.dumps(data)
        data_json = json.loads(data_str)
        scores.append(data_json)

    
    return scores

def insert_question_into_bd(question):
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    entire_question_json = select_question_with_position(question.position)
    #if question already exists, replace and change others positions
    if(entire_question_json['title'] != ""):
        move_question_by(cur, question.position, 1)

    cur.execute(
    f"insert into question (title, text, position, image) values"
    f"( \"{question.title}\", \"{question.text}\", {question.position}, \"{question.image}\")")

    cur.execute("commit")

def insert_answer_into_bd(answer):
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    cur.execute(
    f"insert into answer (question_number, text, isCorrect, answer_number) values"
    f"( {answer.question_number}, \"{answer.text}\", \"{answer.isCorrect}\", {answer.answer_number})")

    cur.execute("commit")



def get_question_number():
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    cur.execute(
    f"select COUNT(*) from question")

    return int(cur.fetchone()[0])
    

def verify_participation_completion(participation_length):
    print("participation len : " + str(participation_length))
    if(get_question_number() == participation_length):
        return True
    else:
        return False



##### PARTICIPATION ##########
def insert_participationResult_into_bd(participation):
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    print(date_time)
    
    cur.execute(
    f"insert into participation (playerName, score, date) values"
    f"( \"{participation.playerName}\", {participation.score},  \"{date_time}\")")
    
    

    cur.execute("commit")		

"""
Select the correct answer position for the question at indice
"""
def select_correct_answer_position(indice):
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    select_result = cur.execute(
        f"SELECT * FROM answer WHERE question_number = {indice} AND isCorrect = 'True'"
    )

    good_answer = 0
    for out in select_result:
        good_answer = int(out[4])

    return good_answer


def delete_all_participations():
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    cur.execute(f"DELETE FROM participation")

    cur.execute("commit")


"""
def select_all_questions():
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    select_result = cur.execute("select * from question")
    output = select_result.fetchall()
    for row in output:
        print(row)


def select_questions_with_title(title):
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    select_result = cur.execute(f"select * from question where title = \"{title}\"")

    output = select_result.fetchall()
    for row in output:
        print(row)
"""


"""Select the question and its answers from the database
Returns the json of the entire question with its answers

"""
def select_question_with_position(position):
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()

    #Database request should only give 1 result
    select_questions_result = cur.execute(f"select * from question where position = {position}")
    output = select_questions_result
    q1 = Question()
    for row in output:
        #Create the question from the database values
        q1 = Question(row[2], row[3], row[1], row[4])

    #make sure the list is empty
    q1.possibleAnswers.clear()
    
    #Database requesting all answers associated with the question's position
    select_questions_result = cur.execute(f"select * from answer where question_number = {position}")
    output = select_questions_result.fetchall()
    for col in output:
        a1 = Answer(0, col[2], col[3], 0)
        q1.possibleAnswers.append(a1.object_to_json())

    return q1.object_to_json()

    
    
def delete_question_with_position(position):
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    select_result = cur.execute(f"SELECT title FROM question WHERE position = {position}")
    output = select_result.fetchall()

    #check if the line exists
    if(output != []):
        
        cur.execute(f"DELETE FROM question WHERE position = {position}")
        cur.execute(f"DELETE FROM answer WHERE question_number = {position}")
        move_question_by(cur, position, -1)
        cur.execute("commit")
        return True
    else:
        return False

def update_question_with_position(question, position):
    db_connection = sqlite3.connect('quiz-db.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")

    select_result = cur.execute(f"SELECT title FROM question WHERE position = {position}")
    output = select_result.fetchall()

    

    #check if the line exists
    if(output != []):
        #if question already exists, replace and change others positions
        if(position != question.position):
            change_question_position2(cur,  question, position)
        else :
            #UPDATE the question
            cur.execute(f"UPDATE question "
            f"SET text = \"{question.text}\", title = \"{question.title}\", image = \"{question.image}\", position = \"{question.position}\"  "
            f"WHERE position = {position}")
            
            #DELETE all the answer from the question
            cur.execute(f"DELETE FROM answer WHERE question_number = {position}")

            #INSERT all the new answers from the question
            i = 0
            for ans in question.possibleAnswers:
                cur.execute(
                f"insert into answer (question_number, text, isCorrect, answer_number) values"
                f"( {position}, \"{ans['text']}\", \"{ans['isCorrect']}\", {i})")
        
        
            

        cur.execute("commit")
        return True
    else:
        return False






######## ADDITIONAL ##############

"""When adding a question, if a question with the same position already exists :
the new question gets the position
the old question is moved

"""
def move_question_by(cur, original_position, amount):

    #move superior all col by 1
    cur.execute(f"UPDATE question "
    f"SET position = position + {amount} "
    f"WHERE position >= {original_position}")

    
    cur.execute(f"UPDATE answer "
    f"SET question_number = question_number + {amount}  "
    f"WHERE question_number >= {original_position}")


def change_question_position2(cur, question, original_position):


    insert_with_position(cur, question, original_position, 0)


    if(int(original_position) > int(question.position)):
        cur.execute(f"UPDATE question "
        f"SET position = position + 1 "
        f"WHERE position < {int(original_position)} AND position >= {int(question.position)}")

        
        cur.execute(f"UPDATE answer "
        f"SET question_number = question_number + 1 "
        f"WHERE question_number < {int(original_position)} AND question_number >= {int(question.position)}")
    else:
        cur.execute(f"UPDATE question "
        f"SET position = position - 1 "
        f"WHERE position > {int(original_position)} AND position <= {int(question.position)}")

        
        cur.execute(f"UPDATE answer "
        f"SET question_number = question_number - 1 "
        f"WHERE question_number > {int(original_position)} AND question_number <= {int(question.position)}")

    
    insert_with_position(cur, question, 0, question.position)



def insert_with_position(cur, question, src_position, dst_position):
    #Move all    
    cur.execute(
    f"insert into question (title, text, position, image) values"
    f"( \"{question.title}\", \"{question.text}\", \"{dst_position}\", \"{question.image}\")")

    i = 0
    for ans in question.possibleAnswers:
        cur.execute(
        f"insert into answer (question_number, text, isCorrect, answer_number) values"
        f"( {dst_position}, \"{ans['text']}\", \"{ans['isCorrect']}\", {i})")

    
    #DELETE all the answer from the question
    cur.execute(f"DELETE FROM question WHERE position = {src_position}")
    cur.execute(f"DELETE FROM answer WHERE question_number = {src_position}")




    
    
