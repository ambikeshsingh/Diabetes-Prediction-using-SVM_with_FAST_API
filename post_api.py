# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:14:34 2023

@author: Ambikesh
"""

import json
import requests

url='http://127.0.0.1:8000/diabetes_prediction'

input_data_from_model={
    'Pregnancies' : 8    ,            
    'Glucose' :  183      ,            
    'BloodPressure': 64  ,            
    'SkinThickness':  0 ,            
    'Insulin': 0        ,            
    'BMI': 23.3          ,            
    'DiabetesPedigreeFunction': 0.172, 
    'Age':32
    }
    
input_json=json.dumps(input_data_from_model)
response=requests.post(url,data=input_json)
print(response.text)    