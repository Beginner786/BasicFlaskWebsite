import requests
from flask import Flask, render_template, request
import requests_cache
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/home')
def back():
    return render_template('index.html')


@app.route('/epass', methods=['POST',"GET"])
def epass():
    firstName =request.form['fname']
    lastName = request.form['lname']
    emailID  = request.form['email']
    sourceST = request.form['sourceST']
    sourceDT = request.form['sourceDT']
    destinationST = request.form['destinationST']
    destinationDT = request.form['destinationDT']
    phoneNumber = request.form['phoneNumber']
    idProof = request.form['idProof']
    date = request.form['trip']
    fullName =firstName + "." + lastName
    r =requests.get('https://api.covid19india.org/v4/data.json')
    jsonData = r.json()
    cnt = jsonData[destinationST]['districts'][destinationDT]['total']['confirmed']
    pop = jsonData[destinationST]['districts'][destinationDT]['meta']['population']
    travelPass = (cnt/pop)*100
    if(travelPass < 30 and request.method=='POST'):
        status='CONFIRMED'
    else:
        status = 'NOT CONFIRMED'
    return render_template('output.html', var=fullName, var1=emailID, var2=idProof, var3=sourceST, var4=sourceDT, var5=destinationST, var6=destinationDT, var7=phoneNumber, var8=date, var9=status)

if __name__ == '__main__':
    app.run(port=5000,debug=True)