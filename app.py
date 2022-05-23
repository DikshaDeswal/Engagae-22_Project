from flask import Flask, render_template, request,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

model=pickle.load(open('Mileage_Pred_Model.pkl','rb'))
model1=pickle.load(open('Torque_Pred_Model.pkl','rb'))
model2=pickle.load(open('Chasis_Pred_Model.pkl','rb'))
model3=pickle.load(open('Price_22_Pred_Model.pkl','rb'))
model4=pickle.load(open('buy.pkl', 'rb'))

app=Flask(__name__)


@app.route('/', methods=["GET","POST"])
def main():
    return render_template('home.html')

@app.route('/sell', methods=["GET","POST"])
def main_sell():
    return render_template('sell.html')

@app.route('/sell/submit', methods=["GET","POST"])
def main_sell_pred():
    if request.method=="POST":
        data1 = request.form['a']
        data2 = request.form['b']
        data3 = request.form['c']
        data4 = request.form['d']
        data5 = request.form['e']
    arr = np.array([[data1, data2, data3, data4]])
    arr = arr.astype(np.int)
    pred=model.predict(arr)
    return render_template('predict.html', data1=pred)

@app.route('/sell/submit1', methods=["GET","POST"])
def main_sell_pred_Torque():
    if request.method=="POST":
        data6=request.form['f']
        data7 = request.form['g']
        data8 = request.form['h']
        data9 = request.form['i']
        data10 = request.form['j']
    arr1 = np.array([[data6, data7, data8]])
    arr1 = arr1.astype(np.int)
    pred1=model1.predict(arr1)
    return render_template('predict.html', data2=pred1)

@app.route('/sell/submit2', methods=["GET","POST"])
def main_sell_pred_Power():
    if request.method=="POST":
        data11=request.form['k']
        data12 = request.form['l']
        data13 = request.form['m']
        data14 = request.form['n']
    arr2 = np.array([[data14, data11, data12, data13]])
    arr2 = arr2.astype(np.int)
    pred2=model2.predict(arr2)
    return render_template('predict.html', data3=pred2)


@app.route('/stats', methods=["GET","POST"])
def main_stats():
    return render_template('stats.html')

@app.route('/stats/stats_mileage', methods=["GET","POST"])
def main_stats_mileage():
    return render_template('stats_mileage.html')

@app.route('/stats/stats_body', methods=["GET","POST"])
def main_stats_body():
    return render_template('stats_body.html')

@app.route('/stats/stats_miscellaneous', methods=["GET","POST"])
def main_stats_miscellaneous():
    return render_template('stats_miscellaneous.html')

@app.route('/buy', methods=["GET","POST"])
def main_buy():
    return render_template('buy.html')

@app.route('/buy/pred', methods=["GET","POST"])
def main_buy_pred():
    if request.method=="POST":
        data21 = request.form['ii']
        data22 = request.form['jj']
        data23 = request.form['ee']
        data24 = request.form['ff']
        data25 = request.form['aa']
        data26 = request.form['bb']
    price=int(data21)
    arr5=[]
    arr6=[]
    i=0
    while (i<5):
        arr5[i]=price+ (5000*i)
        i=i+1
    j=0
    while(j<5):
        arr4 = np.array([[arr5[j], data22, data23, data24, data25, data26]])
        arr4 = arr4.astype(np.int)
        pred4=model4.predict(arr4)
        arr6[j]=pred4
        j=j+1
    return render_template('buy.html', data4=arr6)

@app.route('/predict', methods=["GET","POST"])
def main_predict():
    return render_template('predict.html')

@app.route('/contact', methods=["GET","POST"])
def main_contact():
    return render_template('contact.html')


if __name__=="__main__":
    app.run(debug=True)