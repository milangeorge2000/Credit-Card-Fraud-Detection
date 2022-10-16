

import numpy as np
import pickle
import os
from flask import Flask,render_template,request,send_file,safe_join,request,abort
import pickle

import pandas
import pandas as pd




# model = pickle.load(open('rf5.pkl','rb'))



app = Flask(__name__)


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


@app.route('/credpredict',methods=['GET','POST'])
def credit_predict():
    array = list()
   
   
    v3 = float(request.form['V3']) 
    v4 = float(request.form['V4'])  
  
    v9 = float(request.form['V9'])
    v10 = float(request.form['V10'])
    v11 =float(request.form['V11'])
    v12 = float(request.form['V12'])
   
    v14 = float(request.form['V14'])
  
    v16 = float(request.form['V16'])
    v17= float(request.form['V17'])
    v18 = float(request.form['V18'])
   
    




    array = array + [v3,v4,v9,v10,v11,v12,v14,v16,v17,v18]
    
    
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
      data = data[['V3','V4','V9','V10','V11','V12','V14','V16','V17','V18']]
      prediction = model.predict(data.values) 
      print(prediction)
      output = []
      for i in prediction:
            if(i == 0):
               output.append('Normal')
            else:
              output.append('Fraud')
      final = pd.DataFrame({'Output':output})
   

     
      final.to_csv('cfl.csv')
     
     
      
	      
      # return 'file uploaded successfully'
      return render_template('credit_csv_result.html',prediction=output)

@app.route('/cpred')
def find_res():
   

    
    return send_file('cfl.csv', as_attachment=True)

















if __name__ == '__main__':
    app.run(debug=False)
