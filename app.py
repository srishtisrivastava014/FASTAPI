from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data


@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get("/view")
def view_data():
    data = load_data()
    return data

@app.get("/about")
def about():
    return {"message": "This is the about patient management systempage"}