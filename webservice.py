#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
import sqlite3
from datetime import date, datetime
import requests


app = Flask(__name__)



@app.route('/', methods=['GET'])
def get_resume():
	conn = sqlite3.connect('lleidabeer.db')
	print("Opened database successfully")	
	llista =[]
 	
	cursor = conn.execute("SELECT tdate,ttime,tempbeer,tempferm,capferm,capbeer,mixer,heater,valferm,valbeer FROM sensors ORDER BY tdate desc,ttime desc LIMIT 1")
	
	for row in cursor:
		llista_append = llista.append(row) 
	conn.close()
	return jsonify({'Resume': llista})
	
	

@app.route('/ftank', methods=['GET'])
def get_ftank():
	conn = sqlite3.connect('lleidabeer.db')
	print("Opened database successfully")	
	llista =[]
 	
	cursor = conn.execute("SELECT tdate,ttime,tempferm,capferm,mixer,heater,valferm FROM sensors ORDER BY tdate asc,ttime asc ")
	
	for row in cursor:
		llista_append = llista.append(row) 
	conn.close()
	return jsonify({'Fermentation Historic': llista})

@app.route('/btank', methods=['GET'])
def get_btank():
	conn = sqlite3.connect('lleidabeer.db')
	print("Opened database successfully")	
	llista =[]
 	
	cursor = conn.execute("SELECT tdate,ttime,tempbeer,capbeer,valbeer FROM sensors ORDER BY tdate asc,ttime asc ")
	
	for row in cursor:
		llista_append = llista.append(row) 
	conn.close()
	return jsonify({'Beer Historic': llista})

@app.route('/relays', methods=['GET'])
def get_relays():
	

	if request.method == "GET":
		conn = sqlite3.connect('lleidabeer.db')
		print("Opened database successfully")	
		llista =[]
	 	
		cursor = conn.execute("SELECT tdate,ttime,mixer,heater,valferm,valbeer FROM sensors ORDER BY tdate desc,ttime desc LIMIT 1")
		
		for row in cursor:
			llista_append = llista.append(row) 
		conn.close()
		return jsonify({'Relays status': llista})
	
	

def updatesql(actuador, estat):
		conn = sqlite3.connect('lleidabeer.db')
	 	llista =[]
		cursor = conn.execute("SELECT  tdate,ttime,tempbeer,tempferm,capferm,capbeer,mixer,heater,valferm,valbeer from sensors")	
		for row in cursor:
				llista.append(row)
			
		llista = llista[-1:]

                time = datetime.now().strftime("%H:%M:%S")
		data= date.today()		
 		temperaturabirra = llista[0][2]
		temperaturaferm = llista[0][3]
		capaciferm = llista[0][4]
                capacibeer = llista[0][5]
                mix = llista[0][6]
                heat = llista[0][7]
                valvuferm = llista[0][8]
                valvubeer = llista[0][9]
                
		if actuador=='mixer':
			mix= estat 
		if actuador=='heater':
			heat= estat 
		if actuador=='valbeer':
			valvubeer= estat 							
		if actuador=='valferm':
			valvuferm= estat 
			
			


		cursor = conn.execute("insert into sensors (tdate,ttime,tempbeer,tempferm,capferm,capbeer,mixer,heater,valferm,valbeer) values (?,?,?,?,?,?,?,?,?,?)",(data,time,temperaturabirra,temperaturaferm,capaciferm,capacibeer,mix,heat,valvuferm,valvubeer))
		

		conn.commit()
		conn.close()	
		return

@app.route('/heater', methods=['POST'])
def heater():
   	posts=[]
    	post=request.json['Heater']
    	posts.append(post)
    	estat=posts[0]
	a=updatesql('heater',estat)
    	return jsonify({'post': post}), 201

@app.route('/mixer', methods=['POST'])
def mixer():
   	posts=[]
    	post=request.json['Mixer']
    	posts.append(post)
    	estat=posts[0]
	a=updatesql('mixer',estat)
    	return jsonify({'post': post}), 201

@app.route('/valferm', methods=['POST'])
def valferm():
   	posts=[]
    	post=request.json['Valferm']
    	posts.append(post)
    	estat=posts[0]
	a=updatesql('valferm',estat)
    	return jsonify({'post': post}), 201

@app.route('/valbeer', methods=['POST'])
def valbeer():
   	posts=[]
    	post=request.json['Valbeer']
    	posts.append(post)
    	estat=posts[0]
	a=updatesql('valbeer',estat)
    	return jsonify({'post': post}), 201




if __name__ == '__main__':
	app.run(debug=True)

