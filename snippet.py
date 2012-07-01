from flask import Flask, request, render_template, jsonify
from flask.ext.assets import Environment, Bundle

UPLOAD_FOLDER = 'tmp/'


app = Flask(__name__)
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
		print request.files
		return jsonify(
			name='test.png',
			size='10kb',
			url='none',
			)


if __name__ == "__main__":
	app.run()
