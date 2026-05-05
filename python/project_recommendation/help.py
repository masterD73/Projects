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
import os
import streamlit
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import airflow


def type_name(element):
    return str(type(element)).split("'")[1].strip("'")


def fix_col_names(df):
    df.rename(columns=lambda x: x.strip(), inplace=True)
    df.rename(columns=lambda x: x.replace(" ", "_"), inplace=True)
    df.rename(columns=lambda x: x.lower(), inplace=True)
    return df.copy()


def df_types_table(df):
    types_d = {}
    length = len(df)
    df.reset_index(inplace=True, drop=True)
    df_types = pd.DataFrame(index=df.columns, columns=["column_type", "data_type"])
    for col in df.columns:
        types_d[col] = set()
        for i in range(length):
            if df.loc[i, col] is np.nan or str(df.loc[i, col]) == 'nan':
                types_d[col].add(np.nan)
            else:
                types_d[col].add(type_name(df.loc[i, col]))
        df_types.loc[col].column_type = df[col].dtype
        df_types.loc[col].data_type = types_d[col]
    return df_types


def nan_ratio(df):
    return df.isnull().sum().sum() / len(df)


def plot_nas(df: pd.DataFrame):
    if df.isnull().sum().sum() != 0:
        na_df = (df.isnull().sum() / len(df)) * 100
        na_df = na_df.drop(na_df[na_df == 0].index).sort_values(ascending=False)
        missing_data = pd.DataFrame({'Missing Ratio %': na_df})
        missing_data.plot(kind="barh")
        plt.show()
        return na_df
    else:
        print('No NAs found')


def remove_nans(df, rate=2.5, inplace=True):
    for i in df.index:
        if df[i] < rate:
            df.dropna(subset=[i], inplace=inplace)
    return df


def main():
    pass


if __name__ == '__main__':
    main()
