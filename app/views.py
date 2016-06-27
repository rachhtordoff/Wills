from app import app
from flask import render_template, request
@app.route('/')
@app.route('/homepage')
def homepage():
    	return render_template('Homepage.html')
		
@app.route('/calculator-page', methods=['GET'])
def calculator():

	return render_template('calculator.html')
	
