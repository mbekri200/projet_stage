import pandas as pd
df1 = pd.read_csv('Emission2021.csv')
print(df1.head(10))
df2= pd.read_csv('shipstaticdata.csv')
df1['ImoNumber'] = pd.to_numeric(df1['ImoNumber'], errors='coerce')
df1['ImoNumber'] = df1['ImoNumber'].fillna(0)
df1['ImoNumber'] = df1['ImoNumber'].astype(int)
#df1['ImoNumber'] = df1['ImoNumber'].astype(int)
print(df1.dtypes)
df_merged= pd.merge(df1[['ImoNumber','CO₂ emissions per distance [kg CO₂ / n mile]']],df2[['ImoNumber','CallSign']],on='ImoNumber')
# Afficher le DataFrame mis à jour
#print("DataFrame mis à jour :")
print(df_merged)








#df1 = pd.read_csv('PositionReport2.csv')

"""df2= pd.read_csv('shipstaticdata.csv')
df1['ImoNumber'] = pd.to_numeric(df1['ImoNumber'], errors='coerce')
df1['ImoNumber'] = df1['ImoNumber'].fillna(0)
df1['ImoNumber'] = df1['ImoNumber'].astype(int)
#df1['ImoNumber'] = df1['ImoNumber'].astype(int)
print(df1.dtypes)
df_merged= pd.merge(df1[['ImoNumber','CO₂ emissions per distance [kg CO₂ / n mile]']],df2[['ImoNumber','CallSign']],on='ImoNumber')
# Afficher le DataFrame mis à jour
#print("DataFrame mis à jour :")
print(df_merged)

df1=pd.read_csv('shipstaticdata.csv')
df2=pd.read_csv('PositionReport2.csv')
exp=df1[['MMSI','ImoNumber','Destination']]
exp2=df2[['MMSI','Temps de reception','Sog','Cog','Longitude','Latitude']]
df_dyn=pd.merge(exp,exp2,on='MMSI')
#df_dyn.to_csv('datadyn.csv', index=False)

df_stat=df1[['ImoNumber','Name','MMSI','CallSign','Type of vessel','DimensionA','DimensionB','DimensionC','DimensionD']]
print(df_stat.head(10))
df_stat.to_csv('datastat.csv', index=False)"""
#print(df_dyn['Destination'].head(20))

#df1.head(10)

