from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector("I am glad this happened")['dominant_emotion']
        result2 = emotion_detector("I am really mad about this")['dominant_emotion']
        result3 = emotion_detector("I feel disgusted just hearing about this")['dominant_emotion']
        result4 = emotion_detector("I am so sad about this")['dominant_emotion']
        result5 = emotion_detector("I am really afraid that this will happen")['dominant_emotion']
        self.assertEqual(result1, "joy")
        self.assertEqual(result2, "anger")
        self.assertEqual(result3, "disgust")
        self.assertEqual(result4, "sadness")
        self.assertEqual(result5, "fear")

unittest.main()