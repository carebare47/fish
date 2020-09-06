from flask import Flask, request, Response
import subprocess
import os
devnull = open(os.devnull, 'w')

app = Flask(__name__)

@app.route('/')
def root():
#	return render_template('page.html')
	return return_main_page()

def return_main_page():
	with open('page.html') as f:
		content = f.read()
	return content

@app.route('/', methods=['POST'])
def submit():
#	print(request)
#	print(request.form)
#	print(request.form['text'])
	text = request.form['text']
	print(text)
	subprocess.call(['espeak', u'"{}"'.format(text)], stdout=devnull, stderr=devnull)
#	return Response(status_code=200)
	return return_main_page()

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
