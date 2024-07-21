from flask import Flask,render_template,request

import requests
import datetime as dt

sheety_endpoint = "https://api.sheety.co/03f45a2492e8c24d4b1b90a319112262/copyapp/sheet1"
today_day = dt.datetime.now()
  
sheety_headers = {
    'Authorization': 'Basic cmFodWwxMjI3MDM6cmFodWwxMjI3MDM=',
    'username': 'rahul122703',
    'password': 'rahul122703'
}

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/upload', methods = ['POST','GET'])
def upload():
    uploaded_text = request.form.get('uploadText')
    print(request.form.get('uploadText'))
    sheety_parameters = {
        'sheet1': {
            'date': f"{today_day.year}/{today_day.month}/{today_day.day}/{today_day.hour}:{today_day.minute}:{today_day.second}",
            'text': uploaded_text
        }
    }
    requests.post(sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
    print("upload running")
    feteched_data = requests.get(sheety_endpoint, headers=sheety_headers)
    received_text = feteched_data.json()['sheet1'][-1]['text']
    return render_template('index.html',uploaded_text = uploaded_text,recived_text = received_text)
    
@app.route('/recieve', methods = ['POST','GET'])
def getText():
    feteched_data = requests.get(sheety_endpoint, headers=sheety_headers)
    received_text = feteched_data.json()['sheet1'][-1]['text']
    print(received_text)
    return render_template('index.html',recived_text = received_text)


if __name__ == "__main__":
    app.run(debug=True, port=5002)