from flask import Flask, render_template, jsonify, request, redirect, url_for
from opt import getDNS
import random
from ipconfig import ipconfig,set_dns_mac
from client import test_speed
import time

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():

    return render_template("index.html")

# def home():
#     info = getInfo()
#     return render_template("index.html",info=info)


def generateData():
    realData=random.randint(1,200)
    return  realData

@app.route('/getSpeed')
def run():
    upload_speed, download_speed = test_speed()
    speed=(upload_speed+download_speed)/2



    return jsonify(speed=speed,ping=0,download=download_speed,upload=upload_speed)
@app.route('/dnsServer')
def getDnsServer():
    print("work")
    dns=getDNS()
    info=ipconfig()

    return render_template("index.html",dns=dns,info=info)

    # return redirect(url_for("home",dns=getDNS(),info=ipconfig()))
# @app.route('/dns')
# def update():
#
#     dns=getDNS()
#     info=ipconfig()
#
#     return jsonify(dns=dns,info=info)

@app.route("/setDNS" ,methods = ['POST'])
def setDNS():
    dns = request.form['dns']
    print(dns)
    set_dns_mac(dns)
    return "finish"

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)



