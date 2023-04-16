#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username,
                                   passwd,
                                   database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).order_by(State.id).all()
    for state in data:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
