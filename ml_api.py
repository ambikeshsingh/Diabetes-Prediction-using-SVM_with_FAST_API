# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:03:47 2023

@author: Ambikesh
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

class model_input(BaseModel):
    Pregnancies :int              
    Glucose : int                    
    BloodPressure:int               
    SkinThickness:int               
    Insulin:int                     
    BMI:float                       
    DiabetesPedigreeFunction:float  
    Age:int 
    
#loading the saved model
diabetes_model=pickle.load(open('trained_model.svc','rb')) 

@app.post('/diabetes_prediction')

def diabetes_pred(input_parameters:model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)
    
    preg=input_dictionary['Pregnancies']
    glue=input_dictionary['Glucose']
    bp=input_dictionary['BloodPressure']
    skin=input_dictionary['SkinThickness']
    insulin=input_dictionary['Insulin']
    BMI=input_dictionary['BMI']
    dpf=input_dictionary['DiabetesPedigreeFunction']
    age=input_dictionary['Age']
   
    
    input_list=[preg,glue,bp,skin,insulin,BMI,dpf,age]
    prediction=diabetes_model.predict([input_list])
    
    if (prediction[0]==0):
        return 'The person is not Diabetic'
    else:
        return 'The person is Diabetic'
   
    