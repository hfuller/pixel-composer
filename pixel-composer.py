from flask import Flask, redirect, request
import json
import serial
from enum import Enum

class Mode(Enum):
    REPEAT = 1
    ONE_TO_ONE = 2

mode = Mode.REPEAT
length = 24
pattern_length = 3

app = Flask(__name__)

@app.route('/')
def redir():
    return redirect("/static/index.html")

@app.route('/settings',methods=['POST'])
def set_settings():
    global mode,length,pattern_length
    print "Setting settings"
    print request.form
    if request.form.get('mode') != None:
        print "Setting mode"
        mode = Mode[request.form['mode']]
    if request.form.get('length') != None:
        print "Setting length"
        length = int(request.form['length'])
    if request.form.get('pattern_length') != None:
        print "Setting pattern_length"
        pattern_length = int(request.form['pattern_length'])
    return json.dumps(True)
@app.route('/settings',methods=['GET'])
def get_settings():
    return json.dumps({
        "mode":str(mode).split('.')[-1], #so just like, "REPEAT" or whatever
        "length":length,
        "pattern_length":pattern_length
        })

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=2667)


