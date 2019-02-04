# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
#print(data)

data.rename(columns={'Total':'Total_Medals'}, inplace=True)

data.head(10)


# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
#print(data)

data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])

better_event=data['Better_Event'].value_counts().idxmax()


# --------------
#Code starts here

top_countries=pd.DataFrame(data, columns=['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'])
print(top_countries)

top_countries.drop(top_countries.tail(1).index, inplace=True)

def top_ten(top_countries, values):
    country_list=values[0]
    for i in top_countries.columns:
        country_list=top_countries.nlargest(10, values)
    return country_list    

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

top_10_summer=top_10_summer['Country_Name'].tolist()
top_10_winter=top_10_winter['Country_Name'].tolist()
top_10=top_10['Country_Name'].tolist()

common=(set(top_10_summer)&set(top_10_winter)&set(top_10))
common=list(common)
print(common)




# --------------
#Code starts here

summer_df=data[data['Country_Name'].isin(top_10_summer)]
	
winter_df=data[data['Country_Name'].isin(top_10_winter)]
	
top_df=data[data['Country_Name'].isin(top_10)]


summer_df1=summer_df.groupby(['Country_Name','Total_Summer']).size().unstack()
summer_df1.plot(kind='bar',stacked=True)
	
winter_df1=winter_df.groupby(['Country_Name','Total_Summer']).size().unstack()
winter_df1.plot(kind='bar',stacked=True)
	
top_df1=top_df.groupby(['Country_Name','Total_Summer']).size().unstack()
top_df1.plot(kind='bar',stacked=True)

plt.xlabel('Country_Name')
	
plt.ylabel('Total_Summer')
plt.show()




# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=np.max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.groupby('Country_Name')['Golden_Ratio'].agg(np.max).idxmax()

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=np.max(winter_df['Golden_Ratio'])
winter_country_gold=winter_df.groupby('Country_Name')['Golden_Ratio'].agg(np.max).idxmax()

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=np.max(top_df['Golden_Ratio'])
top_country_gold=top_df.groupby('Country_Name')['Golden_Ratio'].agg(np.max).idxmax()



# --------------
#Code starts here
data.drop(data.tail(1).index, inplace=True)
data_1=pd.DataFrame(data)
	

data_1['Total_Points']=data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']

most_points=np.max(data_1['Total_Points'])

best_country=data_1.groupby('Country_Name')['Total_Points'].agg(np.max).idxmax()

print(best_country)



# --------------
#Code starts here

best=data.loc[data['Country_Name']=='United States']
	
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
	
best.plot(kind='bar',stacked=True)
	
plt.xlabel('United States')
	
plt.ylabel('Medals Tally')
	
plt.xticks(rotation=45)



