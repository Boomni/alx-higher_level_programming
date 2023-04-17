#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username,
                                  password,
                                  db_name),
                           pool_pre_ping=True)

    session = Session(engine)

    cities = session.query(State.name, City.id, City.name).\
        filter(State.id == City.state_id).\
        order_by(City.id)
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    session.close()
