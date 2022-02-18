from flask import Flask, request, jsonify, render_template
import pickle

from Model_ML.movie_recommender import MovieRecommender

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movie_recommender',methods=['POST'])
def movie_recommender():
    
    print('For rendering results on HTML GUI')
    
    movie_name = request.form['movie']
    how_many = int(request.form['how_many'])

    pmovie = MovieRecommender()
    response = pmovie.contents_based_recommender(movie_name, how_many)

    return render_template('index.html', prediction_text='Recommendations are  {}'.format(response))


if __name__ == "__main__":
    print("Starting Python Flask Server For Movie Recommendation Engine...")
    app.run(debug=True)

    