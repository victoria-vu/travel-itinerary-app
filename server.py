"""Travel itinerary application Flask server.

Provides web interface for creating travel itinerary, opening a to-do-list, 
and adding locations to a map."""


from flask import Flask, render_template, redirect, flash
import jinja2

app = Flask(__name__)
app.secret_key = "dev"

# If you refer to undefined variable in a Jinja template, Jinja will ignore it.
# We need to set an attribute of the Jinja environment that says to make this an error.
app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')