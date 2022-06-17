#!flask/bin/python
#export OTEL_SERVICE_NAME=photogallery-web
#opentelemetry-instrument --traces_exporter jaeger_thrift python3 app.py
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask import render_template, redirect
import os    
import time
import datetime
import json
import requests

app = Flask(__name__, static_url_path="")


@app.route('/', methods=['GET'])
def view_photo():
    photo_id=1            
    details = getPhotoDetails(photo_id)
    items=[]
    
    photo=details
    items.append(photo)
    tags=items[0]['Tags'].split(',')    
    
    return render_template('photodetail.html', photo=items[0], tags=tags)

def getPhotoDetails(photo_id):
    photo={}
    photo['PhotoID'] = photo_id
    photo['CreationTime'] = "April 30, 2022"
    photo['Title'] = "Bird"
    photo['Description'] = "Yellow bird sitting on a tree"
    photo['Tags'] = "bird,tree,nature,forest"
    photo['URL'] = "/media/bird.jpg" 
    return photo

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, use_reloader=False)
