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
model5=pickle.load(open('sell_22.pkl', 'rb'))
model6=pickle.load(open('buy01.pkl', 'rb'))
model7=pickle.load(open('buy2.pkl', 'rb'))

app=Flask(__name__)


@app.route('/', methods=["GET","POST"])
def main():
    return render_template('home.html')

@app.route('/sell', methods=["GET","POST"])
def main_sell():
    return render_template('sell1.html')

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
    return render_template('mileage.html', data1=pred)

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
    return render_template('torque.html', data2=pred1)

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
    return render_template('power.html', data3=pred2)


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

@app.route('/buy/buy_pro', methods=["GET","POST"])
def main_buy_pro():
    return render_template('buy_pro.html')

@app.route('/buy/buy_pro/buy1', methods=["GET","POST"])
def main_buy_1():
    return render_template('buy1.html')

@app.route('/buy/buy_pro/buy3', methods=["GET","POST"])
def main_buy_3():
    return render_template('buy3.html')

@app.route('/buy/buy_pro/buy4', methods=["GET","POST"])
def main_buy_4():
    return render_template('buy4.html')

@app.route('/buy/buy_pro/buy5', methods=["GET","POST"])
def main_buy_5():
    return render_template('buy5.html')

@app.route('/buy/buy_pro/buy6', methods=["GET","POST"])
def main_buy_6():
    return render_template('buy6.html')

@app.route('/buy/buy_buy_pro/buy1/predict', methods=["GET","POST"])
def main_buy_buy1():
    if request.method=="POST":
        data41 = request.form['z1']
        data42 = request.form['z2']
        data43 = request.form['z3']
        data44 = request.form['z4']
        data45 = request.form['z5']
    arr11 = np.array([[data41, data42, data43, data44, data45]])
    arr11 = arr11.astype(np.int)
    pred11=model6.predict(arr11)
    pred11=(pred11)
    return render_template('buy1.html', data11=pred11)


@app.route('/buy/pred', methods=["GET","POST"])
def main_buy_pred():
    if request.method=="POST":
        data21 = request.form['b5']
        data22 = request.form['b6']
        data23 = request.form['b7']
        data24 = request.form['b8']
        data25 = request.form['b1']
        data26 = request.form['b4']
        arr9 = np.array([[data21, data22, data23, data24, data25, data26]])
        arr9 = arr9.astype(np.int)
        pred9=model4.predict(arr9)
    return render_template('buy.html', data9=pred9)

@app.route('/predict', methods=["GET","POST"])
def main_predict():
    return render_template('predict.html')

@app.route('/portfolio', methods=["GET","POST"])
def main_contact():
    return render_template('contact.html')

@app.route('/sell_stat', methods=["GET","POST"])
def main_sell_stat():
    return render_template('sell.html')

@app.route('/mileage', methods=["GET","POST"])
def mileage():
    return render_template('mileage.html')

@app.route('/torque', methods=["GET","POST"])
def torque():
    return render_template('torque.html')

@app.route('/power', methods=["GET","POST"])
def power():
    return render_template('power.html')

@app.route('/sell/pred_price', methods=["GET", "POST"])
def main_sell_pred_price():
    if request.method == "POST":
        data31 = request.form['a5']
        data32 = request.form['a6']
        data33 = request.form['a7']
        data34 = request.form['a8']
        data35 = request.form['a3']
        data36 = request.form['a4']
    arr8 = np.array([[data31, data32, data33, data34, data35, data36]])
    arr8 = arr8.astype(np.int)
    pred8 = model5.predict(arr8)
    return render_template('sell1.html', data8=pred8)

@app.route('/buy/buy_pro/buy2', methods=["GET","POST"])
def buy2():
    return render_template('buy2.html')

@app.route('/buy/buy2/predict', methods=["GET","POST"])
def main_buy_buy2():
    if request.method=="POST":
        data51 = request.form['y1']
        data52 = request.form['y2']
        data53 = request.form['y3']
        data54 = request.form['y4']
        data55 = request.form['y5']
    arr12 = np.array([[data51, data52, data53, data54, data55]])
    arr12 = arr12.astype(np.int)
    pred12=model7.predict(arr12)
    return render_template('buy2.html', data12=pred12)



if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0')