import pandas as pd
import matplotlib.pyplot as plt
import math 

def labelPageViewsData(x):
    return int(math.log10(int(x)))

def labelEditCountsData(x):
    return int(int(x) / 50) + 1       

def multi(x):
    return int(x) * 5000

def processData(originFilePath, newFilePath):
    originData = pd.read_csv(originFilePath,index_col=0)
    originData['5000xEditCount'] = originData['Edit Counts'].apply(lambda x: multi(x))
    originData.plot.line(y=['Page Views','5000xEditCount'],title='positions', figsize=(15,5))
    plt.legend()
    plt.show()
    originData['Page Views'] = originData['Page Views'].apply(lambda x: labelPageViewsData(x))
    originData['Edit Counts'] = originData['Edit Counts'].apply(lambda x: labelEditCountsData(x))
    originData.plot.line(y=['Page Views','Edit Counts'],title='positions', figsize=(15,5))
    plt.legend()
    plt.show()
    originData.drop(['5000xEditCount'], axis=1, inplace=True)
    originData.to_csv(newFilePath)

if __name__ == "__main__":
    processData("Database/Database 2A.csv", "Database/r_2A.csv")