import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# main.py


from src.sentiment_analyzer import SentimentAnalyzer
from src.data_loader import load_reviews

def main():
    analyzer = SentimentAnalyzer()
    
    # Analyze some sample texts
    sample_texts = [
        "This movie was fantastic! I really enjoyed it.",
        "The food at the restaurant was terrible and the service was even worse.",
        "I'm feeling neutral about this product. It's neither good nor bad."
    ]
    
    for text in sample_texts:
        sentiment = analyzer.analyze_sentiment(text)
        print(f"Text: {text}")
        print(f"Sentiment: {sentiment}\n")
    
    # Analyze reviews from a file
    reviews = load_reviews('data/sample_reviews.txt')
    for review in reviews:
        sentiment = analyzer.analyze_sentiment(review)
        print(f"Review: {review}")
        print(f"Sentiment: {sentiment}\n")

if __name__ == "__main__":
    main()