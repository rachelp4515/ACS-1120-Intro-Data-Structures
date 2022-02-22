"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from histogram import dictogram, read_file
from sample import sample
from listogram import Listogram
from dictogram import Dictogram
from markov import dict_of_histograms_generator, tweet_generator

# file = 'fish.txt'

app = Flask(__name__)


word_list = read_file('fish.txt')

@app.before_first_request
def before_first_request():
  """Runs only once at Flask startup"""
  # TODO: Initialize your histogram, hash table, or markov chain here.
  histogram = Dictogram(word_list=word_list)
  return histogram

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
     
    histogram = Dictogram(word_list=word_list.split(" "))
    chosen_word = histogram.sample()
    print(histogram, "   here   ")

    markov_chain = dict_of_histograms_generator(word_list.split(" "))
    tweet = tweet_generator(markov_chain)
    # chosen_word = sample(histogram)
    """Route that returns a web page containing the generated text."""
    return render_template('index.html', chosen_word=chosen_word, histogram=histogram, tweet=tweet)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
