import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from flask import Flask, jsonify, render_template
import pandas as pd
import json

todayDate="12-07-2020"

app = Flask(__name__)

engine = create_engine("postgres://hdsqfkpfyrmcls:44d0c2afaa4b73f05e08bd94b4604fdb7b43432e1260f0ee78d4fbf9adae54d2@ec2-34-239-241-25.compute-1.amazonaws.com:5432/ddnn9438k8o9n9", echo=False)
conn = engine.connect()

# us_counties_cases=  pd.read_sql("select * from counties_cases",conn)
# us_counties_deaths=  pd.read_sql("select * from counties_deaths",conn)

# us_states_cases = pd.read_sql("select * from states_cases", conn)
# us_states_deaths = pd.read_sql("select * from states_deaths", conn)
# print(us_states)

states_list_df = pd.read_sql("select distinct state from states_cases WHERE NOT state = 'None'",conn).sort_values('state')

states_list= states_list_df['state']
# print(states_list)
# print(states_list)

#variables for sql loops
queries_cases_county=[]
queries_deaths_county=[]
result_cases_county=[]
result_deaths_county=[]
parsed_cases_county=[]
parsed_deaths_county=[]

queries_cases_states_full=[]
queries_deaths_states_full=[]
result_cases_states_full =[]
result_deaths_states_full=[]
parsed_cases_states_full = []
parsed_deaths_states_full=[]

queries_cases_states_today=[]
queries_deaths_states_today=[]
result_cases_states_today=[]
result_deaths_states_today=[]
parsed_cases_states_today=[]
parsed_deaths_states_today=[]

queries_us_today=[]
result_us_today=[]
parsed_us_today=[]

queries_us_today= pd.read_sql(f"select * from us_overall where date = '2020-12-07'", conn)
print(queries_us_today)
result_us_today= queries_us_today.to_json(orient='index')
parsed_us_today= json.loads(result_us_today)
print(parsed_us_today)


# once select a state from states_list need to populate state data
for state in states_list:
    queries_cases_county.append(pd.read_sql(f"select * from counties_cases where state = '{state}' and NOT county ISNULL and 'cases'!= 'N'",conn))
    queries_deaths_county.append(pd.read_sql(f"select * from counties_deaths where state = '{state}'and NOT county ISNULL and 'deaths' != 'N'",conn))
    queries_cases_states_full.append(pd.read_sql(f"select * from states_cases where state = '{state}' and NOT date ISNULL and 'cases'!= 'N'",conn))
    queries_deaths_states_full.append(pd.read_sql(f"select * from states_deaths where state = '{state}' and NOT date ISNULL and 'deaths' != 'N'",conn))
    queries_cases_states_today.append(pd.read_sql(f"select * from states_cases where state = '{state}' and date= '{todayDate}' and 'cases'!= 'N'",conn))
    queries_deaths_states_today.append(pd.read_sql(f"select * from states_deaths where state = '{state}' and date= '{todayDate}'and 'deaths' != 'N'",conn))

# loop to jsonify cases for county queries
for x in range(len(queries_cases_county)):
    result_cases_county.append(queries_cases_county[x].to_json(orient='index'))
    parsed_cases_county.append(json.loads(result_cases_county[x]))

# loop to jsonify deaths for county queries
for x in range(len(queries_deaths_county)):
    result_deaths_county.append(queries_deaths_county[x].to_json(orient='index'))
    parsed_deaths_county.append(json.loads(result_deaths_county[x]))

# jsonify cases for state full data 
for x in range(len(queries_cases_states_full)):
    result_cases_states_full.append(queries_cases_states_full[x].to_json(orient='index'))
    parsed_cases_states_full.append(json.loads(result_cases_states_full[x]))

# jsonify deaths for state full data 
for x in range(len(queries_deaths_states_full)):
    result_deaths_states_full.append(queries_deaths_states_full[x].to_json(orient='index'))
    parsed_deaths_states_full.append(json.loads(result_deaths_states_full[x]))

# jsonify cases for today state queries:
for x in range(len(queries_cases_states_today)):
    result_cases_states_today.append(queries_cases_states_today[x].to_json(orient='index'))
    parsed_cases_states_today.append(json.loads(result_cases_states_today[x]))

# jsonify deaths for today state queries:
for x in range(len(queries_deaths_states_today)):
    result_deaths_states_today.append(queries_deaths_states_today[x].to_json(orient='index'))
    parsed_deaths_states_today.append(json.loads(result_deaths_states_today[x]))


# ALABAMA COUNTY DATA:
queries_alabama_counties_cases=pd.read_sql(f"select * from counties_cases where state = 'Alabama' and NOT county ISNULL and cases != 'N'",conn)
result_alabama_counties_cases=queries_alabama_counties_cases.to_json(orient='index')
parsed_alabama_counties_cases=json.loads(result_alabama_counties_cases)

queries_alabama_counties_deaths=pd.read_sql(f"select * from counties_deaths where state = 'Alabama' and NOT county ISNULL and deaths != 'N'",conn)
result_alabama_counties_deaths=queries_alabama_counties_deaths.to_json(orient='index')
parsed_alabama_counties_deaths=json.loads(result_alabama_counties_deaths)


# ALABAMA STATE DATA:
queries_alabama_state_cases= pd.read_sql(f"select * from states_cases where state = 'Alabama' and NOT state ISNULL and cases != 'N'",conn)
result_alabama_state_cases=queries_alabama_state_cases.to_json(orient='index')
parsed_alabama_state_cases=json.loads(result_alabama_state_cases)

queries_alabama_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Alabama' and NOT state ISNULL and deaths != 'N'",conn)
result_alabama_state_deaths=queries_alabama_state_deaths.to_json(orient='index')
parsed_alabama_state_deaths=json.loads(result_alabama_state_deaths)

queries_alabama_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Alabama' and NOT state ISNULL",conn)
result_alabama_state_cases_forecast=queries_alabama_state_cases_forecast.to_json(orient='index')
parsed_alabama_state_cases_forecast=json.loads(result_alabama_state_cases_forecast)

queries_alabama_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Alabama' and NOT state ISNULL",conn)
result_alabama_state_deaths_forecast=queries_alabama_state_deaths_forecast.to_json(orient='index')
parsed_alabama_state_deaths_forecast=json.loads(result_alabama_state_deaths_forecast)



# ALASKA STATE DATA:
queries_alaska_state_cases= pd.read_sql(f"select * from states_cases where state = 'Alaska' and NOT state ISNULL and cases != 'N'",conn)
result_alaska_state_cases=queries_alaska_state_cases.to_json(orient='index')
parsed_alaska_state_cases=json.loads(result_alaska_state_cases)

queries_alaska_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Alaska' and NOT state ISNULL and deaths != 'N'",conn)
result_alaska_state_deaths=queries_alaska_state_deaths.to_json(orient='index')
parsed_alaska_state_deaths=json.loads(result_alaska_state_deaths)

queries_alaska_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Alaska' and NOT state ISNULL",conn)
result_alaska_state_cases_forecast=queries_alaska_state_cases_forecast.to_json(orient='index')
parsed_alaska_state_cases_forecast=json.loads(result_alaska_state_cases_forecast)

queries_alaska_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Alaska' and NOT state ISNULL",conn)
result_alaska_state_deaths_forecast=queries_alaska_state_deaths_forecast.to_json(orient='index')
parsed_alaska_state_deaths_forecast=json.loads(result_alaska_state_deaths_forecast)

# ARIZONA STATE DATA:
queries_arizona_state_cases= pd.read_sql(f"select * from states_cases where state = 'Arizona' and NOT state ISNULL and cases != 'N'",conn)
result_arizona_state_cases=queries_arizona_state_cases.to_json(orient='index')
parsed_arizona_state_cases=json.loads(result_arizona_state_cases)

queries_arizona_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Arizona' and NOT state ISNULL and deaths != 'N'",conn)
result_arizona_state_deaths=queries_arizona_state_deaths.to_json(orient='index')
parsed_arizona_state_deaths=json.loads(result_arizona_state_deaths)

queries_arizona_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Arizona' and NOT state ISNULL",conn)
result_arizona_state_cases_forecast=queries_arizona_state_cases_forecast.to_json(orient='index')
parsed_arizona_state_cases_forecast=json.loads(result_arizona_state_cases_forecast)

queries_arizona_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Arizona' and NOT state ISNULL",conn)
result_arizona_state_deaths_forecast=queries_arizona_state_deaths_forecast.to_json(orient='index')
parsed_arizona_state_deaths_forecast=json.loads(result_arizona_state_deaths_forecast)

# ARKANSAS STATE DATA:
queries_arkansas_state_cases= pd.read_sql(f"select * from states_cases where state = 'Arkansas' and NOT state ISNULL and cases != 'N'",conn)
result_arkansas_state_cases=queries_arkansas_state_cases.to_json(orient='index')
parsed_arkansas_state_cases=json.loads(result_arkansas_state_cases)

queries_arkansas_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Arkansas' and NOT state ISNULL and deaths != 'N'",conn)
result_arkansas_state_deaths=queries_arkansas_state_deaths.to_json(orient='index')
parsed_arkansas_state_deaths=json.loads(result_arkansas_state_deaths)

queries_arkansas_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Arkansas' and NOT state ISNULL",conn)
result_arkansas_state_cases_forecast=queries_arkansas_state_cases_forecast.to_json(orient='index')
parsed_arkansas_state_cases_forecast=json.loads(result_arkansas_state_cases_forecast)

queries_arkansas_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Arkansas' and NOT state ISNULL",conn)
result_arkansas_state_deaths_forecast=queries_arkansas_state_deaths_forecast.to_json(orient='index')
parsed_arkansas_state_deaths_forecast=json.loads(result_arkansas_state_deaths_forecast)

# CALIFORNIA STATE DATA:
queries_california_state_cases= pd.read_sql(f"select * from states_cases where state = 'California' and NOT state ISNULL and cases != 'N'",conn)
result_california_state_cases=queries_california_state_cases.to_json(orient='index')
parsed_california_state_cases=json.loads(result_california_state_cases)

queries_california_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'California' and NOT state ISNULL and deaths != 'N'",conn)
result_california_state_deaths=queries_california_state_deaths.to_json(orient='index')
parsed_california_state_deaths=json.loads(result_california_state_deaths)

queries_california_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'California' and NOT state ISNULL",conn)
result_california_state_cases_forecast=queries_california_state_cases_forecast.to_json(orient='index')
parsed_california_state_cases_forecast=json.loads(result_california_state_cases_forecast)

queries_california_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'California' and NOT state ISNULL",conn)
result_california_state_deaths_forecast=queries_california_state_deaths_forecast.to_json(orient='index')
parsed_california_state_deaths_forecast=json.loads(result_california_state_deaths_forecast)

# COLORADO STATE DATA:
queries_colorado_state_cases= pd.read_sql(f"select * from states_cases where state = 'Colorado' and NOT state ISNULL and cases != 'N'",conn)
result_colorado_state_cases=queries_colorado_state_cases.to_json(orient='index')
parsed_colorado_state_cases=json.loads(result_colorado_state_cases)

queries_colorado_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Colorado' and NOT state ISNULL and deaths != 'N'",conn)
result_colorado_state_deaths=queries_colorado_state_deaths.to_json(orient='index')
parsed_colorado_state_deaths=json.loads(result_colorado_state_deaths)

queries_colorado_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Colorado' and NOT state ISNULL",conn)
result_colorado_state_cases_forecast=queries_colorado_state_cases_forecast.to_json(orient='index')
parsed_colorado_state_cases_forecast=json.loads(result_colorado_state_cases_forecast)

queries_colorado_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Colorado' and NOT state ISNULL",conn)
result_colorado_state_deaths_forecast=queries_colorado_state_deaths_forecast.to_json(orient='index')
parsed_colorado_state_deaths_forecast=json.loads(result_colorado_state_deaths_forecast)

# CONNECTICUT STATE DATA:
queries_connecticut_state_cases= pd.read_sql(f"select * from states_cases where state = 'Connecticut' and NOT state ISNULL and cases != 'N'",conn)
result_connecticut_state_cases=queries_connecticut_state_cases.to_json(orient='index')
parsed_connecticut_state_cases=json.loads(result_connecticut_state_cases)

queries_connecticut_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Connecticut' and NOT state ISNULL and deaths != 'N'",conn)
result_connecticut_state_deaths=queries_connecticut_state_deaths.to_json(orient='index')
parsed_connecticut_state_deaths=json.loads(result_connecticut_state_deaths)

queries_connecticut_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Connecticut' and NOT state ISNULL",conn)
result_connecticut_state_cases_forecast=queries_connecticut_state_cases_forecast.to_json(orient='index')
parsed_connecticut_state_cases_forecast=json.loads(result_connecticut_state_cases_forecast)

queries_connecticut_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Connecticut' and NOT state ISNULL",conn)
result_connecticut_state_deaths_forecast=queries_connecticut_state_deaths_forecast.to_json(orient='index')
parsed_connecticut_state_deaths_forecast=json.loads(result_connecticut_state_deaths_forecast)

# DELAWARE STATE DATA:
queries_delaware_state_cases= pd.read_sql(f"select * from states_cases where state = 'Delaware' and NOT state ISNULL and cases != 'N'",conn)
result_delaware_state_cases=queries_delaware_state_cases.to_json(orient='index')
parsed_delaware_state_cases=json.loads(result_delaware_state_cases)

queries_delaware_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Delaware' and NOT state ISNULL and deaths != 'N'",conn)
result_delaware_state_deaths=queries_delaware_state_deaths.to_json(orient='index')
parsed_delaware_state_deaths=json.loads(result_delaware_state_deaths)

queries_delaware_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Delaware' and NOT state ISNULL",conn)
result_delaware_state_cases_forecast=queries_delaware_state_cases_forecast.to_json(orient='index')
parsed_delaware_state_cases_forecast=json.loads(result_delaware_state_cases_forecast)

queries_delaware_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Delaware' and NOT state ISNULL",conn)
result_delaware_state_deaths_forecast=queries_delaware_state_deaths_forecast.to_json(orient='index')
parsed_delaware_state_deaths_forecast=json.loads(result_delaware_state_deaths_forecast)

# DISTRICT OF COLOUMBIA STATE DATA:
queries_dc_state_cases= pd.read_sql(f"select * from states_cases where state = 'District of Columbia' and NOT state ISNULL and cases != 'N'",conn)
result_dc_state_cases=queries_dc_state_cases.to_json(orient='index')
parsed_dc_state_cases=json.loads(result_dc_state_cases)

queries_dc_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'District of Columbia' and NOT state ISNULL and deaths != 'N'",conn)
result_dc_state_deaths=queries_dc_state_deaths.to_json(orient='index')
parsed_dc_state_deaths=json.loads(result_dc_state_deaths)

queries_dc_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'District of Columbia' and NOT state ISNULL",conn)
result_dc_state_cases_forecast=queries_dc_state_cases_forecast.to_json(orient='index')
parsed_dc_state_cases_forecast=json.loads(result_dc_state_cases_forecast)

queries_dc_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'District of Columbia' and NOT state ISNULL",conn)
result_dc_state_deaths_forecast=queries_dc_state_deaths_forecast.to_json(orient='index')
parsed_dc_state_deaths_forecast=json.loads(result_dc_state_deaths_forecast)

# FLORIDA STATE DATA:
queries_florida_state_cases= pd.read_sql(f"select * from states_cases where state = 'Florida' and NOT state ISNULL and cases != 'N'",conn)
result_florida_state_cases=queries_florida_state_cases.to_json(orient='index')
parsed_florida_state_cases=json.loads(result_florida_state_cases)

queries_florida_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Florida' and NOT state ISNULL and deaths != 'N'",conn)
result_florida_state_deaths=queries_florida_state_deaths.to_json(orient='index')
parsed_florida_state_deaths=json.loads(result_florida_state_deaths)

queries_florida_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Florida' and NOT state ISNULL",conn)
result_florida_state_cases_forecast=queries_florida_state_cases_forecast.to_json(orient='index')
parsed_florida_state_cases_forecast=json.loads(result_florida_state_cases_forecast)

queries_florida_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Florida' and NOT state ISNULL",conn)
result_florida_state_deaths_forecast=queries_florida_state_deaths_forecast.to_json(orient='index')
parsed_florida_state_deaths_forecast=json.loads(result_florida_state_deaths_forecast)

# GEORGIA STATE DATA:
queries_georgia_state_cases= pd.read_sql(f"select * from states_cases where state = 'Georgia' and NOT state ISNULL and cases != 'N'",conn)
result_georgia_state_cases=queries_georgia_state_cases.to_json(orient='index')
parsed_georgia_state_cases=json.loads(result_georgia_state_cases)

queries_georgia_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Georgia' and NOT state ISNULL and deaths != 'N'",conn)
result_georgia_state_deaths=queries_georgia_state_deaths.to_json(orient='index')
parsed_georgia_state_deaths=json.loads(result_georgia_state_deaths)

queries_georgia_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Georgia' and NOT state ISNULL",conn)
result_georgia_state_cases_forecast=queries_georgia_state_cases_forecast.to_json(orient='index')
parsed_georgia_state_cases_forecast=json.loads(result_georgia_state_cases_forecast)

queries_georgia_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Georgia' and NOT state ISNULL",conn)
result_georgia_state_deaths_forecast=queries_georgia_state_deaths_forecast.to_json(orient='index')
parsed_georgia_state_deaths_forecast=json.loads(result_georgia_state_deaths_forecast)

# GUAM STATE DATA:
queries_guam_state_cases= pd.read_sql(f"select * from states_cases where state = 'Guam' and NOT state ISNULL and cases != 'N'",conn)
result_guam_state_cases=queries_guam_state_cases.to_json(orient='index')
parsed_guam_state_cases=json.loads(result_guam_state_cases)

queries_guam_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Guam' and NOT state ISNULL and deaths != 'N'",conn)
result_guam_state_deaths=queries_guam_state_deaths.to_json(orient='index')
parsed_guam_state_deaths=json.loads(result_guam_state_deaths)

queries_guam_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Guam' and NOT state ISNULL",conn)
result_guam_state_cases_forecast=queries_guam_state_cases_forecast.to_json(orient='index')
parsed_guam_state_cases_forecast=json.loads(result_guam_state_cases_forecast)

queries_guam_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Guam' and NOT state ISNULL",conn)
result_guam_state_deaths_forecast=queries_guam_state_deaths_forecast.to_json(orient='index')
parsed_guam_state_deaths_forecast=json.loads(result_guam_state_deaths_forecast)

# HAWAII STATE DATA:
queries_hawaii_state_cases= pd.read_sql(f"select * from states_cases where state = 'Hawaii' and NOT state ISNULL and cases != 'N'",conn)
result_hawaii_state_cases=queries_hawaii_state_cases.to_json(orient='index')
parsed_hawaii_state_cases=json.loads(result_hawaii_state_cases)

queries_hawaii_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Hawaii' and NOT state ISNULL and deaths != 'N'",conn)
result_hawaii_state_deaths=queries_hawaii_state_deaths.to_json(orient='index')
parsed_hawaii_state_deaths=json.loads(result_hawaii_state_deaths)

queries_hawaii_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Hawaii' and NOT state ISNULL",conn)
result_hawaii_state_cases_forecast=queries_hawaii_state_cases_forecast.to_json(orient='index')
parsed_hawaii_state_cases_forecast=json.loads(result_hawaii_state_cases_forecast)

queries_hawaii_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Hawaii' and NOT state ISNULL",conn)
result_hawaii_state_deaths_forecast=queries_hawaii_state_deaths_forecast.to_json(orient='index')
parsed_hawaii_state_deaths_forecast=json.loads(result_hawaii_state_deaths_forecast)

# IDAHO STATE DATA:
queries_idaho_state_cases= pd.read_sql(f"select * from states_cases where state = 'Idaho' and NOT state ISNULL and cases != 'N'",conn)
result_idaho_state_cases=queries_idaho_state_cases.to_json(orient='index')
parsed_idaho_state_cases=json.loads(result_idaho_state_cases)

queries_idaho_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Idaho' and NOT state ISNULL and deaths != 'N'",conn)
result_idaho_state_deaths=queries_idaho_state_deaths.to_json(orient='index')
parsed_idaho_state_deaths=json.loads(result_idaho_state_deaths)

queries_idaho_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Idaho' and NOT state ISNULL",conn)
result_idaho_state_cases_forecast=queries_idaho_state_cases_forecast.to_json(orient='index')
parsed_idaho_state_cases_forecast=json.loads(result_idaho_state_cases_forecast)

queries_idaho_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Idaho' and NOT state ISNULL",conn)
result_idaho_state_deaths_forecast=queries_idaho_state_deaths_forecast.to_json(orient='index')
parsed_idaho_state_deaths_forecast=json.loads(result_idaho_state_deaths_forecast)

# ILLINOIS STATE DATA:
queries_illinois_state_cases= pd.read_sql(f"select * from states_cases where state = 'Illinois' and NOT state ISNULL and cases != 'N'",conn)
result_illinois_state_cases=queries_illinois_state_cases.to_json(orient='index')
parsed_illinois_state_cases=json.loads(result_illinois_state_cases)

queries_illinois_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Illinois' and NOT state ISNULL and deaths != 'N'",conn)
result_illinois_state_deaths=queries_illinois_state_deaths.to_json(orient='index')
parsed_illinois_state_deaths=json.loads(result_illinois_state_deaths)

queries_illinois_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Illinois' and NOT state ISNULL",conn)
result_illinois_state_cases_forecast=queries_illinois_state_cases_forecast.to_json(orient='index')
parsed_illinois_state_cases_forecast=json.loads(result_illinois_state_cases_forecast)

queries_illinois_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Illinois' and NOT state ISNULL",conn)
result_illinois_state_deaths_forecast=queries_illinois_state_deaths_forecast.to_json(orient='index')
parsed_illinois_state_deaths_forecast=json.loads(result_illinois_state_deaths_forecast)

# INDIANA STATE DATA:
queries_indiana_state_cases= pd.read_sql(f"select * from states_cases where state = 'Indiana' and NOT state ISNULL and cases != 'N'",conn)
result_indiana_state_cases=queries_indiana_state_cases.to_json(orient='index')
parsed_indiana_state_cases=json.loads(result_indiana_state_cases)

queries_indiana_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Indiana' and NOT state ISNULL and deaths != 'N'",conn)
result_indiana_state_deaths=queries_indiana_state_deaths.to_json(orient='index')
parsed_indiana_state_deaths=json.loads(result_indiana_state_deaths)

queries_indiana_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Indiana' and NOT state ISNULL",conn)
result_indiana_state_cases_forecast=queries_indiana_state_cases_forecast.to_json(orient='index')
parsed_indiana_state_cases_forecast=json.loads(result_indiana_state_cases_forecast)

queries_indiana_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Indiana' and NOT state ISNULL",conn)
result_indiana_state_deaths_forecast=queries_indiana_state_deaths_forecast.to_json(orient='index')
parsed_indiana_state_deaths_forecast=json.loads(result_indiana_state_deaths_forecast)


# IOWA STATE DATA:
queries_iowa_state_cases= pd.read_sql(f"select * from states_cases where state = 'Iowa' and NOT state ISNULL and cases != 'N'",conn)
result_iowa_state_cases=queries_iowa_state_cases.to_json(orient='index')
parsed_iowa_state_cases=json.loads(result_iowa_state_cases)

queries_iowa_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Iowa' and NOT state ISNULL and deaths != 'N'",conn)
result_iowa_state_deaths=queries_iowa_state_deaths.to_json(orient='index')
parsed_iowa_state_deaths=json.loads(result_iowa_state_deaths)

queries_iowa_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Iowa' and NOT state ISNULL",conn)
result_iowa_state_cases_forecast=queries_iowa_state_cases_forecast.to_json(orient='index')
parsed_iowa_state_cases_forecast=json.loads(result_iowa_state_cases_forecast)

queries_iowa_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Iowa' and NOT state ISNULL",conn)
result_iowa_state_deaths_forecast=queries_iowa_state_deaths_forecast.to_json(orient='index')
parsed_iowa_state_deaths_forecast=json.loads(result_iowa_state_deaths_forecast)

# KANSAS STATE DATA:
queries_kansas_state_cases= pd.read_sql(f"select * from states_cases where state = 'Kansas' and NOT state ISNULL and cases != 'N'",conn)
result_kansas_state_cases=queries_kansas_state_cases.to_json(orient='index')
parsed_kansas_state_cases=json.loads(result_kansas_state_cases)

queries_kansas_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Kansas' and NOT state ISNULL and deaths != 'N'",conn)
result_kansas_state_deaths=queries_kansas_state_deaths.to_json(orient='index')
parsed_kansas_state_deaths=json.loads(result_kansas_state_deaths)

queries_kansas_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Kansas' and NOT state ISNULL",conn)
result_kansas_state_cases_forecast=queries_kansas_state_cases_forecast.to_json(orient='index')
parsed_kansas_state_cases_forecast=json.loads(result_kansas_state_cases_forecast)

queries_kansas_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Kansas' and NOT state ISNULL",conn)
result_kansas_state_deaths_forecast=queries_kansas_state_deaths_forecast.to_json(orient='index')
parsed_kansas_state_deaths_forecast=json.loads(result_kansas_state_deaths_forecast)

# KENTUCKY STATE DATA:
queries_kentucky_state_cases= pd.read_sql(f"select * from states_cases where state = 'Kentucky' and NOT state ISNULL and cases != 'N'",conn)
result_kentucky_state_cases=queries_kentucky_state_cases.to_json(orient='index')
parsed_kentucky_state_cases=json.loads(result_kentucky_state_cases)

queries_kentucky_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Kentucky' and NOT state ISNULL and deaths != 'N'",conn)
result_kentucky_state_deaths=queries_kentucky_state_deaths.to_json(orient='index')
parsed_kentucky_state_deaths=json.loads(result_kentucky_state_deaths)

queries_kentucky_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Kentucky' and NOT state ISNULL",conn)
result_kentucky_state_cases_forecast=queries_kentucky_state_cases_forecast.to_json(orient='index')
parsed_kentucky_state_cases_forecast=json.loads(result_kentucky_state_cases_forecast)

queries_kentucky_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Kentucky' and NOT state ISNULL",conn)
result_kentucky_state_deaths_forecast=queries_kentucky_state_deaths_forecast.to_json(orient='index')
parsed_kentucky_state_deaths_forecast=json.loads(result_kentucky_state_deaths_forecast)

# LOUISIANA STATE DATA:
queries_louisiana_state_cases= pd.read_sql(f"select * from states_cases where state = 'Louisiana' and NOT state ISNULL and cases != 'N'",conn)
result_louisiana_state_cases=queries_louisiana_state_cases.to_json(orient='index')
parsed_louisiana_state_cases=json.loads(result_louisiana_state_cases)

queries_louisiana_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Louisiana' and NOT state ISNULL and deaths != 'N'",conn)
result_louisiana_state_deaths=queries_louisiana_state_deaths.to_json(orient='index')
parsed_louisiana_state_deaths=json.loads(result_louisiana_state_deaths)

queries_louisiana_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Louisiana' and NOT state ISNULL",conn)
result_louisiana_state_cases_forecast=queries_louisiana_state_cases_forecast.to_json(orient='index')
parsed_louisiana_state_cases_forecast=json.loads(result_louisiana_state_cases_forecast)

queries_louisiana_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Louisiana' and NOT state ISNULL",conn)
result_louisiana_state_deaths_forecast=queries_louisiana_state_deaths_forecast.to_json(orient='index')
parsed_louisiana_state_deaths_forecast=json.loads(result_louisiana_state_deaths_forecast)

# MAINE STATE DATA:
queries_maine_state_cases= pd.read_sql(f"select * from states_cases where state = 'Maine' and NOT state ISNULL and cases != 'N'",conn)
result_maine_state_cases=queries_maine_state_cases.to_json(orient='index')
parsed_maine_state_cases=json.loads(result_maine_state_cases)

queries_maine_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Maine' and NOT state ISNULL and deaths != 'N'",conn)
result_maine_state_deaths=queries_maine_state_deaths.to_json(orient='index')
parsed_maine_state_deaths=json.loads(result_maine_state_deaths)

queries_maine_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Maine' and NOT state ISNULL",conn)
result_maine_state_cases_forecast=queries_maine_state_cases_forecast.to_json(orient='index')
parsed_maine_state_cases_forecast=json.loads(result_maine_state_cases_forecast)

queries_maine_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Maine' and NOT state ISNULL",conn)
result_maine_state_deaths_forecast=queries_maine_state_deaths_forecast.to_json(orient='index')
parsed_maine_state_deaths_forecast=json.loads(result_maine_state_deaths_forecast)

# MARYLAND STATE DATA:
queries_maryland_state_cases= pd.read_sql(f"select * from states_cases where state = 'Maryland' and NOT state ISNULL and cases != 'N'",conn)
result_maryland_state_cases=queries_maryland_state_cases.to_json(orient='index')
parsed_maryland_state_cases=json.loads(result_maryland_state_cases)

queries_maryland_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Maryland' and NOT state ISNULL and deaths != 'N'",conn)
result_maryland_state_deaths=queries_maryland_state_deaths.to_json(orient='index')
parsed_maryland_state_deaths=json.loads(result_maryland_state_deaths)

queries_maryland_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Maryland' and NOT state ISNULL",conn)
result_maryland_state_cases_forecast=queries_maryland_state_cases_forecast.to_json(orient='index')
parsed_maryland_state_cases_forecast=json.loads(result_maryland_state_cases_forecast)

queries_maryland_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Maryland' and NOT state ISNULL",conn)
result_maryland_state_deaths_forecast=queries_maryland_state_deaths_forecast.to_json(orient='index')
parsed_maryland_state_deaths_forecast=json.loads(result_maryland_state_deaths_forecast)

# MASSACHUSETTS STATE DATA:
queries_massachusetts_state_cases= pd.read_sql(f"select * from states_cases where state = 'Massachusetts' and NOT state ISNULL and cases != 'N'",conn)
result_massachusetts_state_cases=queries_massachusetts_state_cases.to_json(orient='index')
parsed_massachusetts_state_cases=json.loads(result_massachusetts_state_cases)

queries_massachusetts_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Massachusetts' and NOT state ISNULL and deaths != 'N'",conn)
result_massachusetts_state_deaths=queries_massachusetts_state_deaths.to_json(orient='index')
parsed_massachusetts_state_deaths=json.loads(result_massachusetts_state_deaths)

queries_massachusetts_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Massachusetts' and NOT state ISNULL",conn)
result_massachusetts_state_cases_forecast=queries_massachusetts_state_cases_forecast.to_json(orient='index')
parsed_massachusetts_state_cases_forecast=json.loads(result_massachusetts_state_cases_forecast)

queries_massachusetts_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Massachusetts' and NOT state ISNULL",conn)
result_massachusetts_state_deaths_forecast=queries_massachusetts_state_deaths_forecast.to_json(orient='index')
parsed_massachusetts_state_deaths_forecast=json.loads(result_massachusetts_state_deaths_forecast)

# MICHIGAN STATE DATA:
queries_michigan_state_cases= pd.read_sql(f"select * from states_cases where state = 'Michigan' and NOT state ISNULL and cases != 'N'",conn)
result_michigan_state_cases=queries_michigan_state_cases.to_json(orient='index')
parsed_michigan_state_cases=json.loads(result_michigan_state_cases)

queries_michigan_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Michigan' and NOT state ISNULL and deaths != 'N'",conn)
result_michigan_state_deaths=queries_michigan_state_deaths.to_json(orient='index')
parsed_michigan_state_deaths=json.loads(result_michigan_state_deaths)

queries_michigan_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Michigan' and NOT state ISNULL",conn)
result_michigan_state_cases_forecast=queries_michigan_state_cases_forecast.to_json(orient='index')
parsed_michigan_state_cases_forecast=json.loads(result_michigan_state_cases_forecast)

queries_michigan_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Michigan' and NOT state ISNULL",conn)
result_michigan_state_deaths_forecast=queries_michigan_state_deaths_forecast.to_json(orient='index')
parsed_michigan_state_deaths_forecast=json.loads(result_michigan_state_deaths_forecast)

# MINNESOTA STATE DATA:
queries_minnesota_state_cases= pd.read_sql(f"select * from states_cases where state = 'Minnesota' and NOT state ISNULL and cases != 'N'",conn)
result_minnesota_state_cases=queries_minnesota_state_cases.to_json(orient='index')
parsed_minnesota_state_cases=json.loads(result_minnesota_state_cases)

queries_minnesota_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Minnesota' and NOT state ISNULL and deaths != 'N'",conn)
result_minnesota_state_deaths=queries_minnesota_state_deaths.to_json(orient='index')
parsed_minnesota_state_deaths=json.loads(result_minnesota_state_deaths)

queries_minnesota_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Minnesota' and NOT state ISNULL",conn)
result_minnesota_state_cases_forecast=queries_minnesota_state_cases_forecast.to_json(orient='index')
parsed_minnesota_state_cases_forecast=json.loads(result_minnesota_state_cases_forecast)

queries_minnesota_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Minnesota' and NOT state ISNULL",conn)
result_minnesota_state_deaths_forecast=queries_minnesota_state_deaths_forecast.to_json(orient='index')
parsed_minnesota_state_deaths_forecast=json.loads(result_minnesota_state_deaths_forecast)

# MISSISSIPPI STATE DATA:
queries_mississippi_state_cases= pd.read_sql(f"select * from states_cases where state = 'Mississippi' and NOT state ISNULL and cases != 'N'",conn)
result_mississippi_state_cases=queries_mississippi_state_cases.to_json(orient='index')
parsed_mississippi_state_cases=json.loads(result_mississippi_state_cases)

queries_mississippi_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Mississippi' and NOT state ISNULL and deaths != 'N'",conn)
result_mississippi_state_deaths=queries_mississippi_state_deaths.to_json(orient='index')
parsed_mississippi_state_deaths=json.loads(result_mississippi_state_deaths)

queries_mississippi_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Mississippi' and NOT state ISNULL",conn)
result_mississippi_state_cases_forecast=queries_mississippi_state_cases_forecast.to_json(orient='index')
parsed_mississippi_state_cases_forecast=json.loads(result_mississippi_state_cases_forecast)

queries_mississippi_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Mississippi' and NOT state ISNULL",conn)
result_mississippi_state_deaths_forecast=queries_mississippi_state_deaths_forecast.to_json(orient='index')
parsed_mississippi_state_deaths_forecast=json.loads(result_mississippi_state_deaths_forecast)

# MISSOURI STATE DATA:
queries_missouri_state_cases= pd.read_sql(f"select * from states_cases where state = 'Missouri' and NOT state ISNULL and cases != 'N'",conn)
result_missouri_state_cases=queries_missouri_state_cases.to_json(orient='index')
parsed_missouri_state_cases=json.loads(result_missouri_state_cases)

queries_missouri_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Missouri' and NOT state ISNULL and deaths != 'N'",conn)
result_missouri_state_deaths=queries_missouri_state_deaths.to_json(orient='index')
parsed_missouri_state_deaths=json.loads(result_missouri_state_deaths)

queries_missouri_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Missouri' and NOT state ISNULL",conn)
result_missouri_state_cases_forecast=queries_missouri_state_cases_forecast.to_json(orient='index')
parsed_missouri_state_cases_forecast=json.loads(result_missouri_state_cases_forecast)

queries_missouri_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Missouri' and NOT state ISNULL",conn)
result_missouri_state_deaths_forecast=queries_missouri_state_deaths_forecast.to_json(orient='index')
parsed_missouri_state_deaths_forecast=json.loads(result_missouri_state_deaths_forecast)

# MONTANA STATE DATA:
queries_montana_state_cases= pd.read_sql(f"select * from states_cases where state = 'Montana' and NOT state ISNULL and cases != 'N'",conn)
result_montana_state_cases=queries_montana_state_cases.to_json(orient='index')
parsed_montana_state_cases=json.loads(result_montana_state_cases)

queries_montana_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Montana' and NOT state ISNULL and deaths != 'N'",conn)
result_montana_state_deaths=queries_montana_state_deaths.to_json(orient='index')
parsed_montana_state_deaths=json.loads(result_montana_state_deaths)

queries_montana_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Montana' and NOT state ISNULL",conn)
result_montana_state_cases_forecast=queries_montana_state_cases_forecast.to_json(orient='index')
parsed_montana_state_cases_forecast=json.loads(result_montana_state_cases_forecast)

queries_montana_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Montana' and NOT state ISNULL",conn)
result_montana_state_deaths_forecast=queries_montana_state_deaths_forecast.to_json(orient='index')
parsed_montana_state_deaths_forecast=json.loads(result_montana_state_deaths_forecast)

# NEBRASKA STATE DATA:
queries_nebraska_state_cases= pd.read_sql(f"select * from states_cases where state = 'Nebraska' and NOT state ISNULL and cases != 'N'",conn)
result_nebraska_state_cases=queries_nebraska_state_cases.to_json(orient='index')
parsed_nebraska_state_cases=json.loads(result_nebraska_state_cases)

queries_nebraska_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Nebraska' and NOT state ISNULL and deaths != 'N'",conn)
result_nebraska_state_deaths=queries_nebraska_state_deaths.to_json(orient='index')
parsed_nebraska_state_deaths=json.loads(result_nebraska_state_deaths)

queries_nebraska_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Nebraska' and NOT state ISNULL",conn)
result_nebraska_state_cases_forecast=queries_nebraska_state_cases_forecast.to_json(orient='index')
parsed_nebraska_state_cases_forecast=json.loads(result_nebraska_state_cases_forecast)

queries_nebraska_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Nebraska' and NOT state ISNULL",conn)
result_nebraska_state_deaths_forecast=queries_nebraska_state_deaths_forecast.to_json(orient='index')
parsed_nebraska_state_deaths_forecast=json.loads(result_nebraska_state_deaths_forecast)

# NEVADA STATE DATA:
queries_nevada_state_cases= pd.read_sql(f"select * from states_cases where state = 'Nevada' and NOT state ISNULL and cases != 'N'",conn)
result_nevada_state_cases=queries_nevada_state_cases.to_json(orient='index')
parsed_nevada_state_cases=json.loads(result_nevada_state_cases)

queries_nevada_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Nevada' and NOT state ISNULL and deaths != 'N'",conn)
result_nevada_state_deaths=queries_nevada_state_deaths.to_json(orient='index')
parsed_nevada_state_deaths=json.loads(result_nevada_state_deaths)

queries_nevada_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Nevada' and NOT state ISNULL",conn)
result_nevada_state_cases_forecast=queries_nevada_state_cases_forecast.to_json(orient='index')
parsed_nevada_state_cases_forecast=json.loads(result_nevada_state_cases_forecast)

queries_nevada_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Nevada' and NOT state ISNULL",conn)
result_nevada_state_deaths_forecast=queries_nevada_state_deaths_forecast.to_json(orient='index')
parsed_nevada_state_deaths_forecast=json.loads(result_nevada_state_deaths_forecast)

# NEW HAMPSHIRE STATE DATA:
queries_new_hampshire_state_cases= pd.read_sql(f"select * from states_cases where state = 'New Hampshire' and NOT state ISNULL and cases != 'N'",conn)
result_new_hampshire_state_cases=queries_new_hampshire_state_cases.to_json(orient='index')
parsed_new_hampshire_state_cases=json.loads(result_new_hampshire_state_cases)

queries_new_hampshire_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'New Hampshire' and NOT state ISNULL and deaths != 'N'",conn)
result_new_hampshire_state_deaths=queries_new_hampshire_state_deaths.to_json(orient='index')
parsed_new_hampshire_state_deaths=json.loads(result_new_hampshire_state_deaths)

queries_new_hampshire_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'New Hampshire' and NOT state ISNULL",conn)
result_new_hampshire_state_cases_forecast=queries_new_hampshire_state_cases_forecast.to_json(orient='index')
parsed_new_hampshire_state_cases_forecast=json.loads(result_new_hampshire_state_cases_forecast)

queries_new_hampshire_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'New Hampshire' and NOT state ISNULL",conn)
result_new_hampshire_state_deaths_forecast=queries_new_hampshire_state_deaths_forecast.to_json(orient='index')
parsed_new_hampshire_state_deaths_forecast=json.loads(result_new_hampshire_state_deaths_forecast)

# NEW JERSEY STATE DATA:
queries_new_jersey_state_cases= pd.read_sql(f"select * from states_cases where state = 'New Jersey' and NOT state ISNULL and cases != 'N'",conn)
result_new_jersey_state_cases=queries_new_jersey_state_cases.to_json(orient='index')
parsed_new_jersey_state_cases=json.loads(result_new_jersey_state_cases)

queries_new_jersey_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'New Jersey' and NOT state ISNULL and deaths != 'N'",conn)
result_new_jersey_state_deaths=queries_new_jersey_state_deaths.to_json(orient='index')
parsed_new_jersey_state_deaths=json.loads(result_new_jersey_state_deaths)

queries_new_jersey_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'New Jersey' and NOT state ISNULL",conn)
result_new_jersey_state_cases_forecast=queries_new_jersey_state_cases_forecast.to_json(orient='index')
parsed_new_jersey_state_cases_forecast=json.loads(result_new_jersey_state_cases_forecast)

queries_new_jersey_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'New Jersey' and NOT state ISNULL",conn)
result_new_jersey_state_deaths_forecast=queries_new_jersey_state_deaths_forecast.to_json(orient='index')
parsed_new_jersey_state_deaths_forecast=json.loads(result_new_jersey_state_deaths_forecast)

# NEW MEXICO STATE DATA:
queries_new_mexico_state_cases= pd.read_sql(f"select * from states_cases where state = 'New Mexico' and NOT state ISNULL and cases != 'N'",conn)
result_new_mexico_state_cases=queries_new_mexico_state_cases.to_json(orient='index')
parsed_new_mexico_state_cases=json.loads(result_new_mexico_state_cases)

queries_new_mexico_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'New Mexico' and NOT state ISNULL and deaths != 'N'",conn)
result_new_mexico_state_deaths=queries_new_mexico_state_deaths.to_json(orient='index')
parsed_new_mexico_state_deaths=json.loads(result_new_mexico_state_deaths)

queries_new_mexico_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'New Mexico' and NOT state ISNULL",conn)
result_new_mexico_state_cases_forecast=queries_new_mexico_state_cases_forecast.to_json(orient='index')
parsed_new_mexico_state_cases_forecast=json.loads(result_new_mexico_state_cases_forecast)

queries_new_mexico_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'New Mexico' and NOT state ISNULL",conn)
result_new_mexico_state_deaths_forecast=queries_new_mexico_state_deaths_forecast.to_json(orient='index')
parsed_new_mexico_state_deaths_forecast=json.loads(result_new_mexico_state_deaths_forecast)

# NEW YORK STATE DATA:
queries_new_york_state_cases= pd.read_sql(f"select * from states_cases where state = 'New York' and NOT state ISNULL and cases != 'N'",conn)
result_new_york_state_cases=queries_new_york_state_cases.to_json(orient='index')
parsed_new_york_state_cases=json.loads(result_new_york_state_cases)

queries_new_york_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'New York' and NOT state ISNULL and deaths != 'N'",conn)
result_new_york_state_deaths=queries_new_york_state_deaths.to_json(orient='index')
parsed_new_york_state_deaths=json.loads(result_new_york_state_deaths)

queries_new_york_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'New York' and NOT state ISNULL",conn)
result_new_york_state_cases_forecast=queries_new_york_state_cases_forecast.to_json(orient='index')
parsed_new_york_state_cases_forecast=json.loads(result_new_york_state_cases_forecast)

queries_new_york_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'New York' and NOT state ISNULL",conn)
result_new_york_state_deaths_forecast=queries_new_york_state_deaths_forecast.to_json(orient='index')
parsed_new_york_state_deaths_forecast=json.loads(result_new_york_state_deaths_forecast)

# NORTH CAROLINA STATE DATA:
queries_north_carolina_state_cases= pd.read_sql(f"select * from states_cases where state = 'North Carolina' and NOT state ISNULL and cases != 'N'",conn)
result_north_carolina_state_cases=queries_north_carolina_state_cases.to_json(orient='index')
parsed_north_carolina_state_cases=json.loads(result_north_carolina_state_cases)

queries_north_carolina_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'North Carolina' and NOT state ISNULL and deaths != 'N'",conn)
result_north_carolina_state_deaths=queries_north_carolina_state_deaths.to_json(orient='index')
parsed_north_carolina_state_deaths=json.loads(result_north_carolina_state_deaths)

queries_north_carolina_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'North Carolina' and NOT state ISNULL",conn)
result_north_carolina_state_cases_forecast=queries_north_carolina_state_cases_forecast.to_json(orient='index')
parsed_north_carolina_state_cases_forecast=json.loads(result_north_carolina_state_cases_forecast)

queries_north_carolina_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'North Carolina' and NOT state ISNULL",conn)
result_north_carolina_state_deaths_forecast=queries_north_carolina_state_deaths_forecast.to_json(orient='index')
parsed_north_carolina_state_deaths_forecast=json.loads(result_north_carolina_state_deaths_forecast)

# NORTH DAKOTA STATE DATA:
queries_north_dakota_state_cases= pd.read_sql(f"select * from states_cases where state = 'North Dakota' and NOT state ISNULL and cases != 'N'",conn)
result_north_dakota_state_cases=queries_north_dakota_state_cases.to_json(orient='index')
parsed_north_dakota_state_cases=json.loads(result_north_dakota_state_cases)

queries_north_dakota_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'North Dakota' and NOT state ISNULL and deaths != 'N'",conn)
result_north_dakota_state_deaths=queries_north_dakota_state_deaths.to_json(orient='index')
parsed_north_dakota_state_deaths=json.loads(result_north_dakota_state_deaths)

queries_north_dakota_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'North Dakota' and NOT state ISNULL",conn)
result_north_dakota_state_cases_forecast=queries_north_dakota_state_cases_forecast.to_json(orient='index')
parsed_north_dakota_state_cases_forecast=json.loads(result_north_dakota_state_cases_forecast)

queries_north_dakota_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'North Dakota' and NOT state ISNULL",conn)
result_north_dakota_state_deaths_forecast=queries_north_dakota_state_deaths_forecast.to_json(orient='index')
parsed_north_dakota_state_deaths_forecast=json.loads(result_north_dakota_state_deaths_forecast)

# NORTHERN MARIANA ISLANDS STATE DATA:
queries_northern_mariana_islands_state_cases= pd.read_sql(f"select * from states_cases where state = 'Northern Mariana Islands' and NOT state ISNULL and cases != 'N'",conn)
result_northern_mariana_islands_state_cases=queries_northern_mariana_islands_state_cases.to_json(orient='index')
parsed_northern_mariana_islands_state_cases=json.loads(result_northern_mariana_islands_state_cases)

queries_northern_mariana_islands_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Northern Mariana Islands' and NOT state ISNULL and deaths != 'N'",conn)
result_northern_mariana_islands_state_deaths=queries_northern_mariana_islands_state_deaths.to_json(orient='index')
parsed_northern_mariana_islands_state_deaths=json.loads(result_northern_mariana_islands_state_deaths)

queries_northern_mariana_islands_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Northern Mariana Islands' and NOT state ISNULL",conn)
result_northern_mariana_islands_state_cases_forecast=queries_northern_mariana_islands_state_cases_forecast.to_json(orient='index')
parsed_northern_mariana_islands_state_cases_forecast=json.loads(result_northern_mariana_islands_state_cases_forecast)

queries_northern_mariana_islands_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Northern Mariana Islands' and NOT state ISNULL",conn)
result_northern_mariana_islands_state_deaths_forecast=queries_northern_mariana_islands_state_deaths_forecast.to_json(orient='index')
parsed_northern_mariana_islands_state_deaths_forecast=json.loads(result_northern_mariana_islands_state_deaths_forecast)

# OHIO STATE DATA:
queries_ohio_state_cases= pd.read_sql(f"select * from states_cases where state = 'Ohio' and NOT state ISNULL and cases != 'N'",conn)
result_ohio_state_cases=queries_ohio_state_cases.to_json(orient='index')
parsed_ohio_state_cases=json.loads(result_ohio_state_cases)

queries_ohio_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Ohio' and NOT state ISNULL and deaths != 'N'",conn)
result_ohio_state_deaths=queries_ohio_state_deaths.to_json(orient='index')
parsed_ohio_state_deaths=json.loads(result_ohio_state_deaths)

queries_ohio_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Ohio' and NOT state ISNULL",conn)
result_ohio_state_cases_forecast=queries_ohio_state_cases_forecast.to_json(orient='index')
parsed_ohio_state_cases_forecast=json.loads(result_ohio_state_cases_forecast)

queries_ohio_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Ohio' and NOT state ISNULL",conn)
result_ohio_state_deaths_forecast=queries_ohio_state_deaths_forecast.to_json(orient='index')
parsed_ohio_state_deaths_forecast=json.loads(result_ohio_state_deaths_forecast)

# OKLAHOMA STATE DATA:
queries_oklahoma_state_cases= pd.read_sql(f"select * from states_cases where state = 'Oklahoma' and NOT state ISNULL and cases != 'N'",conn)
result_oklahoma_state_cases=queries_oklahoma_state_cases.to_json(orient='index')
parsed_oklahoma_state_cases=json.loads(result_oklahoma_state_cases)

queries_oklahoma_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Oklahoma' and NOT state ISNULL and deaths != 'N'",conn)
result_oklahoma_state_deaths=queries_oklahoma_state_deaths.to_json(orient='index')
parsed_oklahoma_state_deaths=json.loads(result_oklahoma_state_deaths)

queries_oklahoma_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Oklahoma' and NOT state ISNULL",conn)
result_oklahoma_state_cases_forecast=queries_oklahoma_state_cases_forecast.to_json(orient='index')
parsed_oklahoma_state_cases_forecast=json.loads(result_oklahoma_state_cases_forecast)

queries_oklahoma_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Oklahoma' and NOT state ISNULL",conn)
result_oklahoma_state_deaths_forecast=queries_oklahoma_state_deaths_forecast.to_json(orient='index')
parsed_oklahoma_state_deaths_forecast=json.loads(result_oklahoma_state_deaths_forecast)

# OREGON STATE DATA:
queries_oregon_state_cases= pd.read_sql(f"select * from states_cases where state = 'Oregon' and NOT state ISNULL and cases != 'N'",conn)
result_oregon_state_cases=queries_oregon_state_cases.to_json(orient='index')
parsed_oregon_state_cases=json.loads(result_oregon_state_cases)

queries_oregon_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Oregon' and NOT state ISNULL and deaths != 'N'",conn)
result_oregon_state_deaths=queries_oregon_state_deaths.to_json(orient='index')
parsed_oregon_state_deaths=json.loads(result_oregon_state_deaths)

queries_oregon_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Oregon' and NOT state ISNULL",conn)
result_oregon_state_cases_forecast=queries_oregon_state_cases_forecast.to_json(orient='index')
parsed_oregon_state_cases_forecast=json.loads(result_oregon_state_cases_forecast)

queries_oregon_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Oregon' and NOT state ISNULL",conn)
result_oregon_state_deaths_forecast=queries_oregon_state_deaths_forecast.to_json(orient='index')
parsed_oregon_state_deaths_forecast=json.loads(result_oregon_state_deaths_forecast)

# PENNSYLVANIA STATE DATA:
queries_pennsylvania_state_cases= pd.read_sql(f"select * from states_cases where state = 'Pennsylvania' and NOT state ISNULL and cases != 'N'",conn)
result_pennsylvania_state_cases=queries_pennsylvania_state_cases.to_json(orient='index')
parsed_pennsylvania_state_cases=json.loads(result_pennsylvania_state_cases)

queries_pennsylvania_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Pennsylvania' and NOT state ISNULL and deaths != 'N'",conn)
result_pennsylvania_state_deaths=queries_pennsylvania_state_deaths.to_json(orient='index')
parsed_pennsylvania_state_deaths=json.loads(result_pennsylvania_state_deaths)

queries_pennsylvania_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Pennsylvania' and NOT state ISNULL",conn)
result_pennsylvania_state_cases_forecast=queries_pennsylvania_state_cases_forecast.to_json(orient='index')
parsed_pennsylvania_state_cases_forecast=json.loads(result_pennsylvania_state_cases_forecast)

queries_pennsylvania_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Pennsylvania' and NOT state ISNULL",conn)
result_pennsylvania_state_deaths_forecast=queries_pennsylvania_state_deaths_forecast.to_json(orient='index')
parsed_pennsylvania_state_deaths_forecast=json.loads(result_pennsylvania_state_deaths_forecast)

# PUERTO RICO STATE DATA:
queries_puerto_rico_state_cases= pd.read_sql(f"select * from states_cases where state = 'Puerto Rico' and NOT state ISNULL and cases != 'N'",conn)
result_puerto_rico_state_cases=queries_puerto_rico_state_cases.to_json(orient='index')
parsed_puerto_rico_state_cases=json.loads(result_puerto_rico_state_cases)

queries_puerto_rico_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Puerto Rico' and NOT state ISNULL and deaths != 'N'",conn)
result_puerto_rico_state_deaths=queries_puerto_rico_state_deaths.to_json(orient='index')
parsed_puerto_rico_state_deaths=json.loads(result_puerto_rico_state_deaths)

queries_puerto_rico_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Puerto Rico' and NOT state ISNULL",conn)
result_puerto_rico_state_cases_forecast=queries_puerto_rico_state_cases_forecast.to_json(orient='index')
parsed_puerto_rico_state_cases_forecast=json.loads(result_puerto_rico_state_cases_forecast)

queries_puerto_rico_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Puerto Rico' and NOT state ISNULL",conn)
result_puerto_rico_state_deaths_forecast=queries_puerto_rico_state_deaths_forecast.to_json(orient='index')
parsed_puerto_rico_state_deaths_forecast=json.loads(result_puerto_rico_state_deaths_forecast)

# RHODE ISLAND STATE DATA:
queries_rhode_island_state_cases= pd.read_sql(f"select * from states_cases where state = 'Rhode Island' and NOT state ISNULL and cases != 'N'",conn)
result_rhode_island_state_cases=queries_rhode_island_state_cases.to_json(orient='index')
parsed_rhode_island_state_cases=json.loads(result_rhode_island_state_cases)

queries_rhode_island_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Rhode Island' and NOT state ISNULL and deaths != 'N'",conn)
result_rhode_island_state_deaths=queries_rhode_island_state_deaths.to_json(orient='index')
parsed_rhode_island_state_deaths=json.loads(result_rhode_island_state_deaths)

queries_rhode_island_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Rhode Island' and NOT state ISNULL",conn)
result_rhode_island_state_cases_forecast=queries_rhode_island_state_cases_forecast.to_json(orient='index')
parsed_rhode_island_state_cases_forecast=json.loads(result_rhode_island_state_cases_forecast)

queries_rhode_island_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Rhode Island' and NOT state ISNULL",conn)
result_rhode_island_state_deaths_forecast=queries_rhode_island_state_deaths_forecast.to_json(orient='index')
parsed_rhode_island_state_deaths_forecast=json.loads(result_rhode_island_state_deaths_forecast)

# SOUTH CAROLINA STATE DATA:
queries_south_carolina_state_cases= pd.read_sql(f"select * from states_cases where state = 'South Carolina' and NOT state ISNULL and cases != 'N'",conn)
result_south_carolina_state_cases=queries_south_carolina_state_cases.to_json(orient='index')
parsed_south_carolina_state_cases=json.loads(result_south_carolina_state_cases)

queries_south_carolina_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'South Carolina' and NOT state ISNULL and deaths != 'N'",conn)
result_south_carolina_state_deaths=queries_south_carolina_state_deaths.to_json(orient='index')
parsed_south_carolina_state_deaths=json.loads(result_south_carolina_state_deaths)

queries_south_carolina_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'South Carolina' and NOT state ISNULL",conn)
result_south_carolina_state_cases_forecast=queries_south_carolina_state_cases_forecast.to_json(orient='index')
parsed_south_carolina_state_cases_forecast=json.loads(result_south_carolina_state_cases_forecast)

queries_south_carolina_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'South Carolina' and NOT state ISNULL",conn)
result_south_carolina_state_deaths_forecast=queries_south_carolina_state_deaths_forecast.to_json(orient='index')
parsed_south_carolina_state_deaths_forecast=json.loads(result_south_carolina_state_deaths_forecast)

# SOUTH DAKOTA STATE DATA:
queries_south_dakota_state_cases= pd.read_sql(f"select * from states_cases where state = 'South Dakota' and NOT state ISNULL and cases != 'N'",conn)
result_south_dakota_state_cases=queries_south_dakota_state_cases.to_json(orient='index')
parsed_south_dakota_state_cases=json.loads(result_south_dakota_state_cases)

queries_south_dakota_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'South Dakota' and NOT state ISNULL and deaths != 'N'",conn)
result_south_dakota_state_deaths=queries_south_dakota_state_deaths.to_json(orient='index')
parsed_south_dakota_state_deaths=json.loads(result_south_dakota_state_deaths)

queries_south_dakota_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'South Dakota' and NOT state ISNULL",conn)
result_south_dakota_state_cases_forecast=queries_south_dakota_state_cases_forecast.to_json(orient='index')
parsed_south_dakota_state_cases_forecast=json.loads(result_south_dakota_state_cases_forecast)

queries_south_dakota_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'South Dakota' and NOT state ISNULL",conn)
result_south_dakota_state_deaths_forecast=queries_south_dakota_state_deaths_forecast.to_json(orient='index')
parsed_south_dakota_state_deaths_forecast=json.loads(result_south_dakota_state_deaths_forecast)

# TENNESSEE STATE DATA:
queries_tennessee_state_cases= pd.read_sql(f"select * from states_cases where state = 'Tennessee' and NOT state ISNULL and cases != 'N'",conn)
result_tennessee_state_cases=queries_tennessee_state_cases.to_json(orient='index')
parsed_tennessee_state_cases=json.loads(result_tennessee_state_cases)

queries_tennessee_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Tennessee' and NOT state ISNULL and deaths != 'N'",conn)
result_tennessee_state_deaths=queries_tennessee_state_deaths.to_json(orient='index')
parsed_tennessee_state_deaths=json.loads(result_tennessee_state_deaths)

queries_tennessee_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Tennessee' and NOT state ISNULL",conn)
result_tennessee_state_cases_forecast=queries_tennessee_state_cases_forecast.to_json(orient='index')
parsed_tennessee_state_cases_forecast=json.loads(result_tennessee_state_cases_forecast)

queries_tennessee_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Tennessee' and NOT state ISNULL",conn)
result_tennessee_state_deaths_forecast=queries_tennessee_state_deaths_forecast.to_json(orient='index')
parsed_tennessee_state_deaths_forecast=json.loads(result_tennessee_state_deaths_forecast)

# TEXAS STATE DATA:
queries_texas_state_cases= pd.read_sql(f"select * from states_cases where state = 'Texas' and NOT state ISNULL and cases != 'N'",conn)
result_texas_state_cases=queries_texas_state_cases.to_json(orient='index')
parsed_texas_state_cases=json.loads(result_texas_state_cases)

queries_texas_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Texas' and NOT state ISNULL and deaths != 'N'",conn)
result_texas_state_deaths=queries_texas_state_deaths.to_json(orient='index')
parsed_texas_state_deaths=json.loads(result_texas_state_deaths)

queries_texas_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Texas' and NOT state ISNULL",conn)
result_texas_state_cases_forecast=queries_texas_state_cases_forecast.to_json(orient='index')
parsed_texas_state_cases_forecast=json.loads(result_texas_state_cases_forecast)

queries_texas_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Texas' and NOT state ISNULL",conn)
result_texas_state_deaths_forecast=queries_texas_state_deaths_forecast.to_json(orient='index')
parsed_texas_state_deaths_forecast=json.loads(result_texas_state_deaths_forecast)

# UTAH STATE DATA:
queries_utah_state_cases= pd.read_sql(f"select * from states_cases where state = 'Utah' and NOT state ISNULL and cases != 'N'",conn)
result_utah_state_cases=queries_utah_state_cases.to_json(orient='index')
parsed_utah_state_cases=json.loads(result_utah_state_cases)

queries_utah_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Utah' and NOT state ISNULL and deaths != 'N'",conn)
result_utah_state_deaths=queries_utah_state_deaths.to_json(orient='index')
parsed_utah_state_deaths=json.loads(result_utah_state_deaths)

queries_utah_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Utah' and NOT state ISNULL",conn)
result_utah_state_cases_forecast=queries_utah_state_cases_forecast.to_json(orient='index')
parsed_utah_state_cases_forecast=json.loads(result_utah_state_cases_forecast)

queries_utah_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Utah' and NOT state ISNULL",conn)
result_utah_state_deaths_forecast=queries_utah_state_deaths_forecast.to_json(orient='index')
parsed_utah_state_deaths_forecast=json.loads(result_utah_state_deaths_forecast)

# VERMONT STATE DATA:
queries_vermont_state_cases= pd.read_sql(f"select * from states_cases where state = 'Vermont' and NOT state ISNULL and cases != 'N'",conn)
result_vermont_state_cases=queries_vermont_state_cases.to_json(orient='index')
parsed_vermont_state_cases=json.loads(result_vermont_state_cases)

queries_vermont_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Vermont' and NOT state ISNULL and deaths != 'N'",conn)
result_vermont_state_deaths=queries_vermont_state_deaths.to_json(orient='index')
parsed_vermont_state_deaths=json.loads(result_vermont_state_deaths)

queries_vermont_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Vermont' and NOT state ISNULL",conn)
result_vermont_state_cases_forecast=queries_vermont_state_cases_forecast.to_json(orient='index')
parsed_vermont_state_cases_forecast=json.loads(result_vermont_state_cases_forecast)

queries_vermont_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Vermont' and NOT state ISNULL",conn)
result_vermont_state_deaths_forecast=queries_vermont_state_deaths_forecast.to_json(orient='index')
parsed_vermont_state_deaths_forecast=json.loads(result_vermont_state_deaths_forecast)

# VIRGIN ISLANDS STATE DATA:
queries_virgin_islands_state_cases= pd.read_sql(f"select * from states_cases where state = 'Virgin Islands' and NOT state ISNULL and cases != 'N'",conn)
result_virgin_islands_state_cases=queries_virgin_islands_state_cases.to_json(orient='index')
parsed_virgin_islands_state_cases=json.loads(result_virgin_islands_state_cases)

queries_virgin_islands_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Virgin Islands' and NOT state ISNULL and deaths != 'N'",conn)
result_virgin_islands_state_deaths=queries_virgin_islands_state_deaths.to_json(orient='index')
parsed_virgin_islands_state_deaths=json.loads(result_virgin_islands_state_deaths)

queries_virgin_islands_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Virgin Islands' and NOT state ISNULL",conn)
result_virgin_islands_state_cases_forecast=queries_virgin_islands_state_cases_forecast.to_json(orient='index')
parsed_virgin_islands_state_cases_forecast=json.loads(result_virgin_islands_state_cases_forecast)

queries_virgin_islands_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Virgin Islands' and NOT state ISNULL",conn)
result_virgin_islands_state_deaths_forecast=queries_virgin_islands_state_deaths_forecast.to_json(orient='index')
parsed_virgin_islands_state_deaths_forecast=json.loads(result_virgin_islands_state_deaths_forecast)

# VIRGINIA STATE DATA:
queries_virginia_state_cases= pd.read_sql(f"select * from states_cases where state = 'Virginia' and NOT state ISNULL and cases != 'N'",conn)
result_virginia_state_cases=queries_virginia_state_cases.to_json(orient='index')
parsed_virginia_state_cases=json.loads(result_virginia_state_cases)

queries_virginia_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Virginia' and NOT state ISNULL and deaths != 'N'",conn)
result_virginia_state_deaths=queries_virginia_state_deaths.to_json(orient='index')
parsed_virginia_state_deaths=json.loads(result_virginia_state_deaths)

queries_virginia_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Virginia' and NOT state ISNULL",conn)
result_virginia_state_cases_forecast=queries_virginia_state_cases_forecast.to_json(orient='index')
parsed_virginia_state_cases_forecast=json.loads(result_virginia_state_cases_forecast)

queries_virginia_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Virginia' and NOT state ISNULL",conn)
result_virginia_state_deaths_forecast=queries_virginia_state_deaths_forecast.to_json(orient='index')
parsed_virginia_state_deaths_forecast=json.loads(result_virginia_state_deaths_forecast)

# WASHINGTON STATE DATA:
queries_washington_state_cases= pd.read_sql(f"select * from states_cases where state = 'Washington' and NOT state ISNULL and cases != 'N'",conn)
result_washington_state_cases=queries_washington_state_cases.to_json(orient='index')
parsed_washington_state_cases=json.loads(result_washington_state_cases)

queries_washington_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Washington' and NOT state ISNULL and deaths != 'N'",conn)
result_washington_state_deaths=queries_washington_state_deaths.to_json(orient='index')
parsed_washington_state_deaths=json.loads(result_washington_state_deaths)

queries_washington_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Washington' and NOT state ISNULL",conn)
result_washington_state_cases_forecast=queries_washington_state_cases_forecast.to_json(orient='index')
parsed_washington_state_cases_forecast=json.loads(result_washington_state_cases_forecast)

queries_washington_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Washington' and NOT state ISNULL",conn)
result_washington_state_deaths_forecast=queries_washington_state_deaths_forecast.to_json(orient='index')
parsed_washington_state_deaths_forecast=json.loads(result_washington_state_deaths_forecast)

# WEST VIRGINIA STATE DATA:
queries_west_virginia_state_cases= pd.read_sql(f"select * from states_cases where state = 'West Virginia' and NOT state ISNULL and cases != 'N'",conn)
result_west_virginia_state_cases=queries_west_virginia_state_cases.to_json(orient='index')
parsed_west_virginia_state_cases=json.loads(result_west_virginia_state_cases)

queries_west_virginia_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'West Virginia' and NOT state ISNULL and deaths != 'N'",conn)
result_west_virginia_state_deaths=queries_west_virginia_state_deaths.to_json(orient='index')
parsed_west_virginia_state_deaths=json.loads(result_west_virginia_state_deaths)

queries_west_virginia_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'West Virginia' and NOT state ISNULL",conn)
result_west_virginia_state_cases_forecast=queries_west_virginia_state_cases_forecast.to_json(orient='index')
parsed_west_virginia_state_cases_forecast=json.loads(result_west_virginia_state_cases_forecast)

queries_west_virginia_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'West Virginia' and NOT state ISNULL",conn)
result_west_virginia_state_deaths_forecast=queries_west_virginia_state_deaths_forecast.to_json(orient='index')
parsed_west_virginia_state_deaths_forecast=json.loads(result_west_virginia_state_deaths_forecast)

# WISCONSIN STATE DATA:
queries_wisconsin_state_cases= pd.read_sql(f"select * from states_cases where state = 'Wisconsin' and NOT state ISNULL and cases != 'N'",conn)
result_wisconsin_state_cases=queries_wisconsin_state_cases.to_json(orient='index')
parsed_wisconsin_state_cases=json.loads(result_wisconsin_state_cases)

queries_wisconsin_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Wisconsin' and NOT state ISNULL and deaths != 'N'",conn)
result_wisconsin_state_deaths=queries_wisconsin_state_deaths.to_json(orient='index')
parsed_wisconsin_state_deaths=json.loads(result_wisconsin_state_deaths)

queries_wisconsin_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Wisconsin' and NOT state ISNULL",conn)
result_wisconsin_state_cases_forecast=queries_wisconsin_state_cases_forecast.to_json(orient='index')
parsed_wisconsin_state_cases_forecast=json.loads(result_wisconsin_state_cases_forecast)

queries_wisconsin_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Wisconsin' and NOT state ISNULL",conn)
result_wisconsin_state_deaths_forecast=queries_wisconsin_state_deaths_forecast.to_json(orient='index')
parsed_wisconsin_state_deaths_forecast=json.loads(result_wisconsin_state_deaths_forecast)

# WYOMING STATE DATA:
queries_wyoming_state_cases= pd.read_sql(f"select * from states_cases where state = 'Wyoming' and NOT state ISNULL and cases != 'N'",conn)
result_wyoming_state_cases=queries_wyoming_state_cases.to_json(orient='index')
parsed_wyoming_state_cases=json.loads(result_wyoming_state_cases)

queries_wyoming_state_deaths= pd.read_sql(f"select * from states_deaths where state = 'Wyoming' and NOT state ISNULL and deaths != 'N'",conn)
result_wyoming_state_deaths=queries_wyoming_state_deaths.to_json(orient='index')
parsed_wyoming_state_deaths=json.loads(result_wyoming_state_deaths)

queries_wyoming_state_cases_forecast= pd.read_sql(f"select * from states_cases_forecast where state = 'Wyoming' and NOT state ISNULL",conn)
result_wyoming_state_cases_forecast=queries_wyoming_state_cases_forecast.to_json(orient='index')
parsed_wyoming_state_cases_forecast=json.loads(result_wyoming_state_cases_forecast)

queries_wyoming_state_deaths_forecast= pd.read_sql(f"select * from states_deaths_forecast where state = 'Wyoming' and NOT state ISNULL",conn)
result_wyoming_state_deaths_forecast=queries_wyoming_state_deaths_forecast.to_json(orient='index')
parsed_wyoming_state_deaths_forecast=json.loads(result_wyoming_state_deaths_forecast)

#Routes
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/usa_cases_today")
def usa_cases_today():
    return jsonify(parsed_cases_states_today)

@app.route("/usa_deaths_today")
def usa_deaths_today():
    return jsonify(parsed_deaths_states_today)

@app.route("/usa_cases_all")
def usa_cases_all():
    return jsonify(parsed_cases_states_full)

@app.route("/usa_deaths_all")
def usa_deaths_all():
    return jsonify(parsed_deaths_states_full)


@app.route("/us_overall_today")
def us_overall():
    return jsonify(parsed_us_today)



# ALABAMA ROUTES
@app.route(f'/Alabama_cases')
def alabama_cases():
    return jsonify(parsed_alabama_state_cases)

@app.route(f'/Alabama_deaths')
def alabama_deaths():
    return jsonify(parsed_alabama_state_deaths)

@app.route(f'/Alabama_cases_forecast')
def alabama_cases_forecast():
    return jsonify(parsed_alabama_state_cases_forecast)

@app.route(f'/Alabama_deaths_forecast')
def alabama_deaths_forecast():
    return jsonify(parsed_alabama_state_deaths_forecast)



# ALASKA ROUTES
@app.route(f'/Alaska_cases')
def alaska_cases():
    return jsonify(parsed_alaska_state_cases)

@app.route(f'/Alaska_deaths')
def alaska_deaths():
    return jsonify(parsed_alaska_state_deaths)

@app.route(f'/Alaska_cases_forecast')
def alaska_cases_forecast():
    return jsonify(parsed_alaska_state_cases_forecast)

@app.route(f'/Alaska_deaths_forecast')
def alaska_deaths_forecast():
    return jsonify(parsed_alaska_state_deaths_forecast)


# ARIZONA ROUTES
@app.route(f'/Arizona_cases')
def arizona_cases():
    return jsonify(parsed_arizona_state_cases)

@app.route(f'/Arizona_deaths')
def arizona_deaths():
    return jsonify(parsed_arizona_state_deaths)

@app.route(f'/Arizona_cases_forecast')
def arizona_cases_forecast():
    return jsonify(parsed_arizona_state_cases_forecast)

@app.route(f'/Arizona_deaths_forecast')
def arizona_deaths_forecast():
    return jsonify(parsed_arizona_state_deaths_forecast)



# ARKANSAS ROUTES
@app.route(f'/Arkansas_cases')
def arkansas_cases():
    return jsonify(parsed_arkansas_state_cases)

@app.route(f'/Arkansas_deaths')
def arkansas_deaths():
    return jsonify(parsed_arkansas_state_deaths)

@app.route(f'/Arkansas_cases_forecast')
def arkansas_cases_forecast():
    return jsonify(parsed_arkansas_state_cases_forecast)

@app.route(f'/Arkansas_deaths_forecast')
def arkansas_deaths_forecast():
    return jsonify(parsed_arkansas_state_deaths_forecast)



# CALIFORNIA ROUTES
@app.route(f'/California_cases')
def california_cases():
    return jsonify(parsed_california_state_cases)

@app.route(f'/California_deaths')
def california_deaths():
    return jsonify(parsed_california_state_deaths)

@app.route(f'/California_cases_forecast')
def california_cases_forecast():
    return jsonify(parsed_california_state_cases_forecast)

@app.route(f'/California_deaths_forecast')
def california_deaths_forecast():
    return jsonify(parsed_california_state_deaths_forecast)



# COLORADO ROUTES
@app.route(f'/Colorado_cases')
def colorado_cases():
    return jsonify(parsed_colorado_state_cases)

@app.route(f'/Colorado_deaths')
def colorado_deaths():
    return jsonify(parsed_colorado_state_deaths)

# COLORADO ROUTES
@app.route(f'/Colorado_cases_forecast')
def colorado_cases_forecast():
    return jsonify(parsed_colorado_state_cases_forecast)

@app.route(f'/Colorado_deaths_forecast')
def colorado_deaths_forecast():
    return jsonify(parsed_colorado_state_deaths_forecast)



# CONNECTICUT ROUTES
@app.route(f'/Connecticut_cases')
def connecticut_cases():
    return jsonify(parsed_connecticut_state_cases)

@app.route(f'/Connecticut_deaths')
def connecticut_deaths():
    return jsonify(parsed_connecticut_state_deaths)

@app.route(f'/Connecticut_cases_forecast')
def connecticut_case_forecast():
    return jsonify(parsed_connecticut_state_cases_forecast)

@app.route(f'/Connecticut_deaths_forecast')
def connecticut_deaths_forecast():
    return jsonify(parsed_connecticut_state_deaths_forecast)


# DELAWARE ROUTES
@app.route(f'/Delaware_cases')
def delaware_cases():
    return jsonify(parsed_delaware_state_cases)

@app.route(f'/Delaware_deaths')
def delaware_deaths():
    return jsonify(parsed_delaware_state_deaths)

@app.route(f'/Delaware_cases_forecast')
def delaware_cases_forecast():
    return jsonify(parsed_delaware_state_cases_forecast)

@app.route(f'/Delaware_deaths_forecast')
def delaware_deaths_forecast():
    return jsonify(parsed_delaware_state_deaths_forecast)    



# DISTRICT OF COLUMBIA ROUTES
@app.route(f'/District of Columbia_cases')
def dc_cases():
    return jsonify(parsed_dc_state_cases)

@app.route(f'/District of Columbia_deaths')
def dc_deaths():
    return jsonify(parsed_dc_state_deaths)

@app.route(f'/District of Columbia_cases_forecast')
def dc_cases_forecast():
    return jsonify(parsed_dc_state_cases_forecast)

@app.route(f'/District of Columbia_deaths_forecast')
def dc_deaths_forecast():
    return jsonify(parsed_dc_state_deaths_forecast)



# FLORIDA ROUTES
@app.route(f'/Florida_cases')
def florida_cases():
    return jsonify(parsed_florida_state_cases)

@app.route(f'/Florida_deaths')
def florida_deaths():
    return jsonify(parsed_florida_state_deaths)

@app.route(f'/Florida_cases_forecast')
def florida_cases_forecast():
    return jsonify(parsed_florida_state_cases_forecast)

@app.route(f'/Florida_deaths_forecast')
def florida_deaths_forecast():
    return jsonify(parsed_florida_state_deaths_forecast)



# GEORGIA ROUTES
@app.route(f'/Georgia_cases')
def georgia_cases():
    return jsonify(parsed_georgia_state_cases)

@app.route(f'/Georgia_deaths')
def georgia_deaths():
    return jsonify(parsed_georgia_state_deaths)

@app.route(f'/Georgia_cases_forecast')
def georgia_cases_forecast():
    return jsonify(parsed_georgia_state_cases_forecast)

@app.route(f'/Georgia_deaths_forecast')
def georgia_deaths_forecast():
    return jsonify(parsed_georgia_state_deaths_forecast)



# GUAM ROUTES
@app.route(f'/Guam_cases')
def guam_cases():
    return jsonify(parsed_guam_state_cases)

@app.route(f'/Guam_deaths')
def guam_deaths():
    return jsonify(parsed_guam_state_deaths)

@app.route(f'/Guam_cases_forecast')
def guam_cases_forecast():
    return jsonify(parsed_guam_state_cases_forecast)

@app.route(f'/Guam_deaths_forecast')
def guam_deaths_forecast():
    return jsonify(parsed_guam_state_deaths_forecast)



# HAWAII ROUTES
@app.route(f'/Hawaii_cases')
def hawaii_cases():
    return jsonify(parsed_hawaii_state_cases)

@app.route(f'/Hawaii_deaths')
def hawaii_deaths():
    return jsonify(parsed_hawaii_state_deaths)

@app.route(f'/Hawaii_cases_forecast')
def hawaii_cases_forecast():
    return jsonify(parsed_hawaii_state_cases_forecast)

@app.route(f'/Hawaii_deaths_forecast')
def hawaii_deaths_forecast():
    return jsonify(parsed_hawaii_state_deaths_forecast)



# IDAHO ROUTES
@app.route(f'/Idaho_cases')
def idaho_cases():
    return jsonify(parsed_idaho_state_cases)

@app.route(f'/Idaho_deaths')
def idaho_deaths():
    return jsonify(parsed_idaho_state_deaths)

@app.route(f'/Idaho_cases_forecast')
def idaho_cases_forecast():
    return jsonify(parsed_idaho_state_cases_forecast)

@app.route(f'/Idaho_deaths_forecast')
def idaho_deaths_forecast():
    return jsonify(parsed_idaho_state_deaths_forecast)



# ILLINOIS ROUTES
@app.route(f'/Illinois_cases')
def illinois_cases():
    return jsonify(parsed_illinois_state_cases)

@app.route(f'/Illinois_deaths')
def illinois_deaths():
    return jsonify(parsed_illinois_state_deaths)

@app.route(f'/Illinois_cases_forecast')
def illinois_cases_forecast():
    return jsonify(parsed_illinois_state_cases_forecast)

@app.route(f'/Illinois_deaths_forecast')
def illinois_deaths_forecast():
    return jsonify(parsed_illinois_state_deaths_forecast)




# INDIANA ROUTES
@app.route(f'/Indiana_cases')
def indiana_cases():
    return jsonify(parsed_indiana_state_cases)

@app.route(f'/Indiana_deaths')
def indiana_deaths():
    return jsonify(parsed_indiana_state_deaths)

@app.route(f'/Indiana_cases_forecast')
def indiana_cases_forecast():
    return jsonify(parsed_indiana_state_cases_forecast)

@app.route(f'/Indiana_deaths_forecast')
def indiana_deaths_forecast():
    return jsonify(parsed_indiana_state_deaths_forecast)



# IOWA ROUTES
@app.route(f'/Iowa_cases')
def iowa_cases():
    return jsonify(parsed_iowa_state_cases)

@app.route(f'/Iowa_deaths')
def iowa_deaths():
    return jsonify(parsed_iowa_state_deaths)

@app.route(f'/Iowa_cases_forecast')
def iowa_cases_forecast():
    return jsonify(parsed_iowa_state_cases_forecast)

@app.route(f'/Iowa_deaths_forecast')
def iowa_deaths_forecast():
    return jsonify(parsed_iowa_state_deaths_forecast)



# KANSAS ROUTES
@app.route(f'/Kansas_cases')
def kansas_cases():
    return jsonify(parsed_kansas_state_cases)

@app.route(f'/Kansas_deaths')
def kansas_deaths():
    return jsonify(parsed_kansas_state_deaths)

@app.route(f'/Kansas_cases_forecast')
def kansas_cases_forecast():
    return jsonify(parsed_kansas_state_cases_forecast)

@app.route(f'/Kansas_deaths_forecast')
def kansas_deaths_forecast():
    return jsonify(parsed_kansas_state_deaths_forecast)



# KENTUCKY ROUTES
@app.route(f'/Kentucky_cases')
def kentucky_cases():
    return jsonify(parsed_kentucky_state_cases)

@app.route(f'/Kentucky_deaths')
def kentucky_deaths():
    return jsonify(parsed_kentucky_state_deaths)

@app.route(f'/Kentucky_cases_forecast')
def kentucky_cases_forecast():
    return jsonify(parsed_kentucky_state_cases_forecast)

@app.route(f'/Kentucky_deaths_forecast')
def kentucky_deaths_forecast():
    return jsonify(parsed_kentucky_state_deaths_forecast)



# LOUISIANA ROUTES
@app.route(f'/Louisiana_cases')
def louisiana_cases():
    return jsonify(parsed_louisiana_state_cases)

@app.route(f'/Louisiana_deaths')
def louisiana_deaths():
    return jsonify(parsed_louisiana_state_deaths)

@app.route(f'/Louisiana_cases_forecast')
def louisiana_cases_forecast():
    return jsonify(parsed_louisiana_state_cases_forecast)

@app.route(f'/Louisiana_deaths_forecast')
def louisiana_deaths_forecast():
    return jsonify(parsed_louisiana_state_deaths_forecast)



# MAINE ROUTES
@app.route(f'/Maine_cases')
def maine_cases():
    return jsonify(parsed_maine_state_cases)

@app.route(f'/Maine_deaths')
def maine_deaths():
    return jsonify(parsed_maine_state_deaths)

@app.route(f'/Maine_cases_forecast')
def maine_cases_forecast():
    return jsonify(parsed_maine_state_cases_forecast)

@app.route(f'/Maine_deaths_forecast')
def maine_deaths_forecast():
    return jsonify(parsed_maine_state_deaths_forecast)



# MARYLAND ROUTES
@app.route(f'/Maryland_cases')
def maryland_cases():
    return jsonify(parsed_maryland_state_cases)

@app.route(f'/Maryland_deaths')
def maryland_deaths():
    return jsonify(parsed_maryland_state_deaths)

@app.route(f'/Maryland_cases_forecast')
def maryland_cases_forecast():
    return jsonify(parsed_maryland_state_cases_forecast)

@app.route(f'/Maryland_deaths_forecast')
def maryland_deaths_forecast():
    return jsonify(parsed_maryland_state_deaths_forecast)



# MASSACHUSETTS ROUTES
@app.route(f'/Massachusetts_cases')
def massachusetts_cases():
    return jsonify(parsed_massachusetts_state_cases)

@app.route(f'/Massachusetts_deaths')
def massachusetts_deaths():
    return jsonify(parsed_massachusetts_state_deaths)

@app.route(f'/Massachusetts_cases_forecast')
def massachusetts_cases_forecast():
    return jsonify(parsed_massachusetts_state_cases_forecast)

@app.route(f'/Massachusetts_deaths_forecast')
def massachusetts_deaths_forecast():
    return jsonify(parsed_massachusetts_state_deaths_forecast)



# MICHIGAN ROUTES
@app.route(f'/Michigan_cases')
def michigan_cases():
    return jsonify(parsed_michigan_state_cases)

@app.route(f'/Michigan_deaths')
def michigan_deaths():
    return jsonify(parsed_michigan_state_deaths)

@app.route(f'/Michigan_cases_forecast')
def michigan_cases_forecast():
    return jsonify(parsed_michigan_state_cases_forecast)

@app.route(f'/Michigan_deaths_forecast')
def michigan_deaths_forecast():
    return jsonify(parsed_michigan_state_deaths_forecast)



# MINNESOTA ROUTES
@app.route(f'/Minnesota_cases')
def minnesota_cases():
    return jsonify(parsed_minnesota_state_cases)

@app.route(f'/Minnesota_deaths')
def minnesota_deaths():
    return jsonify(parsed_minnesota_state_deaths)

@app.route(f'/Minnesota_cases_forecast')
def minnesota_cases_forecast():
    return jsonify(parsed_minnesota_state_cases_forecast)

@app.route(f'/Minnesota_deaths_forecast')
def minnesota_deaths_forecast():
    return jsonify(parsed_minnesota_state_deaths_forecast)



# MISSISSIPPI ROUTES
@app.route(f'/Mississippi_cases')
def mississippi_cases():
    return jsonify(parsed_mississippi_state_cases)

@app.route(f'/Mississippi_deaths')
def mississippi_deaths():
    return jsonify(parsed_mississippi_state_deaths)

@app.route(f'/Mississippi_cases_forecast')
def mississippi_cases_forecast():
    return jsonify(parsed_mississippi_state_cases_forecast)

@app.route(f'/Mississippi_deaths_forecast')
def mississippi_deaths_forecast():
    return jsonify(parsed_mississippi_state_deaths_forecast)



# MISSOURI ROUTES
@app.route(f'/Missouri_cases')
def missouri_cases():
    return jsonify(parsed_missouri_state_cases)

@app.route(f'/Missouri_deaths')
def missouri_deaths():
    return jsonify(parsed_missouri_state_deaths)

@app.route(f'/Missouri_cases_forecast')
def missouri_cases_forecast():
    return jsonify(parsed_missouri_state_cases_forecast)

@app.route(f'/Missouri_deaths_forecast')
def missouri_deaths_forecast():
    return jsonify(parsed_missouri_state_deaths_forecast)



# MONTANA ROUTES
@app.route(f'/Montana_cases')
def montana_cases():
    return jsonify(parsed_montana_state_cases)

@app.route(f'/Montana_deaths')
def montana_deaths():
    return jsonify(parsed_montana_state_deaths)

@app.route(f'/Montana_cases_forecast')
def montana_cases_forecast():
    return jsonify(parsed_montana_state_cases_forecast)

@app.route(f'/Montana_deaths_forecast')
def montana_deaths_forecast():
    return jsonify(parsed_montana_state_deaths_forecast)




# NEBRASKA ROUTES
@app.route(f'/Nebraska_cases')
def nebraska_cases():
    return jsonify(parsed_nebraska_state_cases)

@app.route(f'/Nebraska_deaths')
def nebraska_deaths():
    return jsonify(parsed_nebraska_state_deaths)

@app.route(f'/Nebraska_cases_forecast')
def nebraska_cases_forecast():
    return jsonify(parsed_nebraska_state_cases_forecast)

@app.route(f'/Nebraska_deaths_forecast')
def nebraska_deaths_forecast():
    return jsonify(parsed_nebraska_state_deaths_forecast)




# NEVADA ROUTES
@app.route(f'/Nevada_cases')
def nevada_cases():
    return jsonify(parsed_nevada_state_cases)

@app.route(f'/Nevada_deaths')
def nevada_deaths():
    return jsonify(parsed_nevada_state_deaths)

@app.route(f'/Nevada_cases_forecast')
def nevada_cases_forecast():
    return jsonify(parsed_nevada_state_cases_forecast)

@app.route(f'/Nevada_deaths_forecast')
def nevada_deaths_forecast():
    return jsonify(parsed_nevada_state_deaths_forecast)



# NEW HAMPSHIRE ROUTES
@app.route(f'/New Hampshire_cases')
def new_hampshire_cases():
    return jsonify(parsed_new_hampshire_state_cases)

@app.route(f'/New Hampshire_deaths')
def new_hampshire_deaths():
    return jsonify(parsed_new_hampshire_state_deaths)

@app.route(f'/New Hampshire_cases_forecast')
def new_hampshire_cases_forecast():
    return jsonify(parsed_new_hampshire_state_cases_forecast)

@app.route(f'/New Hampshire_deaths_forecast')
def new_hampshire_deaths_forecast():
    return jsonify(parsed_new_hampshire_state_deaths_forecast)




# NEW JERSEY ROUTES
@app.route(f'/New Jersey_cases')
def new_jersey_cases():
    return jsonify(parsed_new_jersey_state_cases)

@app.route(f'/New Jersey_deaths')
def new_jersey_deaths():
    return jsonify(parsed_new_jersey_state_deaths)

@app.route(f'/New Jersey_cases_forecast')
def new_jersey_cases_forecast():
    return jsonify(parsed_new_jersey_state_cases_forecast)

@app.route(f'/New Jersey_deaths_forecast')
def new_jersey_deaths_forecast():
    return jsonify(parsed_new_jersey_state_deaths_forecast)



# NEW MEXICO ROUTES
@app.route(f'/New Mexico_cases')
def new_mexico_cases():
    return jsonify(parsed_new_mexico_state_cases)

@app.route(f'/New Mexico_deaths')
def new_mexico_deaths():
    return jsonify(parsed_new_mexico_state_deaths)

@app.route(f'/New Mexico_cases_forecast')
def new_mexico_cases_forecast():
    return jsonify(parsed_new_mexico_state_cases_forecast)

@app.route(f'/New Mexico_deaths_forecast')
def new_mexico_deaths_forecast():
    return jsonify(parsed_new_mexico_state_deaths_forecast)



# NEW YORK ROUTES
@app.route(f'/New York_cases')
def new_york_cases():
    return jsonify(parsed_new_york_state_cases)

@app.route(f'/New York_deaths')
def new_york_deaths():
    return jsonify(parsed_new_york_state_deaths)

@app.route(f'/New York_cases_forecast')
def new_york_cases_forecast():
    return jsonify(parsed_new_york_state_cases_forecast)

@app.route(f'/New York_deaths_forecast')
def new_york_deaths_forecast():
    return jsonify(parsed_new_york_state_deaths_forecast)



# NORTH CAROLINA ROUTES
@app.route(f'/North Carolina_cases')
def north_carolina_cases():
    return jsonify(parsed_north_carolina_state_cases)

@app.route(f'/North Carolina_deaths')
def north_carolina_deaths():
    return jsonify(parsed_north_carolina_state_deaths)

@app.route(f'/North Carolina_cases_forecast')
def north_carolina_cases_forecast():
    return jsonify(parsed_north_carolina_state_cases_forecast)

@app.route(f'/North Carolina_deaths_forecast')
def north_carolina_deaths_forecast():
    return jsonify(parsed_north_carolina_state_deaths_forecast)



# NORTH DAKOTA ROUTES
@app.route(f'/North Dakota_cases')
def north_dakota_cases():
    return jsonify(parsed_north_dakota_state_cases)

@app.route(f'/North Dakota_deaths')
def north_dakota_deaths():
    return jsonify(parsed_north_dakota_state_deaths)

@app.route(f'/North Dakota_cases_forecast')
def north_dakota_cases_forecast():
    return jsonify(parsed_north_dakota_state_cases_forecast)

@app.route(f'/North Dakota_deaths_forecast')
def north_dakota_deaths_forecast():
    return jsonify(parsed_north_dakota_state_deaths_forecast)



# NORTHERN MARIANA ISLANDS ROUTES
@app.route(f'/Northern Mariana Islands_cases')
def northern_mariana_islands_cases():
    return jsonify(parsed_northern_mariana_islands_state_cases)

@app.route(f'/Northern Mariana Islands_deaths')
def northern_mariana_islands_deaths():
    return jsonify(parsed_northern_mariana_islands_state_deaths)

@app.route(f'/Northern Mariana Islands_cases_forecast')
def northern_mariana_islands_cases_forecast():
    return jsonify(parsed_northern_mariana_islands_state_cases_forecast)

@app.route(f'/Northern Mariana Islands_deaths_forecast')
def northern_mariana_islands_deaths_forecast():
    return jsonify(parsed_northern_mariana_islands_state_deaths_forecast)



# OHIO ROUTES
@app.route(f'/Ohio_cases')
def ohio_cases():
    return jsonify(parsed_ohio_state_cases)

@app.route(f'/Ohio_deaths')
def ohio_deaths():
    return jsonify(parsed_ohio_state_deaths)

@app.route(f'/Ohio_cases_forecast')
def ohio_cases_forecast():
    return jsonify(parsed_ohio_state_cases_forecast)

@app.route(f'/Ohio_deaths_forecast')
def ohio_deaths_forecast():
    return jsonify(parsed_ohio_state_deaths_forecast)



# OKLAHOMA ROUTES
@app.route(f'/Oklahoma_cases')
def oklahoma_cases():
    return jsonify(parsed_oklahoma_state_cases)

@app.route(f'/Oklahoma_deaths')
def oklahoma_deaths():
    return jsonify(parsed_oklahoma_state_deaths)

@app.route(f'/Oklahoma_cases_forecast')
def oklahoma_cases_forecast():
    return jsonify(parsed_oklahoma_state_cases_forecast)

@app.route(f'/Oklahoma_deaths_forecast')
def oklahoma_deaths_forecast():
    return jsonify(parsed_oklahoma_state_deaths_forecast)



# OREGON ROUTES
@app.route(f'/Oregon_cases')
def oregon_cases():
    return jsonify(parsed_oregon_state_cases)

@app.route(f'/Oregon_deaths')
def oregon_deaths():
    return jsonify(parsed_oregon_state_deaths)

@app.route(f'/Oregon_cases_forecast')
def oregon_cases_forecast():
    return jsonify(parsed_oregon_state_cases_forecast)

@app.route(f'/Oregon_deaths_forecast')
def oregon_deaths_forecast():
    return jsonify(parsed_oregon_state_deaths_forecast)



# PENNSYLVANIA ROUTES
@app.route(f'/Pennsylvania_cases')
def pennsylvania_cases():
    return jsonify(parsed_pennsylvania_state_cases)

@app.route(f'/Pennsylvania_deaths')
def pennsylvania_deaths():
    return jsonify(parsed_pennsylvania_state_deaths)

@app.route(f'/Pennsylvania_cases_forecast')
def pennsylvania_cases_forecast():
    return jsonify(parsed_pennsylvania_state_cases_forecast)

@app.route(f'/Pennsylvania_deaths_forecast')
def pennsylvania_deaths_forecast():
    return jsonify(parsed_pennsylvania_state_deaths_forecast)



# PUERTO RICO ROUTES
@app.route(f'/Puerto Rico_cases')
def puerto_rico_cases():
    return jsonify(parsed_puerto_rico_state_cases)

@app.route(f'/Puerto Rico_deaths')
def puerto_rico_deaths():
    return jsonify(parsed_puerto_rico_state_deaths)

@app.route(f'/Puerto Rico_cases_forecast')
def puerto_rico_cases_forecast():
    return jsonify(parsed_puerto_rico_state_cases_forecast)

@app.route(f'/Puerto Rico_deaths_forecast')
def puerto_rico_deaths_forecast():
    return jsonify(parsed_puerto_rico_state_deaths_forecast)



# RHODE ISLAND ROUTES
@app.route(f'/Rhode Island_cases')
def rhode_island_cases():
    return jsonify(parsed_rhode_island_state_cases)

@app.route(f'/Rhode Island_deaths')
def rhode_island_deaths():
    return jsonify(parsed_rhode_island_state_deaths)

@app.route(f'/Rhode Island_cases_forecast')
def rhode_island_cases_forecast():
    return jsonify(parsed_rhode_island_state_cases_forecast)

@app.route(f'/Rhode Island_deaths_forecast')
def rhode_island_deaths_forecast():
    return jsonify(parsed_rhode_island_state_deaths_forecast)



# SOUTH CAROLINA ROUTES
@app.route(f'/South Carolina_cases')
def south_carolina_cases():
    return jsonify(parsed_south_carolina_state_cases)

@app.route(f'/South Carolina_deaths')
def south_carolina_deaths():
    return jsonify(parsed_south_carolina_state_deaths)

@app.route(f'/South Carolina_cases_forecast')
def south_carolina_cases_forecast():
    return jsonify(parsed_south_carolina_state_cases_forecast)

@app.route(f'/South Carolina_deaths_forecast')
def south_carolina_deaths_forecast():
    return jsonify(parsed_south_carolina_state_deaths_forecast)



# SOUTH DAKOTA ROUTES
@app.route(f'/South Dakota_cases')
def south_dakota_cases():
    return jsonify(parsed_south_dakota_state_cases)

@app.route(f'/South Dakota_deaths')
def south_dakota_deaths():
    return jsonify(parsed_south_dakota_state_deaths)

@app.route(f'/South Dakota_cases_forecast')
def south_dakota_cases_forecast():
    return jsonify(parsed_south_dakota_state_cases_forecast)

@app.route(f'/South Dakota_deaths_forecast')
def south_dakota_deaths_forecast():
    return jsonify(parsed_south_dakota_state_deaths_forecast)



# TENNESSEE ROUTES
@app.route(f'/Tennessee_cases')
def tennessee_cases():
    return jsonify(parsed_tennessee_state_cases)

@app.route(f'/Tennessee_deaths')
def tennessee_deaths():
    return jsonify(parsed_tennessee_state_deaths)

@app.route(f'/Tennessee_cases_forecast')
def tennessee_cases_forecast():
    return jsonify(parsed_tennessee_state_cases_forecast)

@app.route(f'/Tennessee_deaths_forecast')
def tennessee_deaths_forecast():
    return jsonify(parsed_tennessee_state_deaths_forecast)



# TEXAS ROUTES
@app.route(f'/Texas_cases')
def texas_cases():
    return jsonify(parsed_texas_state_cases)

@app.route(f'/Texas_deaths')
def texas_deaths():
    return jsonify(parsed_texas_state_deaths)

@app.route(f'/Texas_cases_forecast')
def texas_cases_forecast():
    return jsonify(parsed_texas_state_cases_forecast)

@app.route(f'/Texas_deaths_forecast')
def texas_deaths_forecast():
    return jsonify(parsed_texas_state_deaths_forecast)



# UTAH ROUTES
@app.route(f'/Utah_cases')
def utah_cases():
    return jsonify(parsed_utah_state_cases)

@app.route(f'/Utah_deaths')
def utah_deaths():
    return jsonify(parsed_utah_state_deaths)

@app.route(f'/Utah_cases_forecast')
def utah_cases_forecast():
    return jsonify(parsed_utah_state_cases_forecast)

@app.route(f'/Utah_deaths_forecast')
def utah_deaths_forecast():
    return jsonify(parsed_utah_state_deaths_forecast)



# VERMONT ROUTES
@app.route(f'/Vermont_cases')
def vermont_cases():
    return jsonify(parsed_vermont_state_cases)

@app.route(f'/Vermont_deaths')
def vermont_deaths():
    return jsonify(parsed_vermont_state_deaths)

@app.route(f'/Vermont_cases_forecast')
def vermont_cases_forecast():
    return jsonify(parsed_vermont_state_cases_forecast)

@app.route(f'/Vermont_deaths_forecast')
def vermont_deaths_forecast():
    return jsonify(parsed_vermont_state_deaths_forecast)



# VIRGIN ISLANDS ROUTES
@app.route(f'/Virgin Islands_cases')
def virgin_islands_cases():
    return jsonify(parsed_virgin_islands_state_cases)

@app.route(f'/Virgin Islands_deaths')
def virgin_islands_deaths():
    return jsonify(parsed_virgin_islands_state_deaths)

@app.route(f'/Virgin Islands_cases_forecast')
def virgin_islands_cases_forecast():
    return jsonify(parsed_virgin_islands_state_cases_forecast)

@app.route(f'/Virgin Islands_deaths_forecast')
def virgin_islands_deaths_forecast():
    return jsonify(parsed_virgin_islands_state_deaths_forecast)



# VIRGINIA ROUTES
@app.route(f'/Virginia_cases')
def virginia_cases():
    return jsonify(parsed_virginia_state_cases)

@app.route(f'/Virginia_deaths')
def virginia_deaths():
    return jsonify(parsed_virginia_state_deaths)

# VIRGINIA ROUTES
@app.route(f'/Virginia_cases_forecast')
def virginia_cases_forecast():
    return jsonify(parsed_virginia_state_cases_forecast)

@app.route(f'/Virginia_deaths_forecast')
def virginia_deaths_forecast():
    return jsonify(parsed_virginia_state_deaths_forecast)



# WASHINGTON ROUTES
@app.route(f'/Washington_cases')
def washington_cases():
    return jsonify(parsed_washington_state_cases)

@app.route(f'/Washington_deaths')
def washington_deaths():
    return jsonify(parsed_washington_state_deaths)

@app.route(f'/Washington_cases_forecast')
def washington_cases_forecast():
    return jsonify(parsed_washington_state_cases_forecast)

@app.route(f'/Washington_deaths_forecast')
def washington_deaths_forecast():
    return jsonify(parsed_washington_state_deaths_forecast)



# WEST VIRGINIA ROUTES
@app.route(f'/West Virginia_cases')
def west_virginia_cases():
    return jsonify(parsed_west_virginia_state_cases)

@app.route(f'/West Virginia_deaths')
def west_virginia_deaths():
    return jsonify(parsed_west_virginia_state_deaths)

@app.route(f'/West Virginia_cases_forecast')
def west_virginia_cases_forecast():
    return jsonify(parsed_west_virginia_state_cases_forecast)

@app.route(f'/West Virginia_deaths_forecast')
def west_virginia_deaths_forecast():
    return jsonify(parsed_west_virginia_state_deaths_forecast)



# WISCONSIN ROUTES
@app.route(f'/Wisconsin_cases')
def wisconsin_cases():
    return jsonify(parsed_wisconsin_state_cases)

@app.route(f'/Wisconsin_deaths')
def wisconsin_deaths():
    return jsonify(parsed_wisconsin_state_deaths)

@app.route(f'/Wisconsin_cases_forecast')
def wisconsin_cases_forecast():
    return jsonify(parsed_wisconsin_state_cases_forecast)

@app.route(f'/Wisconsin_deaths_forecast')
def wisconsin_deaths_forecast():
    return jsonify(parsed_wisconsin_state_deaths_forecast)



# WYOMING ROUTES
@app.route(f'/Wyoming_cases')
def wyoming_cases():
    return jsonify(parsed_wyoming_state_cases)

@app.route(f'/Wyoming_deaths')
def wyoming_deaths():
    return jsonify(parsed_wyoming_state_deaths)

@app.route(f'/Wyoming_cases_forecast')
def wyoming_cases_forecast():
    return jsonify(parsed_wyoming_state_cases_forecast)

@app.route(f'/Wyoming_deaths_forecast')
def wyoming_deaths_forecast():
    return jsonify(parsed_wyoming_state_deaths_forecast)



if __name__ == "__main__":
    app.run(debug=True)