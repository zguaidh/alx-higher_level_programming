#!/usr/bin/python3
"""Fetch the 1st state"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ), pool_pre_ping=True)

    '''Make a session'''
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State).first()

    if states is not None:
        print("{}: {}".format(states.id, states.name))
    else:
        print('Nothing')

    session.close()
