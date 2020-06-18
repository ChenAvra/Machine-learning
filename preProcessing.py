from tkinter import messagebox

import pandas as pd
import numpy as np



def readData(path):
    try:
        df = pd.read_excel(path)
        return df
    except:
        messagebox.showinfo("error","Invalid path, pleae enter a new path")

# df = df.to_csv("C:\\Users\\Chen\\Desktop\\Dataset.csv", index=None ,header=True)


def fillMissingValues(df):
    df_select = df.select_dtypes(include=np.number)
    #fill missing values -numeric
    for col in df_select.columns:
        df[col].fillna(df[col].mean(), inplace=True)
    return df

#Standardization

def Standardization(df):
    df_select = df.select_dtypes(include=np.number)

    for col in df_select.columns:
        if col != "year":
            mean = df[col].mean()
            std = df[col].std()
            df[col] = (df[col] - mean) / std
    return df


#group by and mean
def groupByCountry(df):
    df=df.groupby('country').mean()
    return df



def preProcess(path):
    df=readData(path)
    if df is not None:
        df = fillMissingValues(df)
        df=Standardization(df)
        df=groupByCountry(df)
        return df





