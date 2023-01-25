"""CRUD operations."""

from model import db, User, Itinerary, Planner, Entry, ToDo, Task, Map, Location, connect_to_db

# Create = Create new data
# Read = Retrieve data the already exits
# Update = Updating data
# Delete = Deleting data

# Functions that CREATE data
def create_user(email, password, fname, lname):
    """Create and return a new user."""
    
    user = User(email=email, password=password, fname=fname, lname=lname)

    return user    


def create_itinerary(name, start_date, end_date):
    """Create and return a new itinerary."""
    
    itinerary = Itinerary(itinerary_name=name, start_date=start_date, end_date=end_date)

    return itinerary


def create_planner(name):
    """Create a planner within an itinerary."""
    
    planner = Planner(planner_name=name)

    return planner


def create_entry(name, date, location, time, description):
    """Create an entry in a planner."""

    entry = Entry(activity_name=name, 
                    activity_date=date, 
                    activity_location=location,
                    activity_time=time,
                    activity_description=description)

    return entry


def create_todolist(list_name):
    """Create and return a new to-do list."""
    
    todo_list = ToDo(list_name=list_name)

    return todo_list


def create_task(task):
    """Create and return a task in a to-do list."""

    task = Task(task=task)

    return task


def create_map(name, description):
    """Create and return a new map."""
    
    map = Map(map_name=name, map_description=description)

    return map


def create_location():
    """Create and return a location on a map."""
    pass


if __name__ == '__main__':
    from server import app
    connect_to_db(app)