import re

import pandas as pd

from utils import load_json,flatten_dict_innermost


def clean_map_data():
    # hospitals = load_json('hospitals.csv')

    # df = pd.read_csv('hospitals.csv')

    hospitals = load_json('hospitals.json')

    # todo: flattened the data
    flattened_hospitals_data = [flatten_dict_innermost(hospital) for hospital in hospitals]
    hospitals_df = pd.DataFrame(flattened_hospitals_data)

    # todo: clean empty columns
    hospitals_df.replace('','Not Available',inplace=True)

    # todo: drop nulls for lat and long
    hospitals_df = hospitals_df[
        (hospitals_df['Latitude'] != 'Not Available') & (hospitals_df['Longitude'] != 'Not Available')]

    # todo: convert latitude and longitude into floats
    hospitals_df['Latitude'] = hospitals_df['Latitude'].astype(float)
    hospitals_df['Longitude'] = hospitals_df['Longitude'].astype(float)

    # todo: convert some dtypes to number
    hospitals_df['Number of Doctors'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Pharmacists'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number Pharmacy Technicians'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Dentists'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Dental Technicians'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Nurses'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Midwifes'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Nurses/Midwifes'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Lab Technicians'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Lab Scientits'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Health Records/HIM Officers'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Community Health Officer'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Community Health Extension Worker'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Junior Com Health Extension Worker'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Environmental Health Officers'] = hospitals_df['Longitude'].astype(int)
    hospitals_df['Number of Health Attendant/Assistant'] = hospitals_df['Longitude'].astype(int)

    # todo: clean phone number
    # hospitals_df['Phone Number'] = hospitals_df['Phone Number'].apply(lambda x: re.sub(r'\D','',x))

    # todo: clean and flatten special services
    ss = (hospitals_df['Specific Clinical Services'])
    ss = [s for s in ss]

    sf = []
    for s in ss:
        for i in s:
            if i not in sf:
                sf.append(i)
    for s in sf:
        hospitals_df[s] = 'No'

    # print(len(sf))
    # for s in sf:
    #     print(s)

    # todo: apply the right data to all specific clinical services column
    for idx, row in hospitals_df.iterrows():
        for s in row['Specific Clinical Services']:
            hospitals_df.at[idx, s] = 'Yes'

    # print((hospitals_df['HIV/ AIDS Services'] == 'No').sum())

    # todo: add icon columns
    hospitals_df['Icon'] = 'place'

    # todo: finally save the data in a csv file
    hospitals_df.to_csv('hospitals_data_final.csv')
    hospitals_df.to_excel('hospitals_data_final.xlsx')
    print('csv file saved successfully! ')

clean_map_data()
