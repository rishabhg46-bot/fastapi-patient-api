from fastapi import FastAPI,Path,HTTPException,Query
import json
import os
app = FastAPI()

def load_data():
    with open('patients.json') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "patient management system api "}

@app.get('/about')
def about():
    return {"message":'a fully functioning api to manage your patients records'}

@app.get('/view')
def view():
    data=load_data()
    return data


@app.get('/patient/{patient_id}')
def view_patient (patient_id:str=Path(...,description ='ID of the pateint in the DB',exapmle='P001')):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail='patient not found')
    

@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description='attribute to sort by height weight BMI'),order:str=Query('asc',description='sorting order asc or desc')):
    valid_fields=['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'invalid field selected. Please choose from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='invalid sorting order. Please choose asc or desc')
    data=load_data()
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by),reverse=sort_order)
    return sorted_data