{
 "cells": [
  {
   "cell_type": "code",
   "id": "initial_id",
   "metadata": {
    "collapsed": true,
    "ExecuteTime": {
     "end_time": "2025-01-29T14:54:06.650315Z",
     "start_time": "2025-01-29T14:54:00.761223Z"
    }
   },
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.pipeline import make_pipeline\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import RandomizedSearchCV\n",
    "\n",
    "train = pd.read_csv('train.csv')\n",
    "test = pd.read_csv('test.csv')\n",
    "target = train.target"
   ],
   "outputs": [],
   "execution_count": 1
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-01-29T14:54:07.614600Z",
     "start_time": "2025-01-29T14:54:07.573293Z"
    }
   },
   "cell_type": "code",
   "source": "train.info()",
   "id": "ff44d699e0a44569",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 595212 entries, 0 to 595211\n",
      "Data columns (total 57 columns):\n",
      " #   Column          Non-Null Count   Dtype  \n",
      "---  ------          --------------   -----  \n",
      " 0   ps_ind_01       595212 non-null  int64  \n",
      " 1   ps_ind_02_cat   595212 non-null  int64  \n",
      " 2   ps_ind_03       595212 non-null  int64  \n",
      " 3   ps_ind_04_cat   595212 non-null  int64  \n",
      " 4   ps_ind_05_cat   595212 non-null  int64  \n",
      " 5   ps_ind_06_bin   595212 non-null  int64  \n",
      " 6   ps_ind_07_bin   595212 non-null  int64  \n",
      " 7   ps_ind_08_bin   595212 non-null  int64  \n",
      " 8   ps_ind_09_bin   595212 non-null  int64  \n",
      " 9   ps_ind_10_bin   595212 non-null  int64  \n",
      " 10  ps_ind_11_bin   595212 non-null  int64  \n",
      " 11  ps_ind_12_bin   595212 non-null  int64  \n",
      " 12  ps_ind_13_bin   595212 non-null  int64  \n",
      " 13  ps_ind_14       595212 non-null  int64  \n",
      " 14  ps_ind_15       595212 non-null  int64  \n",
      " 15  ps_ind_16_bin   595212 non-null  int64  \n",
      " 16  ps_ind_17_bin   595212 non-null  int64  \n",
      " 17  ps_ind_18_bin   595212 non-null  int64  \n",
      " 18  ps_reg_01       595212 non-null  float64\n",
      " 19  ps_reg_02       595212 non-null  float64\n",
      " 20  ps_reg_03       595212 non-null  float64\n",
      " 21  ps_car_01_cat   595212 non-null  int64  \n",
      " 22  ps_car_02_cat   595212 non-null  int64  \n",
      " 23  ps_car_03_cat   595212 non-null  int64  \n",
      " 24  ps_car_04_cat   595212 non-null  int64  \n",
      " 25  ps_car_05_cat   595212 non-null  int64  \n",
      " 26  ps_car_06_cat   595212 non-null  int64  \n",
      " 27  ps_car_07_cat   595212 non-null  int64  \n",
      " 28  ps_car_08_cat   595212 non-null  int64  \n",
      " 29  ps_car_09_cat   595212 non-null  int64  \n",
      " 30  ps_car_10_cat   595212 non-null  int64  \n",
      " 31  ps_car_11_cat   595212 non-null  int64  \n",
      " 32  ps_car_11       595212 non-null  int64  \n",
      " 33  ps_car_12       595212 non-null  float64\n",
      " 34  ps_car_13       595212 non-null  float64\n",
      " 35  ps_car_14       595212 non-null  float64\n",
      " 36  ps_car_15       595212 non-null  float64\n",
      " 37  ps_calc_01      595212 non-null  float64\n",
      " 38  ps_calc_02      595212 non-null  float64\n",
      " 39  ps_calc_03      595212 non-null  float64\n",
      " 40  ps_calc_04      595212 non-null  int64  \n",
      " 41  ps_calc_05      595212 non-null  int64  \n",
      " 42  ps_calc_06      595212 non-null  int64  \n",
      " 43  ps_calc_07      595212 non-null  int64  \n",
      " 44  ps_calc_08      595212 non-null  int64  \n",
      " 45  ps_calc_09      595212 non-null  int64  \n",
      " 46  ps_calc_10      595212 non-null  int64  \n",
      " 47  ps_calc_11      595212 non-null  int64  \n",
      " 48  ps_calc_12      595212 non-null  int64  \n",
      " 49  ps_calc_13      595212 non-null  int64  \n",
      " 50  ps_calc_14      595212 non-null  int64  \n",
      " 51  ps_calc_15_bin  595212 non-null  int64  \n",
      " 52  ps_calc_16_bin  595212 non-null  int64  \n",
      " 53  ps_calc_17_bin  595212 non-null  int64  \n",
      " 54  ps_calc_18_bin  595212 non-null  int64  \n",
      " 55  ps_calc_19_bin  595212 non-null  int64  \n",
      " 56  ps_calc_20_bin  595212 non-null  int64  \n",
      "dtypes: float64(10), int64(47)\n",
      "memory usage: 258.8 MB\n"
     ]
    }
   ],
   "execution_count": 3
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-01-29T14:54:06.756923Z",
     "start_time": "2025-01-29T14:54:06.659837Z"
    }
   },
   "cell_type": "code",
   "source": [
    "train.drop('id', axis=1, inplace=True)\n",
    "train.drop('target', axis=1, inplace=True)\n",
    "train.head()"
   ],
   "id": "60aa5c5a3f7c28f5",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "   ps_ind_01  ps_ind_02_cat  ps_ind_03  ps_ind_04_cat  ps_ind_05_cat  \\\n",
       "0          2              2          5              1              0   \n",
       "1          1              1          7              0              0   \n",
       "2          5              4          9              1              0   \n",
       "3          0              1          2              0              0   \n",
       "4          0              2          0              1              0   \n",
       "\n",
       "   ps_ind_06_bin  ps_ind_07_bin  ps_ind_08_bin  ps_ind_09_bin  ps_ind_10_bin  \\\n",
       "0              0              1              0              0              0   \n",
       "1              0              0              1              0              0   \n",
       "2              0              0              1              0              0   \n",
       "3              1              0              0              0              0   \n",
       "4              1              0              0              0              0   \n",
       "\n",
       "   ...  ps_calc_11  ps_calc_12  ps_calc_13  ps_calc_14  ps_calc_15_bin  \\\n",
       "0  ...           9           1           5           8               0   \n",
       "1  ...           3           1           1           9               0   \n",
       "2  ...           4           2           7           7               0   \n",
       "3  ...           2           2           4           9               0   \n",
       "4  ...           3           1           1           3               0   \n",
       "\n",
       "   ps_calc_16_bin  ps_calc_17_bin  ps_calc_18_bin  ps_calc_19_bin  \\\n",
       "0               1               1               0               0   \n",
       "1               1               1               0               1   \n",
       "2               1               1               0               1   \n",
       "3               0               0               0               0   \n",
       "4               0               0               1               1   \n",
       "\n",
       "   ps_calc_20_bin  \n",
       "0               1  \n",
       "1               0  \n",
       "2               0  \n",
       "3               0  \n",
       "4               0  \n",
       "\n",
       "[5 rows x 57 columns]"
      ],
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ps_ind_01</th>\n",
       "      <th>ps_ind_02_cat</th>\n",
       "      <th>ps_ind_03</th>\n",
       "      <th>ps_ind_04_cat</th>\n",
       "      <th>ps_ind_05_cat</th>\n",
       "      <th>ps_ind_06_bin</th>\n",
       "      <th>ps_ind_07_bin</th>\n",
       "      <th>ps_ind_08_bin</th>\n",
       "      <th>ps_ind_09_bin</th>\n",
       "      <th>ps_ind_10_bin</th>\n",
       "      <th>...</th>\n",
       "      <th>ps_calc_11</th>\n",
       "      <th>ps_calc_12</th>\n",
       "      <th>ps_calc_13</th>\n",
       "      <th>ps_calc_14</th>\n",
       "      <th>ps_calc_15_bin</th>\n",
       "      <th>ps_calc_16_bin</th>\n",
       "      <th>ps_calc_17_bin</th>\n",
       "      <th>ps_calc_18_bin</th>\n",
       "      <th>ps_calc_19_bin</th>\n",
       "      <th>ps_calc_20_bin</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>8</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 57 columns</p>\n",
       "</div>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 2
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-01-29T14:54:08.060562Z",
     "start_time": "2025-01-29T14:54:07.659200Z"
    }
   },
   "cell_type": "code",
   "source": [
    "import numpy as np\n",
    "scaled_train = StandardScaler().fit_transform(train)"
   ],
   "id": "6cb9fed4b355796f",
   "outputs": [],
   "execution_count": 4
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-01-29T15:20:23.176315Z",
     "start_time": "2025-01-29T15:13:04.968754Z"
    }
   },
   "cell_type": "code",
   "source": [
    "from sklearn.decomposition import PCA\n",
    "from sklearn.cluster import dbscan\n",
    "pca = PCA(random_state=42, n_components=0.95, svd_solver='full')\n",
    "df_reduced = pca.fit_transform(np.array(scaled_train))\n",
    "\n",
    "dbscan_model = dbscan(df_reduced, eps=0.2, min_samples=10, n_jobs=-1)"
   ],
   "id": "8f57d1f1c5557502",
   "outputs": [],
   "execution_count": 19
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-01-29T15:06:45.092988Z",
     "start_time": "2025-01-29T15:06:33.531332Z"
    }
   },
   "cell_type": "code",
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.model_selection import RandomizedSearchCV\n",
    "from sklearn.pipeline import make_pipeline\n",
    "clf = make_pipeline(StandardScaler(), PCA(random_state=42),\n",
    "RandomForestClassifier(random_state=42))\n",
    "param_distrib = {\"randomforestclassifier__n_estimators\": np.arange(300, 501, 100),\n",
    "                 \"dbscan__eps\": np.arange(0.05, 0.21, 0.05), \"dbscan__min_samples\": np.arange(10, 100, 10)}\n",
    "rnd_search = RandomizedSearchCV(clf, param_distrib, n_iter=10, cv=3, random_state=42, n_jobs=-1)\n",
    "rnd_search.fit(train, target)"
   ],
   "id": "3d28659c4c52f1fa",
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Invalid parameter 'dbscan' for estimator Pipeline(steps=[('standardscaler', StandardScaler()),\n                ('pca', PCA(random_state=42)),\n                ('randomforestclassifier',\n                 RandomForestClassifier(random_state=42))]). Valid parameters are: ['memory', 'steps', 'transform_input', 'verbose'].",
     "output_type": "error",
     "traceback": [
      "\u001B[1;31m---------------------------------------------------------------------------\u001B[0m",
      "\u001B[1;31m_RemoteTraceback\u001B[0m                          Traceback (most recent call last)",
      "\u001B[1;31m_RemoteTraceback\u001B[0m: \n\"\"\"\nTraceback (most recent call last):\n  File \"C:\\Users\\merda\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\joblib\\externals\\loky\\process_executor.py\", line 463, in _process_worker\n    r = call_item()\n        ^^^^^^^^^^^\n  File \"C:\\Users\\merda\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\joblib\\externals\\loky\\process_executor.py\", line 291, in __call__\n    return self.fn(*self.args, **self.kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Users\\merda\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\joblib\\parallel.py\", line 598, in __call__\n    return [func(*args, **kwargs)\n            ^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Users\\merda\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\sklearn\\utils\\parallel.py\", line 139, in __call__\n    return self.function(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Users\\merda\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\sklearn\\model_selection\\_validation.py\", line 854, in _fit_and_score\n    estimator = estimator.set_params(**clone(parameters, safe=False))\n                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"C:\\Users\\merda\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\sklearn\\pipeline.py\", line 320, in set_params\n    self._set_params(\"steps\", **kwargs)\n  File \"C:\\Users\\merda\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\sklearn\\utils\\metaestimators.py\", line 69, in _set_params\n    super().set_params(**params)\n  File \"C:\\Users\\merda\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\sklearn\\base.py\", line 283, in set_params\n    raise ValueError(\nValueError: Invalid parameter 'dbscan' for estimator Pipeline(steps=[('standardscaler', StandardScaler()),\n                ('pca', PCA(random_state=42)),\n                ('randomforestclassifier',\n                 RandomForestClassifier(random_state=42))]). Valid parameters are: ['memory', 'steps', 'transform_input', 'verbose'].\n\"\"\"",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001B[1;31mValueError\u001B[0m                                Traceback (most recent call last)",
      "Cell \u001B[1;32mIn[18], line 9\u001B[0m\n\u001B[0;32m      6\u001B[0m param_distrib \u001B[38;5;241m=\u001B[39m {\u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mrandomforestclassifier__n_estimators\u001B[39m\u001B[38;5;124m\"\u001B[39m: np\u001B[38;5;241m.\u001B[39marange(\u001B[38;5;241m300\u001B[39m, \u001B[38;5;241m501\u001B[39m, \u001B[38;5;241m100\u001B[39m),\n\u001B[0;32m      7\u001B[0m                  \u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mdbscan__eps\u001B[39m\u001B[38;5;124m\"\u001B[39m: np\u001B[38;5;241m.\u001B[39marange(\u001B[38;5;241m0.05\u001B[39m, \u001B[38;5;241m0.21\u001B[39m, \u001B[38;5;241m0.05\u001B[39m), \u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mdbscan__min_samples\u001B[39m\u001B[38;5;124m\"\u001B[39m: np\u001B[38;5;241m.\u001B[39marange(\u001B[38;5;241m10\u001B[39m, \u001B[38;5;241m100\u001B[39m, \u001B[38;5;241m10\u001B[39m)}\n\u001B[0;32m      8\u001B[0m rnd_search \u001B[38;5;241m=\u001B[39m RandomizedSearchCV(clf, param_distrib, n_iter\u001B[38;5;241m=\u001B[39m\u001B[38;5;241m10\u001B[39m, cv\u001B[38;5;241m=\u001B[39m\u001B[38;5;241m3\u001B[39m, random_state\u001B[38;5;241m=\u001B[39m\u001B[38;5;241m42\u001B[39m, n_jobs\u001B[38;5;241m=\u001B[39m\u001B[38;5;241m-\u001B[39m\u001B[38;5;241m1\u001B[39m)\n\u001B[1;32m----> 9\u001B[0m \u001B[43mrnd_search\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mfit\u001B[49m\u001B[43m(\u001B[49m\u001B[43mtrain\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mtarget\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\sklearn\\base.py:1389\u001B[0m, in \u001B[0;36m_fit_context.<locals>.decorator.<locals>.wrapper\u001B[1;34m(estimator, *args, **kwargs)\u001B[0m\n\u001B[0;32m   1382\u001B[0m     estimator\u001B[38;5;241m.\u001B[39m_validate_params()\n\u001B[0;32m   1384\u001B[0m \u001B[38;5;28;01mwith\u001B[39;00m config_context(\n\u001B[0;32m   1385\u001B[0m     skip_parameter_validation\u001B[38;5;241m=\u001B[39m(\n\u001B[0;32m   1386\u001B[0m         prefer_skip_nested_validation \u001B[38;5;129;01mor\u001B[39;00m global_skip_validation\n\u001B[0;32m   1387\u001B[0m     )\n\u001B[0;32m   1388\u001B[0m ):\n\u001B[1;32m-> 1389\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[43mfit_method\u001B[49m\u001B[43m(\u001B[49m\u001B[43mestimator\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[43margs\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[43mkwargs\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\sklearn\\model_selection\\_search.py:1024\u001B[0m, in \u001B[0;36mBaseSearchCV.fit\u001B[1;34m(self, X, y, **params)\u001B[0m\n\u001B[0;32m   1018\u001B[0m     results \u001B[38;5;241m=\u001B[39m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_format_results(\n\u001B[0;32m   1019\u001B[0m         all_candidate_params, n_splits, all_out, all_more_results\n\u001B[0;32m   1020\u001B[0m     )\n\u001B[0;32m   1022\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m results\n\u001B[1;32m-> 1024\u001B[0m \u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43m_run_search\u001B[49m\u001B[43m(\u001B[49m\u001B[43mevaluate_candidates\u001B[49m\u001B[43m)\u001B[49m\n\u001B[0;32m   1026\u001B[0m \u001B[38;5;66;03m# multimetric is determined here because in the case of a callable\u001B[39;00m\n\u001B[0;32m   1027\u001B[0m \u001B[38;5;66;03m# self.scoring the return type is only known after calling\u001B[39;00m\n\u001B[0;32m   1028\u001B[0m first_test_score \u001B[38;5;241m=\u001B[39m all_out[\u001B[38;5;241m0\u001B[39m][\u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mtest_scores\u001B[39m\u001B[38;5;124m\"\u001B[39m]\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\sklearn\\model_selection\\_search.py:1951\u001B[0m, in \u001B[0;36mRandomizedSearchCV._run_search\u001B[1;34m(self, evaluate_candidates)\u001B[0m\n\u001B[0;32m   1949\u001B[0m \u001B[38;5;28;01mdef\u001B[39;00m\u001B[38;5;250m \u001B[39m\u001B[38;5;21m_run_search\u001B[39m(\u001B[38;5;28mself\u001B[39m, evaluate_candidates):\n\u001B[0;32m   1950\u001B[0m \u001B[38;5;250m    \u001B[39m\u001B[38;5;124;03m\"\"\"Search n_iter candidates from param_distributions\"\"\"\u001B[39;00m\n\u001B[1;32m-> 1951\u001B[0m     \u001B[43mevaluate_candidates\u001B[49m\u001B[43m(\u001B[49m\n\u001B[0;32m   1952\u001B[0m \u001B[43m        \u001B[49m\u001B[43mParameterSampler\u001B[49m\u001B[43m(\u001B[49m\n\u001B[0;32m   1953\u001B[0m \u001B[43m            \u001B[49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mparam_distributions\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mn_iter\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mrandom_state\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mrandom_state\u001B[49m\n\u001B[0;32m   1954\u001B[0m \u001B[43m        \u001B[49m\u001B[43m)\u001B[49m\n\u001B[0;32m   1955\u001B[0m \u001B[43m    \u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\sklearn\\model_selection\\_search.py:970\u001B[0m, in \u001B[0;36mBaseSearchCV.fit.<locals>.evaluate_candidates\u001B[1;34m(candidate_params, cv, more_results)\u001B[0m\n\u001B[0;32m    962\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39mverbose \u001B[38;5;241m>\u001B[39m \u001B[38;5;241m0\u001B[39m:\n\u001B[0;32m    963\u001B[0m     \u001B[38;5;28mprint\u001B[39m(\n\u001B[0;32m    964\u001B[0m         \u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mFitting \u001B[39m\u001B[38;5;132;01m{0}\u001B[39;00m\u001B[38;5;124m folds for each of \u001B[39m\u001B[38;5;132;01m{1}\u001B[39;00m\u001B[38;5;124m candidates,\u001B[39m\u001B[38;5;124m\"\u001B[39m\n\u001B[0;32m    965\u001B[0m         \u001B[38;5;124m\"\u001B[39m\u001B[38;5;124m totalling \u001B[39m\u001B[38;5;132;01m{2}\u001B[39;00m\u001B[38;5;124m fits\u001B[39m\u001B[38;5;124m\"\u001B[39m\u001B[38;5;241m.\u001B[39mformat(\n\u001B[0;32m    966\u001B[0m             n_splits, n_candidates, n_candidates \u001B[38;5;241m*\u001B[39m n_splits\n\u001B[0;32m    967\u001B[0m         )\n\u001B[0;32m    968\u001B[0m     )\n\u001B[1;32m--> 970\u001B[0m out \u001B[38;5;241m=\u001B[39m \u001B[43mparallel\u001B[49m\u001B[43m(\u001B[49m\n\u001B[0;32m    971\u001B[0m \u001B[43m    \u001B[49m\u001B[43mdelayed\u001B[49m\u001B[43m(\u001B[49m\u001B[43m_fit_and_score\u001B[49m\u001B[43m)\u001B[49m\u001B[43m(\u001B[49m\n\u001B[0;32m    972\u001B[0m \u001B[43m        \u001B[49m\u001B[43mclone\u001B[49m\u001B[43m(\u001B[49m\u001B[43mbase_estimator\u001B[49m\u001B[43m)\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    973\u001B[0m \u001B[43m        \u001B[49m\u001B[43mX\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    974\u001B[0m \u001B[43m        \u001B[49m\u001B[43my\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    975\u001B[0m \u001B[43m        \u001B[49m\u001B[43mtrain\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mtrain\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    976\u001B[0m \u001B[43m        \u001B[49m\u001B[43mtest\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mtest\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    977\u001B[0m \u001B[43m        \u001B[49m\u001B[43mparameters\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43mparameters\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    978\u001B[0m \u001B[43m        \u001B[49m\u001B[43msplit_progress\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43m(\u001B[49m\u001B[43msplit_idx\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mn_splits\u001B[49m\u001B[43m)\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    979\u001B[0m \u001B[43m        \u001B[49m\u001B[43mcandidate_progress\u001B[49m\u001B[38;5;241;43m=\u001B[39;49m\u001B[43m(\u001B[49m\u001B[43mcand_idx\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mn_candidates\u001B[49m\u001B[43m)\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    980\u001B[0m \u001B[43m        \u001B[49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[43mfit_and_score_kwargs\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    981\u001B[0m \u001B[43m    \u001B[49m\u001B[43m)\u001B[49m\n\u001B[0;32m    982\u001B[0m \u001B[43m    \u001B[49m\u001B[38;5;28;43;01mfor\u001B[39;49;00m\u001B[43m \u001B[49m\u001B[43m(\u001B[49m\u001B[43mcand_idx\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mparameters\u001B[49m\u001B[43m)\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43m(\u001B[49m\u001B[43msplit_idx\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43m(\u001B[49m\u001B[43mtrain\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43mtest\u001B[49m\u001B[43m)\u001B[49m\u001B[43m)\u001B[49m\u001B[43m \u001B[49m\u001B[38;5;129;43;01min\u001B[39;49;00m\u001B[43m \u001B[49m\u001B[43mproduct\u001B[49m\u001B[43m(\u001B[49m\n\u001B[0;32m    983\u001B[0m \u001B[43m        \u001B[49m\u001B[38;5;28;43menumerate\u001B[39;49m\u001B[43m(\u001B[49m\u001B[43mcandidate_params\u001B[49m\u001B[43m)\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    984\u001B[0m \u001B[43m        \u001B[49m\u001B[38;5;28;43menumerate\u001B[39;49m\u001B[43m(\u001B[49m\u001B[43mcv\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43msplit\u001B[49m\u001B[43m(\u001B[49m\u001B[43mX\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[43my\u001B[49m\u001B[43m,\u001B[49m\u001B[43m \u001B[49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[38;5;241;43m*\u001B[39;49m\u001B[43mrouted_params\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43msplitter\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43msplit\u001B[49m\u001B[43m)\u001B[49m\u001B[43m)\u001B[49m\u001B[43m,\u001B[49m\n\u001B[0;32m    985\u001B[0m \u001B[43m    \u001B[49m\u001B[43m)\u001B[49m\n\u001B[0;32m    986\u001B[0m \u001B[43m\u001B[49m\u001B[43m)\u001B[49m\n\u001B[0;32m    988\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m \u001B[38;5;28mlen\u001B[39m(out) \u001B[38;5;241m<\u001B[39m \u001B[38;5;241m1\u001B[39m:\n\u001B[0;32m    989\u001B[0m     \u001B[38;5;28;01mraise\u001B[39;00m \u001B[38;5;167;01mValueError\u001B[39;00m(\n\u001B[0;32m    990\u001B[0m         \u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mNo fits were performed. \u001B[39m\u001B[38;5;124m\"\u001B[39m\n\u001B[0;32m    991\u001B[0m         \u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mWas the CV iterator empty? \u001B[39m\u001B[38;5;124m\"\u001B[39m\n\u001B[0;32m    992\u001B[0m         \u001B[38;5;124m\"\u001B[39m\u001B[38;5;124mWere there no candidates?\u001B[39m\u001B[38;5;124m\"\u001B[39m\n\u001B[0;32m    993\u001B[0m     )\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\sklearn\\utils\\parallel.py:77\u001B[0m, in \u001B[0;36mParallel.__call__\u001B[1;34m(self, iterable)\u001B[0m\n\u001B[0;32m     72\u001B[0m config \u001B[38;5;241m=\u001B[39m get_config()\n\u001B[0;32m     73\u001B[0m iterable_with_config \u001B[38;5;241m=\u001B[39m (\n\u001B[0;32m     74\u001B[0m     (_with_config(delayed_func, config), args, kwargs)\n\u001B[0;32m     75\u001B[0m     \u001B[38;5;28;01mfor\u001B[39;00m delayed_func, args, kwargs \u001B[38;5;129;01min\u001B[39;00m iterable\n\u001B[0;32m     76\u001B[0m )\n\u001B[1;32m---> 77\u001B[0m \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28;43msuper\u001B[39;49m\u001B[43m(\u001B[49m\u001B[43m)\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[38;5;21;43m__call__\u001B[39;49m\u001B[43m(\u001B[49m\u001B[43miterable_with_config\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\joblib\\parallel.py:2007\u001B[0m, in \u001B[0;36mParallel.__call__\u001B[1;34m(self, iterable)\u001B[0m\n\u001B[0;32m   2001\u001B[0m \u001B[38;5;66;03m# The first item from the output is blank, but it makes the interpreter\u001B[39;00m\n\u001B[0;32m   2002\u001B[0m \u001B[38;5;66;03m# progress until it enters the Try/Except block of the generator and\u001B[39;00m\n\u001B[0;32m   2003\u001B[0m \u001B[38;5;66;03m# reaches the first `yield` statement. This starts the asynchronous\u001B[39;00m\n\u001B[0;32m   2004\u001B[0m \u001B[38;5;66;03m# dispatch of the tasks to the workers.\u001B[39;00m\n\u001B[0;32m   2005\u001B[0m \u001B[38;5;28mnext\u001B[39m(output)\n\u001B[1;32m-> 2007\u001B[0m \u001B[38;5;28;01mreturn\u001B[39;00m output \u001B[38;5;28;01mif\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39mreturn_generator \u001B[38;5;28;01melse\u001B[39;00m \u001B[38;5;28;43mlist\u001B[39;49m\u001B[43m(\u001B[49m\u001B[43moutput\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\joblib\\parallel.py:1650\u001B[0m, in \u001B[0;36mParallel._get_outputs\u001B[1;34m(self, iterator, pre_dispatch)\u001B[0m\n\u001B[0;32m   1647\u001B[0m     \u001B[38;5;28;01myield\u001B[39;00m\n\u001B[0;32m   1649\u001B[0m     \u001B[38;5;28;01mwith\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_backend\u001B[38;5;241m.\u001B[39mretrieval_context():\n\u001B[1;32m-> 1650\u001B[0m         \u001B[38;5;28;01myield from\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_retrieve()\n\u001B[0;32m   1652\u001B[0m \u001B[38;5;28;01mexcept\u001B[39;00m \u001B[38;5;167;01mGeneratorExit\u001B[39;00m:\n\u001B[0;32m   1653\u001B[0m     \u001B[38;5;66;03m# The generator has been garbage collected before being fully\u001B[39;00m\n\u001B[0;32m   1654\u001B[0m     \u001B[38;5;66;03m# consumed. This aborts the remaining tasks if possible and warn\u001B[39;00m\n\u001B[0;32m   1655\u001B[0m     \u001B[38;5;66;03m# the user if necessary.\u001B[39;00m\n\u001B[0;32m   1656\u001B[0m     \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_exception \u001B[38;5;241m=\u001B[39m \u001B[38;5;28;01mTrue\u001B[39;00m\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\joblib\\parallel.py:1754\u001B[0m, in \u001B[0;36mParallel._retrieve\u001B[1;34m(self)\u001B[0m\n\u001B[0;32m   1747\u001B[0m \u001B[38;5;28;01mwhile\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_wait_retrieval():\n\u001B[0;32m   1748\u001B[0m \n\u001B[0;32m   1749\u001B[0m     \u001B[38;5;66;03m# If the callback thread of a worker has signaled that its task\u001B[39;00m\n\u001B[0;32m   1750\u001B[0m     \u001B[38;5;66;03m# triggered an exception, or if the retrieval loop has raised an\u001B[39;00m\n\u001B[0;32m   1751\u001B[0m     \u001B[38;5;66;03m# exception (e.g. `GeneratorExit`), exit the loop and surface the\u001B[39;00m\n\u001B[0;32m   1752\u001B[0m     \u001B[38;5;66;03m# worker traceback.\u001B[39;00m\n\u001B[0;32m   1753\u001B[0m     \u001B[38;5;28;01mif\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_aborting:\n\u001B[1;32m-> 1754\u001B[0m         \u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43m_raise_error_fast\u001B[49m\u001B[43m(\u001B[49m\u001B[43m)\u001B[49m\n\u001B[0;32m   1755\u001B[0m         \u001B[38;5;28;01mbreak\u001B[39;00m\n\u001B[0;32m   1757\u001B[0m     \u001B[38;5;66;03m# If the next job is not ready for retrieval yet, we just wait for\u001B[39;00m\n\u001B[0;32m   1758\u001B[0m     \u001B[38;5;66;03m# async callbacks to progress.\u001B[39;00m\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\joblib\\parallel.py:1789\u001B[0m, in \u001B[0;36mParallel._raise_error_fast\u001B[1;34m(self)\u001B[0m\n\u001B[0;32m   1785\u001B[0m \u001B[38;5;66;03m# If this error job exists, immediately raise the error by\u001B[39;00m\n\u001B[0;32m   1786\u001B[0m \u001B[38;5;66;03m# calling get_result. This job might not exists if abort has been\u001B[39;00m\n\u001B[0;32m   1787\u001B[0m \u001B[38;5;66;03m# called directly or if the generator is gc'ed.\u001B[39;00m\n\u001B[0;32m   1788\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m error_job \u001B[38;5;129;01mis\u001B[39;00m \u001B[38;5;129;01mnot\u001B[39;00m \u001B[38;5;28;01mNone\u001B[39;00m:\n\u001B[1;32m-> 1789\u001B[0m     \u001B[43merror_job\u001B[49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mget_result\u001B[49m\u001B[43m(\u001B[49m\u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43mtimeout\u001B[49m\u001B[43m)\u001B[49m\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\joblib\\parallel.py:745\u001B[0m, in \u001B[0;36mBatchCompletionCallBack.get_result\u001B[1;34m(self, timeout)\u001B[0m\n\u001B[0;32m    739\u001B[0m backend \u001B[38;5;241m=\u001B[39m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39mparallel\u001B[38;5;241m.\u001B[39m_backend\n\u001B[0;32m    741\u001B[0m \u001B[38;5;28;01mif\u001B[39;00m backend\u001B[38;5;241m.\u001B[39msupports_retrieve_callback:\n\u001B[0;32m    742\u001B[0m     \u001B[38;5;66;03m# We assume that the result has already been retrieved by the\u001B[39;00m\n\u001B[0;32m    743\u001B[0m     \u001B[38;5;66;03m# callback thread, and is stored internally. It's just waiting to\u001B[39;00m\n\u001B[0;32m    744\u001B[0m     \u001B[38;5;66;03m# be returned.\u001B[39;00m\n\u001B[1;32m--> 745\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28;43mself\u001B[39;49m\u001B[38;5;241;43m.\u001B[39;49m\u001B[43m_return_or_raise\u001B[49m\u001B[43m(\u001B[49m\u001B[43m)\u001B[49m\n\u001B[0;32m    747\u001B[0m \u001B[38;5;66;03m# For other backends, the main thread needs to run the retrieval step.\u001B[39;00m\n\u001B[0;32m    748\u001B[0m \u001B[38;5;28;01mtry\u001B[39;00m:\n",
      "File \u001B[1;32m~\\PycharmProjects\\num_flip\\.venv\\Lib\\site-packages\\joblib\\parallel.py:763\u001B[0m, in \u001B[0;36mBatchCompletionCallBack._return_or_raise\u001B[1;34m(self)\u001B[0m\n\u001B[0;32m    761\u001B[0m \u001B[38;5;28;01mtry\u001B[39;00m:\n\u001B[0;32m    762\u001B[0m     \u001B[38;5;28;01mif\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39mstatus \u001B[38;5;241m==\u001B[39m TASK_ERROR:\n\u001B[1;32m--> 763\u001B[0m         \u001B[38;5;28;01mraise\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_result\n\u001B[0;32m    764\u001B[0m     \u001B[38;5;28;01mreturn\u001B[39;00m \u001B[38;5;28mself\u001B[39m\u001B[38;5;241m.\u001B[39m_result\n\u001B[0;32m    765\u001B[0m \u001B[38;5;28;01mfinally\u001B[39;00m:\n",
      "\u001B[1;31mValueError\u001B[0m: Invalid parameter 'dbscan' for estimator Pipeline(steps=[('standardscaler', StandardScaler()),\n                ('pca', PCA(random_state=42)),\n                ('randomforestclassifier',\n                 RandomForestClassifier(random_state=42))]). Valid parameters are: ['memory', 'steps', 'transform_input', 'verbose']."
     ]
    }
   ],
   "execution_count": 18
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-01-29T15:20:35.221372Z",
     "start_time": "2025-01-29T15:20:35.215373Z"
    }
   },
   "cell_type": "code",
   "source": "dbscan_model\n",
   "id": "ad3d3e375ed5027f",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([], dtype=int64), array([-1, -1, -1, ..., -1, -1, -1], shape=(595212,)))"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 22
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-01-29T15:02:27.129958Z",
     "start_time": "2025-01-29T15:02:27.123298Z"
    }
   },
   "cell_type": "code",
   "source": "np.unique(dbscan_model[1])",
   "id": "de91368e01b60875",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-1])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 16
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
