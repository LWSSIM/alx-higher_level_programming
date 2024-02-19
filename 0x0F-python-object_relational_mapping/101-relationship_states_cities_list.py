#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
 contained in the database hbtn_0e_101_usa
"""


import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import Base, State


def list_all_objs(un, ps, db):
    """<state id>: <state name>
    <tabulation><city id>: <city name>
    """
    engine = create_engine(f"mysql://{un}:{ps}@localhost:3306/{db}")

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        query = (
            session.query(State).
            outerjoin(City).
            order_by(State.id, City.id).
            all()
        )

        for state in query:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")

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

    list_all_objs(un, ps, db)
