import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
fig = ff.create_distplot([data],["temp"],show_hist = False)
fig.show()