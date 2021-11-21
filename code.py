import pandas as pd
import plotly.graph_objects as go
import csv 

df = pd.read_csv("data.csv")
student = df.loc[df["student_id"] == "TRL_xsl"]
print(student.groupby("level")["attempt"].mean())
graph = go.Figure(go.Bar(
    x = student.groupby("level")["attempt"].mean(),
    y = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = "h"
))
graph.show()
