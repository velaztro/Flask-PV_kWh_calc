# PV-Calc

## Overview
This a <a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank">Flask</a> Web App made it based on <a href="https://pvwatts.nrel.gov/index.php" target="_blank">NREL - PV Watts</a> and its <a href="https://developer.nrel.gov/docs/solar/pvwatts/v6/" target="_blank">API</a>. 

The web app consist in a form with the necessary parameters for the API, a button for get the latitude and longitude and a submit button. When you submit the form it use POST method to send the captured parameters to a another route in the app and sends a GET request to the API. Then the app capture the API information, clean and prepare it for show a table with the data.

The data are the kWh that a Photovoltaic System will generate based on the NREL information and the captured parameters.


## Features and implementations
<ul>
  <li>Using NREL-PV WATTS API</li>
  <li>Responsive Design</li>
  <li>Using GET and POST methods for the API and the data</li>
  <li>Cleaning and preparing the recieved data from the API</li>
  <li>User can download table as XLSX</li>
  <li>HTML</li>
  <li>CSS</li>
  <li>JS</li>
</ul>

## Deploy Project

#### Live version: https://kwcalc.herokuapp.com

#### Local deployment (MacOS):
<ol>
  <li>Download this project as a zip and extract it</li>
  <li>Get an <a href="https://developer.nrel.gov/signup/" target="_blank">API key</a></li> 
  <li>From your terminal install virtualenv library with the command <pre>pip install virtualenv</pre></li>
  <li>With the terminal go inside to the carpet you extract from the zip file, make a virtual environment with the command <pre>virtualenv nameOfYouEnv</pre> </li>
  <li>Activate your virtual environment <pre>source nameOfYourEnv/bin/activate</pre> </li>
  <li>Then install the requirements. In the terminal use <pre>pip install -r requirements.txt</pre></li>
  <li>Creaet a file ".env" in the app folder and edit it with <pre>API_KEY = "YourAPIKey"</pre></li>
  <li>Then use the command <pre>flask run</pre></li>
  <li>In the terminal will show app an addres like *http://127.0.0.1:5000/*, open it and the app will show up.
</ol>
