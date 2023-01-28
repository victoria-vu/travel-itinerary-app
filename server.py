"""Travel itinerary application Flask server.

Provides web interface for creating travel itinerary, opening a to-do-list, 
and adding locations to a map."""


from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
import os

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
# FOURSQUARE_KEY = os.environ["FOURSQUARE_KEY"]


@app.route("/")
def show_homepage():
    """Show the homepage."""

    if "user_userid" in session:
        return redirect("/dashboard")

    return render_template("homepage.html")


@app.route("/log-in")
def show_login_page():
    """Show user the log in page."""
    
    return render_template("log-in.html")


@app.route("/log-in", methods=["POST"])
def login():
    """Log in an existing user."""
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email=email)
    
    if not user:
        flash("The email you typed in does not exist. Please sign up for an account.")
        return redirect("/log-in")
    elif user.password != password:
        flash("Incorrect password. Please try again.")
        return redirect("/log-in")
    else:
        session["user_email"] = user.email
        session["user_fname"] = user.fname
        session["user_userid"] = user.user_id
        return redirect("/dashboard")
    
    
@app.route("/sign-up")
def show_signup_page():
    """Show user the sign up page."""

    return render_template("sign-up.html")


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
def show_dashboard():
    """Show user dashboard."""

    return render_template("dashboard.html", name=session["user_fname"], user_id=session["user_userid"])


@app.route("/create-itinerary")
def show_create_itinerary_page():
    """Show user the create an itinerary page."""

    return render_template("create-itinerary.html")


@app.route("/create-itinerary", methods=["POST"])
def user_itinerary():
    """Create an itinerary."""

    user = session["user_userid"]
    name = request.form.get("name")
    start_date = request.form.get("start-date")
    end_date = request.form.get("end-date")

    itinerary = crud.create_itinerary(user, name, start_date, end_date)
    db.session.add(itinerary)
    db.session.commit()

    return redirect("/customize-itinerary")


@app.route("/customize-itinerary")
def show_customize_itinerary_page():
    """Show user the customize an itinerary page."""

    return render_template("customize-itinerary.html")


@app.route("/view-itineraries")
def show_all_itineraries():
    """Show all exisiting itineraries of a particular user."""
    
    if "user_userid" in session:
        itineraries = crud.get_user_itineraries(session["user_userid"])
        return render_template("view-itineraries.html", itineraries=itineraries.itinerary_name)
    return redirect("/dashboard")


@app.route("/view-itinerary/<itinerary_id>")
def view_an_itinerary(itinerary_id):
    """Show one itinerary"""
    #Use a CRUD function to look up itinerary_id 
    #Use Jinja to show everything on the page 
    
    pass


@app.route("/log-out")
def logout_user():
    """Logs a user out."""

    if "user_userid" in session:
        session.pop("user_email")
        session.pop("user_fname")
        session.pop("user_userid")
    return redirect("/")




if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')


    