import datetime
from db_set import Base, Leader, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

engine = create_engine('sqlite:///sarah.db?check_same_thread=False')
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('initial.html')
    else:
        lid = int(request.form['answer'])
        leader = session.query(Leader).filter_by(id = lid).one()
        users = session.query(User).filter_by(leader_id = lid).all()
        for u in users:
            if u.done == False:
                return redirect(url_for('index', id = lid, name=u.name, que=u.question))

@app.route('/leader/<int:id>/<string:name>/<string:que>', methods=['GET', 'POST'])
def index(id, name, que):
    if request.method == 'GET':
        return render_template('index.html', user_n=name, user_q=que)
    else:
        ans = request.form['ans']
        leader = session.query(Leader).filter_by(id = id).one()
        users = session.query(User).filter_by(leader_id = id).all()
        num = 0
        for u in users:
            if u.done == False:
                u.useranswer = ans
                u.done = True
                break

    session.commit()
    return render_template('post.html')
    
def getApp():
    return app

if __name__ == '__main__':
    app.secret_key = 'super'
    app.debug = True
    app.run(host='localhost', port=8000)
