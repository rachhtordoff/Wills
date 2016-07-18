from app import app, JsonParser
from flask import render_template, request, session,  url_for, redirect, jsonify, json


def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

@app.route('/')
@app.route('/homepage')
def homepage():
    	return render_template('Homepage.html')
		
@app.route('/calculator-page', methods=['GET', 'POST'])
def step1():
		if request.method == 'GET':
			return render_template ('calculator.html')
		
		if request.method == 'POST':
			sumSessionCounter()
			username = request.form['username']
			lname = request.form['lname']
			email = request.form['email']
			address = request.form['address']
			rule_new = {}
			rule_new['username'] = username
			rule_new['lname'] = lname
			rule_new['email'] = email
			rule_new['address'] = address
			form_data = {"form1": rule_new, "form2": None, "Form3":None} 
		return render_template ('calculator.html', session = form_data)
	

def step3(session):
		if request.method == 'GET':
			return render_template ('calculator.html')
	
def signup():

		username = request.form['username']
		lname = request.form['lname']
		email = request.form['email']
		address = request.form['address']
		rule_new = {}
		rule_new['username'] = username
		rule_new['lname'] = lname
		rule_new['email'] = email
		rule_new['address'] = address
		session['name'] = rule_new
		return redirect(url_for('calculator2'))


def addExecutors():	
	exfname =  request.form['firstname2']
	exlname = request.form['lastname2']
	exaddress = request.form['address2']
	exe = {}
	exe['fname'] = exfname
	exe['lname'] = exlname
	exe['address'] = exaddress
	
	return jsonify(exe=exe )

def addGuardian():	
	Guardian =  request.form['gender']
	exe = {}
	exe['Guardian'] = Guar
	exe['lname'] = exlname
	exe['address'] = exaddress
	
	return jsonify(exe=exe )
	
										   
def create_form(username, lname, email, address):


	return rule_new
	
""""def validate():"""