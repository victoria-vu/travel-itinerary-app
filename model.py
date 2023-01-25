"""Models for travel itinerary app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    fname = db.Column(db.String)
    lname = db.Column(db.String)

    itinerary = db.relationship("Itinerary", back_populates="user")

    def __repr__(self):
        """Information on a user."""
        
        return f"<User user_id={self.user_id} email={self.email} fname={self.fname}>"


class Itinerary(db.Model):
    """An itinerary."""

    __tablename__ = "itineraries"

    itinerary_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    itinerary_name = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    user = db.relationship("User", back_populates="itinerary")
    todo = db.relationship("ToDo", back_populates="itinerary")
    map = db.relationship("Map", back_populates="itinerary")
    planner = db.relationship("Planner", back_populates="itinerary")

    def __repr__(self):
        """Information on an itinerary."""

        return f"<Itinerary itinerary_id={self.itinerary_id} itinerary_name={self.itinerary_name}>"


class Planner(db.Model):
    """A travel itinerary planner."""
   
    __tablename__ = "planners"

    planner_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    itinerary_id = db.Column(db.Integer, db.ForeignKey("itineraries.itinerary_id"))
    planner_name = db.Column(db.String)

    itinerary = db.relationship("Itinerary", back_populates="planner")
    entry = db.relationship("Entry", back_populates="planner")

    def __repr__(self):
        """Information on a planner in an itinerary."""

        return f"<Planner planner_id={self.planner_id} planner_name={self.planner_name}>"


class Entry(db.Model):
    """An entry in an itinerary planner."""

    __tablename__ = "entries"

    entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    planner_id = db.Column(db.Integer, db.ForeignKey("planners.planner_id"))
    activity_name = db.Column(db.String)
    activity_date = db.Column(db.Date)
    activity_location = db.Column(db.String)
    activity_time = db.Column(db.String)
    activity_description = db.Column(db.String)

    planner = db.relationship("Planner", back_populates="entry")

    def __repr__(self):
        """Information on an entry in a planner."""

        return f"<Entry entry_id={self.entry_id} activity_name={self.activity_name}>"


class ToDo(db.Model):
    """A to-do list in an itinerary."""

    __tablename__ = "todos"

    todo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    itinerary_id = db.Column(db.Integer, db.ForeignKey("itineraries.itinerary_id"))
    list_name = db.Column(db.String)

    itinerary = db.relationship("Itinerary", back_populates="todo")
    task = db.relationship("Task", back_populates="todo")

    def __repr__(self):
        """Information on a to-do list."""

        return f"<ToDo todo_id={self.todo_id} list_name={self.list_name}>"


class Task(db.Model):
    """A task in a to-do list."""

    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    todo_id = db.Column(db.Integer, db.ForeignKey("todos.todo_id"))
    task = db.Column(db.String)

    todo = db.relationship("ToDo", back_populates="task")

    def __repr__(self):
        """Information on a task."""

        return f"<Task task_id={self.task_id} task={self.task}>"


class Map(db.Model):
    """A map in an itinerary."""

    __tablename__ = "maps"

    map_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    itinerary_id = db.Column(db.Integer, db.ForeignKey("itineraries.itinerary_id"))
    map_name = db.Column(db.String)
    map_description = db.Column(db.Text)

    itinerary = db.relationship("Itinerary", back_populates="map")
    location = db.relationship("Location", back_populates="map")

    def __repr__(self):
        """Information on a map in an itinerary."""

        return f"<Map map_id={self.map_id} map_name={self.map_name}>"


class Location(db.Model):
    """A location on a map."""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    location_name = db.Column(db.String)
    map_id = db.Column(db.Integer, db.ForeignKey("maps.map_id"))

    map = db.relationship("Map", back_populates="location")

    def __repr__(self):
        """Information on a location on a map."""

        return f"<Location location_id={self.location_id} location_name={self.location_name}"
   
    
def connect_to_db(flask_app, db_uri="postgresql:///itineraries", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)