import tkinter
import requests
import datetime as dt

BACKGROUND = "black"
sheety_endpoint = "https://api.sheety.co/addba4b3b88a9dd19e6b21123a15b566/onlineText/sheet1"
today_day = dt.datetime.now()

def upload():
    TEXT = f'{text_field1.get("1.0", "end-1c")}'
    sheety_parameters = {
        'sheet1': {
            'date': f"{today_day.year}-{today_day.month}-{today_day.day}",
            'text': TEXT,
        }
    }
    requests.post(sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
    window.config(bg='green') 

def getText():
    feteched_data = requests.get(sheety_endpoint, headers=sheety_headers)
    uploaded_text = feteched_data.json()['sheet1'][-1]['text']
    text_field2.insert(tkinter.END, uploaded_text)
    window.config(bg='black')
    
sheety_headers = {
    'Authorization': 'Basic cmFodWwxMjI3MDM6MjdkZWNlbWJlcjIwMDM=',
    'username': 'rahul122703',
    'password': '27december2003'
}

connection_get = requests.get(sheety_endpoint, headers=sheety_headers)

window = tkinter.Tk()
window.config(bg=BACKGROUND) 
window.title("COPY APP")

field_text1 = tkinter.Label(window, text="ENTER TEXT BELOW", font=("arial",10, "bold"), fg="white", bg=BACKGROUND)
field_text1.grid(row=0, column=1)

field_text2 = tkinter.Label(window, text="UPLOADED TEXT", font=("arial", 10, "bold"), fg="white", bg=BACKGROUND)
field_text2.grid(row=0, column=3)


text_field1 = tkinter.Text(window, height=70, width=50)
text_field1.grid(row=1, column=0, columnspan=2)

text_field2 = tkinter.Text(window, height=70, width=50) 
text_field2.grid(row=1, column=2, columnspan=3)


Upload = tkinter.Button(window, text="UPLOAD THIS TEXT", font=('arial',10,"bold") ,command=upload)
Upload.grid(row=0, column=0)

get_data = tkinter.Button(window, text="GET THE TEXT",font=('arial',10,"bold") , command=getText)
get_data.grid(row=0, column=2)

window.mainloop()