from flask import Flask, render_template, redirect, request, jsonify, send_from_directory, send_file, Response, session
import requests
from decouple import config, AutoConfig
import pandas as pd
import random
import os, io, xlsxwriter
import datetime as dt

app = Flask(__name__)

app.secret_key = b"_j'yXdW7.63}}b7"

API_KEY = config('API_KEY')

def rightnow():
    return dt.datetime.now().strftime("%h-%d, %I-%M")

@app.route("/generacion", methods=["GET","POST"])
def generacion():
    ### Getting relevant data.
    x = request.form.to_dict(flat=False)
    URL = 'https://developer.nrel.gov/api/pvwatts/v6.json?api_key=' + API_KEY
    r = requests.get(url=URL, params=x)
    data = r.json()
    df = pd.DataFrame(data["outputs"])
    ac_a = df['ac_annual'][0]
    sol_a = df['solrad_annual'][0]
    totals = pd.DataFrame([[sol_a,ac_a]], columns=['solrad_monthly','ac_monthly'])

    ### Cleaning and transforming the data.
    table = df.append(totals, ignore_index = True)
    table = table[['solrad_monthly', 'ac_monthly']]
    table = table.reset_index()
    table = table.set_axis(['Mes','Solar Radiation (kWh / m2 / day)', 'AC Energy (kWh)'], axis=1, inplace=False)
    table = table.replace({0: 'Enero',1: 'Febrero',2:'Marzo',3:'Abril',4:"Mayo",5:"Junio",6:"Julio",7:"Agosto",8:"Septiembre",9:"Octubre",10:'Noviembre',11:'Diciembre',12:'Annual'})

    #table.to_excel(session["table"])
    ### Creating XLSX from DataFrame
    new_file = f'output_{rightnow()}.xlsx'
    writer = pd.ExcelWriter(f'tmp/{new_file}', engine='xlsxwriter')
    table.to_excel(writer, sheet_name="Solar Generation", float_format="%.4f")      
    writer.save()
    session['table'] = f'tmp/{new_file}'

    return render_template('gen.html', tables=[table.to_html(classes='data', index=False, float_format=lambda x: '%.2f' % x)])

@app.route("/d", methods=["GET","POST"])
def download():
    xlsx = session["table"]
    buf_str = io.StringIO(xlsx)
    buf_byt = io.BytesIO(buf_str.read().encode("utf-8"))
    return send_file(xlsx,
                    as_attachment=True, 
                    attachment_filename=f"output_{rightnow()}.xlsx")


@app.route("/", methods=["GET","POST"])
def form():
    ### Redirect to "Generacion" if the form is submitted.
    if request.method == "POST":
        return redirect(request.url)
    
    return render_template("form.html")


if __name__ == "__main__":
    app.run(threaded=True)

