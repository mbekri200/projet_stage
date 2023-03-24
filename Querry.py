import sqlite3
import pandas as pd
df1=pd.read_csv('shipstaticdata.csv')
df2=pd.read_csv('PositionReport2.csv')
exp=df1[['MMSI','ImoNumber','Destination']]
exp2=df2[['MMSI','Temps de reception','Sog','Cog','Longitude','Latitude']]
print(df1['Destination'])
df_dyn=pd.merge(exp,exp2,on='MMSI')
print(df_dyn.head(10))
#df_dyn.to_csv('datadyn.csv', index=False)

"""df_stat=df1[['ImoNumber','Name','MMSI','CallSign','Type of vessel','DimensionA','DimensionB','DimensionC','DimensionD']]
print(df_stat.head(10))
df_stat.to_csv('datastat.csv', index=False)"""
#print(df_dyn['Destination'].head(20))

