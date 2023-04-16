#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database hbtn_0e_6_usa
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
    data = session.query(State).all()
    found = False
    for state in data:
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if found is False:
        print("Not found")
