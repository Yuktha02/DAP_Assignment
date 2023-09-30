import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("TESLA.csv")
dataframe=pd.DataFrame(data)
dfh=dataframe.head(20)
dfh.plot(x="Date",y="High",kind="bar",title="stock price")
plt.show()