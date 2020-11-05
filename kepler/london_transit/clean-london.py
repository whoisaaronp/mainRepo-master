# %% read the csv
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'kepler/london_transit'))
    print(os.getcwd())
except:
    pass
# %% import pandas
import pandas as pd

# %% import all data
stops = pd.read_csv('./data/stops.csv')
trips = pd.read_csv('./data/trips.csv')
stop_times = pd.read_csv('./data/stop_times.csv')
print(stop_times)

# %% merge the stops into the stop time
full_trips = stop_times.merge(
    stops[['stop_lat', 'stop_lon', 'stop_id']], on='stop_id')
full_trips.head()

# %% merge trips into full-trips by trips id
full_trips = full_trips.merge(trips[['trip_id', 'route_id']], on='trip_id')
full_trips.head()


# %% customize function
def validate_time(date_str):
    x = int(date_str.split(':', 1)[0])
    if x >= 24:
             return str(x % 24) + date_str[2:]
    else:
        return date_str

print(validate_time('49:01:41'))

# %% clean the time format
full_trips['arrival_time'] = full_trips['arrival_time'].apply(validate_time)
full_trips['arrival_time'] = full_trips['arrival_time'].apply(
    lambda x: x.replace(' ', '0')
)
full_trips['departure_time'] = full_trips['departure_time'].apply(validate_time)
full_trips['departure_time'] = full_trips['departure_time'].apply(
    lambda x: x.replace(' ', '0')
)
print(full_trips)

# %%
full_trips['arrival_time'] = pd.to_datetime(
    full_trips['arrival_time'], format="%H:%M:%S").dt.time
    
full_trips['departure_time'] = pd.to_datetime(
    full_trips['departure_time'], format="%H:%M:%S").dt.time

print(full_trips)

# %%

# full_trips.to.csv('./data/ful_trips')
