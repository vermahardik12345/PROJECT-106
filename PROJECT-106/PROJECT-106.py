import csv
import numpy as np
import plotly_express as px

def getDataSource(data_path):
    Marks= []
    DaysPresent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            DaysPresent.append(float(row["Days Present"]))

    return {"x" : Marks, "y":DaysPresent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Student Marks and  Days Presentis  :-  \n--->",correlation[0,1])
def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()
def setup():
    data_path  = "Marks.csv"
    
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)




setup()