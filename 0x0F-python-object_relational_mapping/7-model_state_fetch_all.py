#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa

Your script should take 3 arguments:
 mysql username, mysql password and database name
You must use the module SQLAlchemy
from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


def list_all_states(username, password, database):
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{database}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        states = session.query(State).order_by(State.id).all()

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

    list_all_states(un, ps, db)
