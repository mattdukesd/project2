import pandas as pd
from sqlalchemy import create_engine
import pymysql
from flask import Flask, jsonify, render_template, request, url_for

pymysql.install_as_MySQLdb()

app = Flask(__name__)

engine = create_engine("mysql://root:password@localhost:3306/schooldata")
conn = engine.connect()


@app.route("/")
def index():
	return render_template("index5.html")

@app.route("/schoolDataAll")
def dataAll():
	schoolsStuff = pd.read_sql("SELECT * FROM `school_data_all`", conn)
	schoolsStuff.set_index("Institution_Name",inplace = True)

	schoolData = schoolsStuff.to_dict(orient = "index")
	
	return jsonify(schoolData)

@app.route("/schools2010")
def data2011():
	schoolsStuff = pd.read_sql("SELECT * FROM `schools2011`", conn)
	schoolsStuff.set_index("Shit",inplace = True)
	schoolData = schoolsStuff.to_dict(orient = "index")
	
	return jsonify(schoolData)

@app.route("/schools2011")
def data2012():
	schoolsStuff = pd.read_sql("SELECT * FROM `schools2012`", conn)
	schoolsStuff.set_index("Shit",inplace = True)
	schoolData = schoolsStuff.to_dict(orient = "index")
	
	return jsonify(schoolData)

@app.route("/schools2012")
def data2013():
	schoolsStuff = pd.read_sql("SELECT * FROM `schools2013`", conn)
	schoolsStuff.set_index("Shit",inplace = True)
	schoolData = schoolsStuff.to_dict(orient = "index")
	
	return jsonify(schoolData)

@app.route("/schools2013")
def data2014():
	schoolsStuff = pd.read_sql("SELECT * FROM `schools2014`", conn)
	schoolsStuff.set_index("Shit",inplace = True)
	schoolData = schoolsStuff.to_dict(orient = "index")
	
	return jsonify(schoolData)

@app.route("/schools2014")
def data2015():
	schoolsStuff = pd.read_sql("SELECT * FROM `schools2015`", conn)
	schoolsStuff.set_index("Shit",inplace = True)
	schoolData = schoolsStuff.to_dict(orient = "index")
	
	return jsonify(schoolData)

@app.route("/schools2015")
def data2016():
	schoolsStuff = pd.read_sql("SELECT * FROM `schools2016`", conn)
	schoolsStuff.set_index("Shit",inplace = True)
	schoolData = schoolsStuff.to_dict(orient = "index")

	return jsonify(schoolData)



if __name__ == "__main__":
    app.run(debug=True)