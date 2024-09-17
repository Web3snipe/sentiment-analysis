# tests/test_sentiment_analyzer.py

import unittest
from src.sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    def test_positive_sentiment(self):
        text = "This movie is fantastic! I really enjoyed it."
        sentiment = self.analyzer.analyze_sentiment(text)
        self.assertEqual(sentiment, 'pos')

    def test_negative_sentiment(self):
        text = "This book was terrible. I couldn't even finish it."
        sentiment = self.analyzer.analyze_sentiment(text)
        self.assertEqual(sentiment, 'neg')

if __name__ == '__main__':
    unittest.main()