import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from preProcessing import preProcess
from matplotlib import pyplot as plt
import preProcessing
import plotly.plotly as py
import plotly.express as px

def runModel(df,n_clusters, n_init):
    # df = convertCategorialVariables(df)
    df = KMeansFunc(df,n_clusters, n_init)
    df = scatterGraph(df)
    df=makeHoroplethMap(df)
    print (df)
    return 0

def convertCategorialVariables(df):
    var_mod = list(df.columns.values)
    le = LabelEncoder()
    for i in var_mod:
      df[i] = le.fit_transform(df[i])
    return df;

def KMeansFunc(df,n_clusters,n_init):
    clustring = KMeans(n_clusters=n_clusters,n_init=n_init)
    a=clustring.fit(df)
    predict = clustring.predict(df)
    df['Clustering'] = pd.Series(predict, index=df.index)
    return df


def scatterGraph(df):
    Generosity = df['Generosity']
    social_support = df['Social support']
    clustering = df['Clustering']

    plt.scatter(social_support,Generosity,c=clustering, edgecolor='black', linewidth=1, alpha=0.75)

    plt.title('clustring')
    plt.xlabel('Generosity')
    plt.ylabel('social_support')

    plt.tight_layout()

    plt.show()

def makeHoroplethMap(df):
    API='Vn3DdeYNzJ9f44m9ykeb'
    USER_NAME='irisdrei'

    choromap = px.choropleth(df ,color="Bergeron",locations="district", featureidkey="properties.district", projection="mercator")
    choromap.update_geos(fitbounds="locations", visible=False)
    choromap.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    choromap.show()

    # py.sign_in(USER_NAME, API)
    # py.image.save_as(choromap, filename='name.png')

df = preProcessing.preProcess("C:\\Users\\iris dreizenshtok\\Desktop\\Dataset.xlsx")
runModel(df,3,2)