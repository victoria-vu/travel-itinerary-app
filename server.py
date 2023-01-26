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

    return render_template("homepage.html")


@app.route("/log-in")
def show_login_page():
    """Shows user the log in page."""
    
    return render_template("log_in.html")


# @app.route("/log-in", methods=["POST"])
# def login_existing_user():
#     """Log in an existing user."""

#     email = request.form.get("email")
#     password = request.form.get("password")

#     # If email and password match, login_user returns the user's first name.
#     # Store the first name in the session.
#     fname = crud.login_user(email, password)
    
#     if fname:
#         session["name"] = fname
#         flash("You are successfully logged in.")
#     else:
#         flash("The email you typed in does not exist. Please sign up for an account.")

#     return redirect("/")

@app.route("/log-in", methods=["POST"])
def login():
    """Login user"""
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email=email)
    
    if not user:
        flash("The email you typed in does not exist. Please sign up for an account.")
    elif user.password != password:
        flash("Incorrect password. Please try again.")
    else:
        session["user_email"] = user.fname
    
    return redirect("/dashboard")


# "user" key = user object
# session["user"] = user

    
@app.route("/sign-up")
def show_signup_page():
    """Shows user the sign up page."""

    return render_template("create_account.html")


@app.route("/sign-up", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")

    user = crud.get_user_by_email(email)
    
    if user is not None:
        flash("An account already exists with that email. Please try another one.")
        return redirect("/sign-up")
    else:
        user = crud.create_user(email, password, fname, lname)
        db.session.add(user)
        db.session.commit()
        flash("Account has been created successfully. Please log in.")
        return redirect("/log-in")
    
    
@app.route("/dashboard")
def display_user_dashboard():
    """Displays user dashboard."""

    return render_template("user_dashboard.html", name=session["user_email"])


@app.route("/create-itinerary")
def show_create_itinerary_page():
    """Shows user the create an itinerary page."""

    return render_template("create_itinerary.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')


    