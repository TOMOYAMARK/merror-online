from bottle import route, run, template
from bottle import static_file
import subprocess


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./gens')

@route('/genup')
def genup():
    subprocess.check_call(["python3","genupchar.py"])

@route('/trans')
def genup():
    subprocess.check_call(["python3","customupchar.py"])


run(host='223.218.26.97', port=8080, debug=True)
