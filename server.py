"""Travel itinerary application Flask server.

Provides web interface for creating travel itinerary, opening a to-do-list, 
and adding locations to a map."""


from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"

# If you refer to undefined variable in a Jinja template, Jinja will ignore it.
# We need to set an attribute of the Jinja environment that says to make this an error.
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/log-in")
def log_in():
    """Show user log-in page."""
    
    return render_template("log_in.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')