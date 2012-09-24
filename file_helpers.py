import os, sys

TMP_FOLDER = 'tmp/'
UPLOAD_FOLDER = 'upload/'
ALLOWED_EXTENSIONS = set(['mp3', 'wav'])

def initialize_folders():
	for folder in [TMP_FOLDER, UPLOAD_FOLDER]:
		initialize_folder(folder)

def initialize_folder(folder):
	try:
		os.mkdir(folder)
	except:
		pass

def allowed_file(filename):
	return '.' in filename and \
		filename.split('.')[-1] in ALLOWED_EXTENSIONS


