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
def show_homepage():
    """Shows the homepage."""

    # Code here: Need to write a code to define session user to pass to Jinja.

    return render_template("homepage.html")


@app.route("/log-in")
def show_login_page():
    """Shows user the log-in page."""
    
    return render_template("log_in.html")


@app.route("/sign-up")
def show_signup_page():
    """Shows user the sign-up page."""

    return render_template("create_account.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')