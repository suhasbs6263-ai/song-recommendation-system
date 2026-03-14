from flask import Flask, render_template, request
import pandas as pd
from model import recommend

app = Flask(__name__)

data = pd.read_csv("Spotify_Youtube.csv")

@app.route('/')
def home():
    songs = list(data['Track'].head(500))
    return render_template("index.html", songs=songs)

@app.route('/recommend', methods=['POST'])
def get_recommendation():

    song = request.form['song']

    recommendations = recommend(song)

    songs = list(data['Track'].head(500))

    return render_template("index.html", songs=songs, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)