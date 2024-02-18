#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
 from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_regx_state(un, ps, db, key):
    engine = create_engine(f"mysql://{un}:{ps}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        states = (
            session.query(State).
            filter(State.name.like(key)).
            first()
        )

        if states:
            print(states.id)
        else:
            print("Not found")

    except Exception as e:
        print(e)

    finally:
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <key>")
        sys.exit(1)

    un = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]
    key = sys.argv[4]

    list_regx_state(un, ps, db, key)
