"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb itineraries")
os.system("createdb itineraries")

# Need to go through model to access the database, then create all tables
model.connect_to_db(server.app)
model.db.create_all()