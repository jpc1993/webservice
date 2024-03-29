#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, render_template, redirect
import sqlite3
from datetime import date, datetime
import requests


app = Flask(__name__)



@app.route('/', methods=['GET'])
def get_resume():
   	url = 'http://127.0.0.1:5000/'
    	response = requests.get(url)
	data=response.json()
	llista=data['Resume']
	return render_template('page.html', llista=llista)



@app.route('/ftank', methods=['GET'])
def get_ftank():
	url = 'http://127.0.0.1:5000/ftank'
    	response = requests.get(url)
	data=response.json()
	llista=data['Fermentation Historic']
 	return render_template('fermhistoric.html', llista=llista)

@app.route('/btank', methods=['GET'])
def get_btank():
	url = 'http://127.0.0.1:5000/btank'
    	response = requests.get(url)
	data=response.json()
	llista=data['Beer Historic']
   	return render_template('beerhistoric.html', llista=llista)
	
@app.route('/relays', methods=['GET','POST'])
def get_relays():
	url = 'http://127.0.0.1:5000/relays'
 	response = requests.get(url)
	data=response.json()
	llista=data['Relays status']
	

	if request.method == "GET":
		
		return render_template('relays.html', llista=llista)	


	elif request.method == "POST":
		
	    	response = requests.post(url)
		
		hsname = request.form.get("Heater")
		
		if hsname== 'OFFH':
				data = {"Heater": 'OFF' }
				response = requests.post("http://127.0.0.1:5000/heater",json=data)
		if hsname== 'ONH':
				data = {"Heater": 'ON' }
				response = requests.post("http://127.0.0.1:5000/heater",json=data)
	
				
		hsname = request.form.get("Mixer")
		
		if hsname== 'OFFM':
				data = {"Mixer": 'OFF' }
				response = requests.post("http://127.0.0.1:5000/mixer",json=data)
		if hsname== 'ONM':
				data = {"Mixer": 'ON' }
				response = requests.post("http://127.0.0.1:5000/mixer",json=data)
				

		hsname = request.form.get("Beerval")
		if hsname== 'OFFB':
				data = {"Valbeer": 'OFF' }
				response = requests.post("http://127.0.0.1:5000/valbeer",json=data)
		if hsname== 'ONB':
				data = {"Valbeer": 'ON' }
				response = requests.post("http://127.0.0.1:5000/valbeer",json=data)
		

		hsname = request.form.get("Fermval")
		if hsname== 'OFFF':
		   		data = {"Valferm": 'OFF' }
				response = requests.post("http://127.0.0.1:5000/valferm",json=data)
		if hsname== 'ONF':
				data = {"Valferm": 'ON' }
				response = requests.post("http://127.0.0.1:5000/valferm",json=data)		

		
		
		return render_template('relays.html', llista=llista)



	
		

























@app.errorhandler(404)
def not_found(error):
   	 return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    	return make_response(jsonify({'error': 'Bad request'}), 400)


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5001, debug=True)
