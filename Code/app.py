"""Main script, uses other modules to generate sentences."""
from flask import Flask
from histogram import dictogram
from sample import sample

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    hist = dictogram("fish.txt")
    return sample(hist)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
     
    return before_first_request()


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
