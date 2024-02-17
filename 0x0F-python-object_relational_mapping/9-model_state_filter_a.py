#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
 from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_regx_state(un, ps, db):
    engine = create_engine(f"mysql://{un}:{ps}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        states = (
            session.query(State).
            filter(State.name.like("%a%")).
            order_by(State.id).all()
        )

        for state in states:
            print(f"{state.id}: {state.name}")

    except Exception as e:
        print(e)

    finally:
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    un = sys.argv[1]
    ps = sys.argv[2]
    db = sys.argv[3]

    list_regx_state(un, ps, db)
