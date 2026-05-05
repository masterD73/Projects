import pickle
import sqlalchemy
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_ECHO'] = True


def name_to_id(movie, movies):
    outcome = movies[movies.movie_title == movie]

    if len(outcome) == 0:
        return 1
    return outcome.movie_id.iloc[0]


@app.route('/', methods=['GET', 'POST'])
def index():
    with open('/models/data.pkl', 'rb') as pickle_file:
        model = pickle.loads(pickle_file.read())
    print(model)
    if request.method == 'POST':
        age = int(request.form['age'])
        sex_mapping = {'male': 0, 'female': 1}
        sex = sex_mapping.get(request.form['sex'].lower())
        if sex is None:
            return render_template('index.html', error="Invalid input: Sex must be 'male' or 'female'.")
        if age is None:
            return render_template('index.html', error="Invalid input: Age must be a number.")

        engine = sqlalchemy.create_engine(f'mysql+pymysql://root:root@mysql/recommendation')
        conn = engine.connect()
        # name_id = name_to_id(movie_name, pd.read_sql('SELECT * FROM movies', conn))
        movie_id = model.predict([[age, sex]])[0]
        movie_title = pd.read_sql(f'SELECT movie_title FROM movies WHERE movie_id = {movie_id}', conn).iloc[0, 0]
        return render_template('index.html', movie_name=movie_title)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
