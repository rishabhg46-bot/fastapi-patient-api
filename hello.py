from fastapi import FastAPI
app = FastAPI()
def load_data():
    import json
    with open('patients.json') as f:
        data = json.load(f)
    return data
@app.get("/")
def hello():
    return {"message": "patient management system api "}
@app.get('/about')
def about():
    return {"message":'a fully functioning api to manage your patients records'}
@app.get('views/patients')
def view():
    data=load_data()
    return data