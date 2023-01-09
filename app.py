import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import json
from datetime import datetime,date,timedelta
import pandas as pd
import category_encoders
from category_encoders import TargetEncoder, CountEncoder
import adal
import time
import uuid
from azure.identity import ClientSecretCredential
from msrestazure.azure_active_directory import AADTokenCredentials
import joblib
from operator import itemgetter
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET

app = Flask(__name__)


@app.route('/snow_ettr_more/',methods=['POST'])
def snow_ettr_more():
    print('@@@@@@@@@@@@@ Testing the code for SOAP API !@@@@@@@@@@@@@@@@@')
    print(request)
    args=request.get_json()
    print(args)
    case_number = args['queryResult']["parameters"]["any"]
    return {"fulfillmentText": "2 hrs"}
    
    
               
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    #app.run(debug = True)