import echonest.audio as audio
import sys, os

class Snipper:

	def __init__(self, filename, target_dirname):
		self.filename = filename
		self.target_dirname = target_dirname
		self.audio_file = audio.LocalAudioFile(filename)

	def analyze(self):
		dir_name = self.target_dirname 
		beats = self.audio_file.analysis.beats

		i = 0
		for beat in beats:
			beat.encode(dir_name+"beat_"+str(i)+".mp3")
			i += 1
