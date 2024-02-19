#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
 from the database hbtn_0e_100_usa
"""


import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import Base, State


def create_state_city(un, ps, db):
    """new state:city"""
    engine = create_engine(f"mysql://{un}:{ps}@localhost:3306/{db}")

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = State(name="California")
        session.add(state)

        city = City(name="San Francisco", state=state)
        session.add(city)

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

    create_state_city(un, ps, db)
