#!/usr/bin/env python3
#server/seed.py

from app import app
from models import db, Pet
from faker import Faker
from random import choice as rc

with app.app_context():
        
    # Create and initialize a faker generator
    faker=Faker()

    # Delete all rows in the "pets" table
    Pet.query.delete()


    # Create an empty list
    pets = []
    species = ["Cat", "Dog", "Snake", "Turtle", "Bird", "Cow", "Chicken", "Hamster"]

    for n in range(10):
        pet=Pet(name=faker.first_name(), species=rc(species))
        pets.append(pet)

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()