#!/usr/bin/python3
"""
List all states with SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.session import Session
from model_state import Base
from model_state import State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    item = session.query(State).order_by(State.id).first()
    if item:
        print('{}: {}'.format(item.id, item.name))
    else:
        print('Nothing')
