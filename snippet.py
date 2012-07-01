import os
from flask import Flask, request, render_template, jsonify
from flask.ext.assets import Environment, Bundle
from werkzeug import secure_filename

# TODO: refactor this goddamn thing

UPLOAD_FOLDER = 'tmp/'
ALLOWED_EXTENSIONS = set(['mp3', 'wav'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
assets = Environment(app)
js = Bundle('vendor/js/jquery-1.7.2.min.js',
	'vendor/js/jquery-ui-1.8.21.custom.min.js',
	'vendor/js/jquery.iframe-transport.js',
	'vendor/js/jquery.fileupload.js',
    filters='rjsmin', output='gen/packed.js')

coffee = Bundle('assets/js/*.coffee',
    filters="coffeescript", output="gen/application.js")

sass = Bundle('assets/css/*.sass',
	filters="sass", output="gen/application.css")

assets.register('js_all', js)
assets.register('coffee_all', coffee)
assets.register('css_all', sass)

@app.route("/", methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

	if request.method == 'POST':
		print 'POST'
		input_file = request.files.getlist('files[]')[0]
		if input_file and allowed_file(input_file.filename):
			filename = secure_filename(input_file.filename)
			input_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return jsonify(
				name=filename,
				size='10kb',
				url='none',
				)

def allowed_file(filename):
	return '.' in filename and \
		filename.split('.')[-1] in ALLOWED_EXTENSIONS

if __name__ == "__main__":
	app.run()
