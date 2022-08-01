
from werkzeug.utils import secure_filename
import numpy as np
import pickle
import os
from flask import Flask,render_template,request,send_file,safe_join,request,abort
import pickle
import shutil
import pandas
import pandas as pd
from flask_cors import CORS



model = pickle.load(open('rf.pkl','rb'))



app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    # Main page
    return render_template('index.html')


@app.route('/index.html', methods=['GET'])
def home_one():
    # Main page
    return render_template('index.html')



@app.route('/credit.html',methods=['GET'])
def credit():
  return render_template('credit.html')


@app.route('/credit_csv.html',methods=['GET'])
def credit_csv():
  return render_template('credit_csv.html')


@app.route('/credit_predict',methods=['GET','POST'])
def credit_predict():
    array = list()
    time = float(request.form['time'])
    v1 = float(request.form['v1'])
    v2 = float(request.form['v2'])
    v3 = float(request.form['v3']) 
    v4 = float(request.form['v4'])  
    v5 = float(request.form['v5'])
    v6 = float(request.form['v6'])
    v7 = float(request.form['v7'])
    v8 = float(request.form['v8'])
    v9 = float(request.form['v9'])
    v10 = float(request.form['v10'])
    v11 =float(request.form['v11'])
    v12 = float(request.form['v12'])
    v13 = float(request.form['v13'])
    v14 = float(request.form['v14'])
    v15 = float(request.form['v15'])
    v16 = float(request.form['v16'])
    v17= float(request.form['v17'])
    v18 = float(request.form['v18'])
    v19 = float(request.form['v19'])
    v20 = float(request.form['v20'])
    v21 = float(request.form['v21'])
    v22 = float(request.form['v22'])
    v23 = float(request.form['v23'])
    v24 = float(request.form['v24'])
    v25 = float(request.form['v25'])
    v26 = float(request.form['v26'])
    v27 = float(request.form['v27'])
    v28 = float(request.form['v28'])
    amount = float(request.form['amount'])




    array = array + [time,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,amount]
    
    
    output = int(model.predict([array])[0])

    
    if output == 1 :
      return render_template('credit_result.html',pred='Fraud Transaction')


    else :
      return render_template('credit_result.html',pred='Normal Transaction')















@app.route('/credit_uploader', methods = ['GET', 'POST'])
def credit_upload_file():
   if request.method == 'POST':
      f = request.files['file']
      data = pd.read_csv(f)
      prediction = model.predict(data.values) 
      print(prediction)   
      final = pd.DataFrame({'Output':prediction})
   

     
      final.to_csv('credit_result.csv')
     
     
      
	      
      # return 'file uploaded successfully'
      return render_template('credit_csv_download.html')

@app.route('/credit_csv_result')
def credit_csv_result():
   

    
    return send_file('credit_result.csv', as_attachment=True)

















if __name__ == '__main__':
    app.run(debug=False)
