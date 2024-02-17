#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_first_obj(un, ps, db):
    engine = create_engine(f"mysql://{un}:{ps}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).first()

        if not state:
            print("Nothing")
        else:
            print(f"{state.id}: {state.name}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    un = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]

    list_first_obj(un, ps, db)
