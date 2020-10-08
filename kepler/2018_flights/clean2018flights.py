# %% import os
import os

try:
    os.chdir(os.path.join(os.getcwd(), 'kepler/2018_flights'))
    print(os.getcwd())
except:
    pass
# %% import all packages
import pandas as pd

# %% check the data, have a glance
flights = pd.read_csv('./data/Cleaned_2018_Flights.csv')
flights.head()

# %% check the aiport data

airport = pd.read_csv('./data/GlobalAirportDatabase.csv', names=['Airport ID',
                           'Name', 'City',
                           'Country', 'IATA',
                           'ICAO', 'Latitude',
                           'Longitude', 'Altitude',
                           'Timezone', 'DST',
                           'Tz database time zone', 'Type',
                           'Source'])
airport.head()
# airport.to_csv('./data/formatted_airports.csv')
# %% look up the origin lat/long take the merge and join with the right side

flights_full = flights.merge(airport[['IATA', 'Longitude', 'Latitude']], left_on='Origin', right_on='IATA')
flights_full.head()

# %% clean up the origin
flights_full['origin_lat'] = flights_full['Latitude']
flights_full['origin_long'] = flights_full['Longitude']
# now drop the lang/long columns
flights_full = flights_full.drop(['Latitude', 'Longitude', 'IATA'], axis=1)
flights_full.head()

# %% get the long/lat of dest and name it des-lat des-long
flights_full = flights_full.merge(airport[['IATA', 'Longitude', 'Latitude']], left_on='Dest', right_on='IATA')
flights_full.head()

# %% clean up by adding hte lat/long
flights_full['dest_lat'] = flights_full['Latitude']
flights_full['dest_long'] = flights_full['Longitude']
# now drop the lang/long columns
flights_full = flights_full.drop(['Latitude', 'Longitude', 'IATA'], axis=1)
flights_full.head()

# %% in order for kepler to read the data is the clean it down further shrink the data into quarters
s1 = flights_full[flights_full['Quarter'] == 1].sample(5000).index
s2 = flights_full[flights_full['Quarter'] == 2].sample(5000).index
s3 = flights_full[flights_full['Quarter'] == 3].sample(5000).index
s4 = flights_full[flights_full['Quarter'] == 4].sample(5000).index

flights_full.loc[s1.union(s2).union(s3).union(
    s4)].to_csv('./data/simplified_flights.csv')
# %%
