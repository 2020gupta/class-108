import pandas as pd
import csv
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
height=df["height"].tolist()
weight=df["weight"].tolist()
graph=ff.create_distplot([height],["height"],show_hist=False)
graph1=ff.create_distplot([weight],["weight"],show_hist=False)
graph1.show()