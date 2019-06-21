import requests
import sys 
 
entrada=sys.argv[1]


if entrada=='resume':
	resp = requests.get("http://127.0.0.1:5000/")
	if resp.status_code != 200:
	    # This means something went wrong.
	    raise Exception('GET /tasks/ %s' % (resp.status_code))
	for element in resp.json():
	    print element
	print '                 Date:          Hour: Ftemp: BTemp: FCap: BCap: Mixer: Heater: Valferm ValBeer:'
	print resp.json()

if entrada=='ftank':
	resp = requests.get("http://127.0.0.1:5000/ftank")
	if resp.status_code != 200:
	    # This means something went wrong.
	    raise Exception('GET /tasks/ %s' % (resp.status_code))
	
	for element in resp.json():
	    print element
            
	     
	

	diccionari= resp.json()
	llista=diccionari['Fermentation Historic']

	for i in range(len(llista)):
		print 'Date:            Hour:   Temp:  Capacity: Mixer: Heater: Valve:'
		print llista[i]
		print "\n"

if entrada=='btank':
	resp = requests.get("http://127.0.0.1:5000/btank")
	if resp.status_code != 200:
	    # This means something went wrong.
	    raise Exception('GET /tasks/ %s' % (resp.status_code))
	for element in resp.json():
			    
		print element

	     
	diccionari= resp.json()
	llista=diccionari['Beer Historic']
	for i in range(len(llista)):
		print 'Date:        Hour:   Temp:  Capacity:  Valve:'
		print llista[i]
		print "\n"
if entrada=='relays':
		resp = requests.get("http://127.0.0.1:5000/relays")
		if resp.status_code != 200:
		    # This means something went wrong.
		    raise Exception('GET /tasks/ %s' % (resp.status_code))
		for element in resp.json():
		    print element
		print resp.json()

if entrada=='heater':
	entrada2=sys.argv[2]
	if entrada2=='ON' or entrada2=='on' or entrada2=='On':
		data = {"Heater": 'ON' }
		response = requests.post("http://127.0.0.1:5000/heater",json=data)
		
	elif entrada2=='OFF'or entrada2=='off' or entrada2=='Off':
		data = {"Heater": 'OFF' }
		response = requests.post("http://127.0.0.1:5000/heater",json=data)
	else:
		print 'the input status must be heater and: On, ON, on, Off, OFF or off.'

if entrada=='mixer':
	entrada2=sys.argv[2]
	if entrada2=='ON' or entrada2=='on' or entrada2=='On':
		data = {"Mixer": 'ON' }
		response = requests.post("http://127.0.0.1:5000/mixer",json=data)
		
	elif entrada2=='OFF'or entrada2=='off' or entrada2=='Off':
		data = {"Mixer": 'OFF' }
		response = requests.post("http://127.0.0.1:5000/mixer",json=data)
	else:
		print 'the input status must be mixer and: On, ON, on, Off, OFF or off.'

if entrada=='valbeer':
	entrada2=sys.argv[2]
	if entrada2=='ON' or entrada2=='on' or entrada2=='On':
		data = {"Valbeer": 'ON' }
		response = requests.post("http://127.0.0.1:5000/valbeer",json=data)
		
	elif entrada2=='OFF'or entrada2=='off' or entrada2=='Off':
		data = {"Valbeer": 'OFF' }
		response = requests.post("http://127.0.0.1:5000/valbeer",json=data)
	else:
		print 'the input status must be valbeer and: On, ON, on, Off, OFF or off.'


if entrada=='valferm':
	entrada2=sys.argv[2]
	if entrada2=='ON' or entrada2=='on' or entrada2=='On':
		data = {"Valferm": 'ON' }
		response = requests.post("http://127.0.0.1:5000/valferm",json=data)
		
	elif entrada2=='OFF'or entrada2=='off' or entrada2=='Off':
		data = {"Valferm": 'OFF' }
		response = requests.post("http://127.0.0.1:5000/valferm",json=data)
	else:
		print 'the input status must be valferm and: On, ON, on, Off, OFF or off.'

