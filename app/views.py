from app import app
from flask import render_template, request, session,  url_for, redirect

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
    sumSessionCounter()

    return redirect(url_for('message'))

@app.route('/message')
def message():
    if not 'name' in session:
        return abort(403)
    return render_template('calculator.html', username=session['name'])
										   

if __name__ == '__main__':
    app.run()