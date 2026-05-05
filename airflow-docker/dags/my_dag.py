# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------

from random import randint
from airflow.operators.bash import BashOperator
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
import pandas as pd
import numpy as np
import pickle
import sqlalchemy


def _training_model():
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import KFold
    from sklearn.model_selection import GridSearchCV
    from sklearn.model_selection import train_test_split
    sql_db_url = "mysql+mysqlconnector://root:root@mysql"
    engine = sqlalchemy.create_engine(sql_db_url)
    with engine.connect() as conn:
        movies = pd.read_sql_table('movies', conn, schema='recommendation')
        ratings = pd.read_sql_table('ratings', conn, schema='recommendation')
        users = pd.read_sql_table('users', conn, schema='recommendation')

    users.replace({'M': 0, 'F': 1}, inplace=True)
    df = ratings.merge(users, on='user_id').merge(movies, on='movie_id')
    df.drop(['zip', 'imdb_url', 'occupation', 'timestamp', 'release_date', 'user_id'], axis=1, inplace=True)
    # scaler = StandardScaler()
    # df.age = scaler.fit_transform(df[['age']])
    knn = KNeighborsClassifier()
    # kf = KFold(n_splits=5, shuffle=True, random_state=42)
    data = df.drop(['rating', 'movie_title'], axis=1)
    knn.fit(data[["age", "gender"]], df['movie_id'])
    # gs = GridSearchCV(knn, {'n_neighbors': list(range(2, 10))}, cv=kf)
    # gs.fit(data, df['rating'])
    # knn.set_params(**gs.best_params_)
    # knn.fit(data, df['rating'])
    with open('/opt/airflow/models/data.pkl', 'wb') as f:
        pickle.dump(knn, f)


# def _choose_best_model(ti):
#     model = ti.xcom_pull(task_ids='trained_model')
#     best_accuracy = max(accuracies)
#     if best_accuracy > 8:
#         return 'accurate'
#     else:
#         return 'inaccurate'


with DAG('my_dag', start_date=datetime(2021, 1, 1),
         schedule="@daily", catchup=False) as dag:
    # training_model_a = PythonOperator(
    #     task_id='training_model_a',
    #     python_callable=_training_model)
    #
    # training_model_b = PythonOperator(
    #     task_id='training_model_b',
    #     python_callable=_training_model)
    #
    # training_model_c = PythonOperator(
    #     task_id='training_model_c',
    #     python_callable=_training_model)
    # choose_best_model = BranchPythonOperator(
    #     task_id='choose_best_model',
    #     python_callable=_choose_best_model)
    # accurate = BashOperator(
    #     task_id='accurate',
    #     bash_command='echo "accurate"')
    # inaccurate = BashOperator(
    #     task_id='inaccurate',
    #     bash_command='echo "inaccurate"')

    install_dependencies = BashOperator(
        task_id='install_dependencies',
        bash_command='pip install scikit-learn'
    )

    trained_model = PythonOperator(
        task_id='trained_model',
        python_callable=_training_model
    )
    install_dependencies >> trained_model
