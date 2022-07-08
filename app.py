from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from helper_class import QuestionFactory

APP = Flask(__name__)

APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/jasongersing/PycharmProjects/pythonProject/pythonProject3/DGQ/data/test.db"
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy()
DB.init_app(APP)


class Answers(DB.Model):
    uu = DB.Column(DB.String(), primary_key=True)
    correct = DB.Column(DB.String(), nullable=True)
    stem = DB.Column(DB.String(), nullable=True)
    a = DB.Column(DB.String(), nullable=True)
    b = DB.Column(DB.String(), nullable=True)
    c = DB.Column(DB.String(), nullable=True)
    d = DB.Column(DB.String(), nullable=True)
    e = DB.Column(DB.String(), nullable=True)

    def __init__(self, uu, correct, stem, a, b, c, d, e):
        self.uu = uu
        self.correct = correct
        self.stem = stem
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def __repr__(self):
        return f"Correct: {self.correct}"


APP.app_context().push()
DB.session.commit()


@APP.route('/')
def home():
    return render_template("home.html", disabled=False)


@APP.route("/reset")
def reset():
    # Drop our DB tables
    DB.drop_all()
    # Create tables according to the classes in models.py
    DB.create_all()
    return render_template('home.html', title='Reset DB')


@APP.route("/about")
def about():
    return render_template("about.html", disabled=False)


@APP.route("/question1", methods=['POST', 'GET'])
def question1():
    question = QuestionFactory(1).No_of_Primes()
    test_data = Answers(uu=str(question.uuid), correct=question.correct,
                        stem=question.question_stem, a=question.ac_list[0],
                        b=question.ac_list[1], c=question.ac_list[2], d=question.ac_list[3],
                        e=question.ac_list[4])
    if request.method == 'GET':
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "question1.html", disabled=False, message1=question.question_stem, message2=question.ac_list[0],
            message3=question.ac_list[1], message4=question.ac_list[2], message5=question.ac_list[3],
            message6=question.ac_list[4], message8=question.uuid)
    if request.method == 'POST':
        answer = request.values.get('Answer').upper()
        token = request.values.get('uuid')
        db_answer = Answers.query.filter(Answers.uu == token).one()
        if answer != db_answer.correct:
            response = "TRY AGAIN"
        else:
            response = "CORRECT!"
        return render_template(
            "question1.html", disabled=False, message1=db_answer.stem, message2=db_answer.a,
            message3=db_answer.b, message4=db_answer.c, message5=db_answer.d,
            message6=db_answer.e, message7=response, message9=db_answer)


@APP.route("/question2", methods=['POST', 'GET'])
def question2():
    question = QuestionFactory(2).sum_of_first_n_numbers()
    q2 = question[0]
    ac_list = question[1]
    correct = question[2]
    uuid = str(question[3])
    a = ac_list[0]
    b = ac_list[1]
    c = ac_list[2]
    d = ac_list[3]
    e = ac_list[4]
    test_data = Answers(uu=uuid, correct=correct)
    if request.method == 'GET':
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "question2.html", disabled=False, message1=q2, message2=a, message3=b,
            message4=c, message5=d, message6=e, message8=uuid)
    if request.method == 'POST':
        answer = request.values.get('Answer2').upper()
        token = request.values.get('uuid')
        db_answer = Answers.query.filter(Answers.uu == token).one()
        if answer != db_answer.correct:
            response = "TRY AGAIN"
        else:
            response = "CORRECT!"
        return render_template(
            "question2.html", disabled=False, message1=q2, message2=a, message3=b,
            message4=c, message5=d, message6=e, message7=response, message9=db_answer)


@APP.route("/question3", methods=['POST', 'GET'])
def question3():
    question = QuestionFactory(3).mf_rat_ratio()
    q3 = question[0]
    ac_list = question[1]
    correct = question[2]
    uuid = str(question[3])
    a = ac_list[0]
    b = ac_list[1]
    c = ac_list[2]
    d = ac_list[3]
    e = ac_list[4]
    test_data = Answers(uu=uuid, correct=correct)
    if request.method == 'GET':
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "question3.html", disabled=False, message1=q3, message2=a, message3=b,
            message4=c, message5=d, message6=e, message8=uuid)
    if request.method == 'POST':
        answer = request.values.get('Answer3').upper()
        token = request.values.get('uuid')
        db_answer = Answers.query.filter(Answers.uu == token).one()
        if answer != db_answer.correct:
            response = "TRY AGAIN"
        else:
            response = "CORRECT!"
        return render_template(
            "question3.html", disabled=False, message1=q3, message2=a, message3=b,
            message4=c, message5=d, message6=e, message7=response, message9=db_answer)


@APP.route("/question4", methods=['POST', 'GET'])
def question4():
    question = QuestionFactory(4).age_diff()
    q4 = question[0]
    ac_list = question[1]
    correct = question[2]
    uuid = str(question[3])
    a = ac_list[0]
    b = ac_list[1]
    c = ac_list[2]
    d = ac_list[3]
    e = ac_list[4]
    test_data = Answers(uu=uuid, correct=correct)
    if request.method == 'GET':
        DB.session.add(test_data)
        DB.session.commit()
        return render_template(
            "question4.html", disabled=False, message1=q4, message2=a, message3=b,
            message4=c, message5=d, message6=e, message8=uuid)
    if request.method == 'POST':
        answer = request.values.get('Answer4').upper()
        token = request.values.get('uuid')
        db_answer = Answers.query.filter(Answers.uu == token).one()
        if answer != db_answer.correct:
            response = "TRY AGAIN"
        else:
            response = "CORRECT!"
        return render_template(
            "question4.html", disabled=False, message1=q4, message2=a, message3=b,
            message4=c, message5=d, message6=e, message7=response, message9=db_answer)


@APP.route("/contact")
def contact():
    return render_template("contact.html", disabled=True)


if __name__ == '__main__':
    APP.run(debug=True)
