import numpy as np
import pandas as pd
#import 311_Service_Requests_2020.csv
file = '311_Service_Requests_2020.csv'
df = pd.read_csv(file)
#choose zip code 10025
df = df[df["Incident Zip"] == 10025]
#find top10 incident types
total_incidents = df.groupby("Complaint Type")['Unique Key'].count()
top10 = total_incidents.sort_values(ascending = False)[:10]
top10