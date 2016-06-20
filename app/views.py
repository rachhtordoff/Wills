from app import app
from flask import render_template
@app.route('/')
@app.route('/Homepage')
def index():
    	return render_template('Homepage.html')