from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from flask import Flask,jsonify

#import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/test")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    import pandas as pd
    # Find one record of data from the mongo database
    
    destination_data = mongo.db.housing_data.find()

    print ("reached test")
    realData=[]
    for eachrow in destination_data:
        print (eachrow)
        realData.append (eachrow)
    
     
        #print (realData_json)

    # Return template and data
    realEstateContent=realData
    return (realEstateContent)
  
    #return render_template("index.html", realEstateContent=realData)

# Route that will trigger the scrape function
if __name__ == "__main__":
    app.run(debug=True)