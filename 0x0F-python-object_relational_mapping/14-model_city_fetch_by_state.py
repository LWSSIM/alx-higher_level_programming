#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


def print_all_cities(un, ps, db):
    """Prints (<state name>: (<city id>) <city name>)"""
    engine = create_engine(f"mysql://{un}:{ps}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        query = (
            session.query(State, City)
            .join(State, State.id == City.state_id)
            .all()
        )

        for state, city in query:
            print(f"{state.name}: ({city.id}) {city.name}")

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

    print_all_cities(un, ps, db)
