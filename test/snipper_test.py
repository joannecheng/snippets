from snipper import *
import unittest, os

class TestSnipper(unittest.TestCase):
  def setUp(self):
    self.filename = "test/test.mp3"
    self.output_dir = 'test/tmp/'

  def tearTown(self):
    os.system("rm -rf " +self.output_dir+"/*")

  def test_init(self):
    snip = Snipper(self.filename, self.output_dir)
    self.assertEqual(snip.audio_file.__class__.__name__, 'LocalAudioFile' )

  def test_analyze(self):
    snip = Snipper(self.filename, self.output_dir).analyze()

if __name__ == '__main__':
  unittest.main()
