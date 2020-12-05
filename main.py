from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def city():

    info = requests.get('https://api.coindesk.com/v1/bpi/currentprice/CNY.json')
    r_json = info.json()

    currency= r_json['bpi']['USD']['code']
    value =r_json['bpi']['USD']['rate']
    des = r_json['bpi']['USD']['description']
    rate = r_json['bpi']['USD']['rate_float']
    updated = r_json['time']['updated']



    return render_template("index.html", currency =currency,value= value, description =des,rate =rate,updated =updated )



if __name__ == '__main__':
    app.run(debug=True)
