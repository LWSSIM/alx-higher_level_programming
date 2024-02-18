#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def change_state_name(un, ps, db):
    """Prints the ne states.id when success
    """
    engine = create_engine(f"mysql://{un}:{ps}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        new_name = "New Mexico"
        old_name = session.query(State).filter(State.id == 2).first()

        if old_name:
            old_name.name = new_name
        session.commit()

    except Exception as e:
        session.rollback()
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

    change_state_name(un, ps, db)
