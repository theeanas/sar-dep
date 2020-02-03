import csv
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_set import Base, Leader, User

out = open("groups.csv", "rt", encoding="utf-8")
data = csv.reader(out)
data = [row for row in data]
out.close()


engine = create_engine('sqlite:///sarah.db?check_same_thread=False')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# leaders = ["عبدالرحمن سعيد الغامدي","عبدالرحمن الجهني","خالد الزهراني",
#            "عبدالعزيز إسماعيل","عبدالرحيم بيمه","عبدالله العمودي",
#            "منصور بن عبادي","مهند الأحمدي","سامي خجا","مهند الزهراني"]


#Now, the rest ..
#leads = session.query(Leader).all()
# ss = "Name: {}, Que:{}, Ans:{}, id: {}, done: {}, time: {}, uans: {}\n"
# for user in users:
#     print (ss.format(user.name, user.question, user.answer, user.id, user.done, user.timestamp, user.useranswer))

#users = session.query(User).all()

# for d in data:
#     hname, que, ans = d[:3]
#     leader_id = int(d[-1])
#     leader = session.query(Leader).filter_by(id = leader_id).one()
#     user = User(name=hname, leader=leader, question=que, answer=ans, useranswer='NY')
#     session.add(user)

# session.commit()
# print("Cool!")
