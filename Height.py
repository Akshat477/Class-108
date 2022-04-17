import pandas as pd
import csv
import plotly.figure_factory as ff
df =  pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()
fig = ff.create_distplot([data],["Height"],show_hist=False)
fig.show()
