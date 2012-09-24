import os, shutil, sys
from flask import Flask, request, render_template, jsonify, send_from_directory
from flask.ext.assets import Environment, Bundle
from werkzeug import secure_filename
from snipper import *
import file_helpers

# TODO: refactor this goddamn thing

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = file_helpers.UPLOAD_FOLDER
app.config['TMP_FOLDER'] = file_helpers.TMP_FOLDER
app.config['ALLOWED_EXTENSIONS'] = file_helpers.ALLOWED_EXTENSIONS
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

# assets
assets = Environment(app)
js = Bundle('vendor/js/jquery-1.7.2.min.js',
	'vendor/js/jquery-ui-1.8.21.custom.min.js',
	'vendor/js/jquery.iframe-transport.js',
	'vendor/js/jquery.fileupload.js',
  'vendor/js/underscore.js',
  'vendor/js/backbone.js',
    filters='rjsmin', output='gen/packed.js')

coffee = Bundle('assets/js/*.coffee',
    filters="coffeescript", output="gen/application.js")

sass = Bundle('assets/css/*.sass',
	filters="sass", output="gen/application.css")

assets.register('js_all', js)
assets.register('coffee_all', coffee)
assets.register('css_all', sass)

# initialize folders
file_helpers.initialize_folders()

@app.route("/", methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

	if request.method == 'POST':
		input_file = request.files.getlist('files[]')[0]
		if input_file and file_helpers.allowed_file(input_file.filename):
			filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(input_file.filename))
			saved_file = input_file.save(filepath)
			try:
				Snipper(filepath, app.config['TMP_FOLDER']).analyze()
				return jsonify(name=input_file.filename, size=input_file.content_length,url='none', uploaded_url ='beats/')
			except Exception:
				app.logger.error(Exception)

@app.route('/beats')
def uploaded():
	files = os.listdir(app.config['TMP_FOLDER'])
	return jsonify({'beat_url': 'beats/', 'files' : files })

@app.route('/beats/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['TMP_FOLDER'], filename)

if __name__ == "__main__":
	app.run()
