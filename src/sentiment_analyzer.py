# src/sentiment_analyzer.py

import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.tokenize import word_tokenize

class SentimentAnalyzer:
    def __init__(self):
        nltk.download('movie_reviews')
        nltk.download('punkt')
        self.classifier = self.train_classifier()

    def train_classifier(self):
        documents = [(list(movie_reviews.words(fileid)), category)
                     for category in movie_reviews.categories()
                     for fileid in movie_reviews.fileids(category)]
        
        # Shuffle the documents
        import random
        random.shuffle(documents)

        all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
        word_features = list(all_words.keys())[:2000]

        def document_features(document):
            document_words = set(document)
            features = {}
            for word in word_features:
                features[f'contains({word})'] = (word in document_words)
            return features

        featuresets = [(document_features(d), c) for (d, c) in documents]
        train_set, test_set = featuresets[100:], featuresets[:100]
        classifier = NaiveBayesClassifier.train(train_set)

        print(f"Classifier accuracy: {accuracy(classifier, test_set)}")
        return classifier

    def analyze_sentiment(self, text):
        tokens = word_tokenize(text.lower())
        features = self.document_features(tokens)
        sentiment = self.classifier.classify(features)
        return sentiment

    def document_features(self, document):
        document_words = set(document)
        features = {}
        all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
        word_features = list(all_words.keys())[:2000]
        for word in word_features:
            features[f'contains({word})'] = (word in document_words)
        return features