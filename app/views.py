from app import app, JsonParser
from flask import render_template, request, session,  url_for, redirect, jsonify, json

def sumSessionCounter():
  try:
	session['name'] = request.form['username']
  except KeyError:
    session['name'] = 'error'


@app.route('/')
@app.route('/homepage')
def homepage():
    	return render_template('Homepage.html')
		
@app.route('/calculator-page', methods=['GET'])
def calculator():

	return render_template('calculator.html')
	
	
@app.route('/signup', methods=['POST'])
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
	
	return jsonify(user=rule_new)

@app.route('/executors', methods=['POST'])
def addExecutors():	
	exfname =  request.form['firstname2']
	exlname = request.form['lastname2']
	exaddress = request.form['address2']
	exe = {}
	exe['fname'] = exfname
	exe['lname'] = exlname
	exe['address'] = exaddress
	
	return jsonify(exe=exe )

@app.route('/guardians', methods=['POST'])
def addGuardian():	
	Guardian =  request.form['gender']
	guard = {}
	guard ['option'] = Guardian
	return jsonify(guard=guard )
	
	
@app.route('/session')
def session():
    if 'username' in session:
      username = session['username']
    return render_template('calculator.html', username=username)
										   
def create_form(username, lname, email, address):


	return rule_new