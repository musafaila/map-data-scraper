
from utils import load_json,convert_to_csv

import  pandas as pd

def demo():
   hospitals = load_json("hospitals.json")

   # IDENTIFIERS
   # fcode
   # suid
   # regNo
   # name
   # sdate
   # ownership
   # type
   # level
   # opDays
   # opHours

   # LOCATION
   # state
   # lga
   # ward
   # locDesc
   # lat
   # long

   # CONTACTS
   # phone
   # email
   # website

   # STATUS
   # opStatus
   # regStatus


   formatted_hospitals = []
   for hospital in hospitals:
      formatted_hospitals.append({
         "fcode": hospital.get('Identifiers')['Facility Code'],
         "suid": hospital.get('Identifiers')['State Unique ID'],
         "regNo": hospital.get('Identifiers')['Registration No'],
         "name": hospital.get('Identifiers')['Facility Name'],
         "sDate": hospital.get('Identifiers')['Start Date'],
         "ownership": hospital.get('Identifiers')['Ownership'],
         "type": hospital.get('Identifiers')['Ownership Type'],
         "level": hospital.get('Identifiers')['Facility Level'],
         "opDays": hospital.get('Identifiers')['Days of Operation'],
         "opHours": hospital.get('Identifiers')['Hours of Operation'],

         # location
         "state": hospital.get('Location')['State'],
         "lga": hospital.get('Location')['LGA'],
         "ward": hospital.get('Location')['Ward'],
         "locDesc": hospital.get('Location')['Physical Location'],
         "lat": hospital.get('Location')['Latitude'],
         "long": hospital.get('Location')['Longitude'],

         # contacts
         "phone": hospital.get('Contacts')['Phone Number'],
         "email": hospital.get('Contacts')['Email Address'],
         "website": hospital.get('Contacts')['Website'],

         # status
         "opStatus": hospital.get('Status')['Operational Status'],
         "regStatus": hospital.get('Status')['Registration Status'],
      })


   convert_to_csv(formatted_hospitals, 'hospitals.csv')


demo()