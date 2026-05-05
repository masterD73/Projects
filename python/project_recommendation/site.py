import os
import pickle
import sqlalchemy
from flask import Flask, request, render_template
import pandas as pd
from project_recommendation.kp import password
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost:3307/recommendation'
app = Flask(__name__)



def name_to_id(movie, movies):
    outcome = movies[movies.movie_title == movie]

    if len(outcome) == 0:
        return 1
    return outcome.movie_id.iloc[0]

print(os.getcwd())
@app.route('/', methods=['GET', 'POST'])
def index():
    with open('../models/data.pkl', 'rb') as pickle_file:
         model = pickle.load(pickle_file)
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{password}@localhost:3307/recommend')
        conn = engine.connect()
        name_id = name_to_id(movie_name, pd.read_sql('SELECT * FROM movies', conn))
        rating = round(pd.read_sql(f'SELECT AVG(rating) FROM ratings WHERE movie_id={name_id}', conn).iloc[0][0], 2)
        return render_template('index.html', movie_name=movie_name, rating=rating)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
