from snipper import *
import unittest

class TestSnipper(unittest.TestCase):
  def setUp(self):
    self.filename = "test/test.mp3"

  def test_init(self):
    snip = Snipper(self.filename)
    self.assertEqual(snip.audio_file.__class__.__name__, 'LocalAudioFile' )

if __name__ == '__main__':
  unittest.main()
