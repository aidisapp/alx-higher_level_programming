#!/usr/bin/python3
"""
Script that creates the State “California” with the
City “San Francisco” from the database
hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_user = argv[1]
    db_password = argv[2]
    db_name = argv[3]
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(db_user, db_password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
