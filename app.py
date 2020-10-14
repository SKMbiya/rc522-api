#!rc522-api-env/bin/python
from flask import Flask, jsonify
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello, World!"

@app.route('/mfrc522/api/read')
def read_card():
	reader = SimpleMFRC522()
	dataObject = {}
	try:
		id, text = reader.read()
		print(text)
		dataObject = {'id':id, 'text':text}
	finally:
		GPIO.cleanup()
	return jsonify(dataObject)

@app.route('/mfrc522/api/write/<data>')
def write_card(data):
	reader = SimpleMFRC522()
	dataObject = {}
	try:
		id, text = reader.read()
		reader.write(data)
		dataObject = {'id':id, 'data':data}
	finally:
		GPIO.cleanup()
	return jsonify(dataObject)
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8090, debug=True)
