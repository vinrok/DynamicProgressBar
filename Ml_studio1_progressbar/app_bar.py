# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:06:56 2019

@author: VC5052254
"""

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import webbrowser
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SECRET_KEY'] =  os.urandom(24)


############################################################################################
########### POST API for Exploring Dataset
############################################################################################
#POST API with body parameters as filename
@app.route("/explore", methods=['POST'])
@cross_origin(supports_credentials=True)
def exploreDatasetApi():
#    data = dict(request.files)
#    print (data)
    request_obj = request.files["file"]
    print(request_obj)
    response ={'status' : True}
#    filename = 'Output/test.csv'
#    pd.DataFrame(objArray).to_csv(filename, index=False)
#        
#    dataset = pd.read_csv(filename)
#    
#    session_dict['dataset'] = dataset
#    session_dict['remove_dup_df'] = dataset.copy()
#    cols = dataset.columns
#    num_cols = dataset._get_numeric_data().columns
#    
#    #Explore Dataset
#    dataset_info = explore_dataset(dataset, num_cols, cols)
#    
#    response={
#            'dataset_info' : dataset_info
#            }
    return jsonify(response)
#    return response


if __name__ == '__main__':
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open('file://' + os.path.realpath('progress.html'))
    app.run(port=5000)
