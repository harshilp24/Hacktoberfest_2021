import COVID19Py
import pandas as pnds

covid19 = COVID19Py.COVID19()
# Get all Data Filter by Death Sort
location = covid19.getLocationByCountryCode("IN")
# location = covid19.getLocations(rank_by='deaths')
covidInfo = []
print(location[0])
for list in location:
    covidInfo.append({
        "Country": list['country'],
        "Total Population": list['country_population'],
        "Total Death": list['latest']['deaths'],
        "Total Recovered": list['latest']['recovered'],
        "Total Confirmed": list['latest']['confirmed'], })
pnds.set_option('display.max_rows', None)
# pnds.set_option('display.max_columns', None)
df = pnds.DataFrame(covidInfo).set_index(
    "Country")
print(df)
df.to_csv(
    r'covid_death_info.csv', index=True)
