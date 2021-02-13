from flask import Flask, render_template, redirect, request, jsonify
import requests
from decouple import config, AutoConfig
import pandas as pd

app = Flask(__name__)

API_KEY = config('API_KEY')

@app.route("/generacion", methods=["GET","POST"])
def form():
    x = request.form.to_dict(flat=False)
    URL = 'https://developer.nrel.gov/api/pvwatts/v6.json?api_key=' + API_KEY
    r = requests.get(url=URL, params=x)
    data = r.json()
    df = pd.DataFrame(data["outputs"])

    ac_a = df['ac_annual'][0]
    sol_a = df['solrad_annual'][0]
    totals = pd.DataFrame([[sol_a,ac_a]], columns=['solrad_monthly','ac_monthly'])
    df = df.append(totals, ignore_index = True)

    df_new = df[['solrad_monthly', 'ac_monthly']]
    df_new = df_new.reset_index()
    table = df_new.set_axis(['Mes','Solar Radiation (kWh / m2 / day)', 'AC Energy (kWh)'], axis=1, inplace=False)
    table = table.replace({0: 'Enero',1: 'Febrero',2:'Marzo',3:'Abril',4:"Mayo",5:"Junio",6:"Julio",7:"Agosto",8:"Septiembre",9:"Octubre",10:'Noviembre',11:'Diciembre',12:'Annual'})

    return render_template('gen.html', tables=[table.to_html(classes='data', index=False, float_format=lambda x: '%10.2f' % x)])

@app.route("/", methods=["GET","POST"])
def sign_up():

    if request.method == "POST":
        return redirect(request.url)
    
    return render_template("form.html")


if __name__ == "__main__":
    app.run()

