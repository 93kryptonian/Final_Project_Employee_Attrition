import joblib 
import pandas as pd 
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def bearnda():
    return render_template('beranda.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/result', methods=['GET', 'POST'])
def Rec():
    if request.method == 'POST':

        input = request.form
        name = input["name"]
        age= int(input["age"])
        gender= input["gender"]

        if gender =="Female":
            gen= 0
        else:
            gen= 1

        jlevel = input["jlevel"]
        if jlevel == "Staff":
            level = 0
        elif jlevel == "Manager":
            level = 1
        elif jlevel == "Board":
            level = 2
        else:
            level = 3

        ms_kerja = int(input["ms_kerja"])

        category = input["dcat"]

        if category =="Business":
            cat = 0
        else:
            cat = 1
        
        bUnit = input["bu"]
        if bUnit =="Head Office":
            bu = 0
        else:
            bu = 1
        dataInput = [[age, ms_kerja, gen, bu, level, cat]]
        deteksi = modelJoblib.predict_proba(dataInput)[0][1]
        hasil = round((deteksi * 100), 2)
        




        return render_template('result.html',  name=name, gender=gender, age=age, ms_kerja=ms_kerja, jlevel=jlevel, dcat=category, bu=bUnit, result=hasil)
    else:
        return "Mustinya anda ngePOST"





















if __name__ == "__main__":
    modelJoblib = joblib.load('modelAttrition')

    app.run(debug = True, port=5000)