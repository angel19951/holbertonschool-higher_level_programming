#!/usr/bin/python3
"""
Prints the State object with the name passed
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for item in session.query(State).filter(State.name == sys.argv[4])\
            .order_by(State.id):
        if item:
            print('{}'.format(item.id))
            found = 1
    if found != 1:
        print('Not found')
