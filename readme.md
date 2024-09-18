# Sentiment Analysis Tool

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Testing](#testing)
8. [How It Works](#how-it-works)
9. [Future Improvements](#future-improvements)
10. [Contributing](#contributing)
11. [License](#license)

## Introduction

This Sentiment Analysis Tool is a Python-based application that uses Natural Language Processing (NLP) techniques to analyze and classify text sentiment. It's designed to determine whether a given piece of text (such as a movie review or product feedback) expresses a positive or negative sentiment.

This project demonstrates proficiency in:
- Natural Language Processing (NLP)
- Machine Learning classification techniques
- Python programming
- Project structure and organization
- Test-driven development

## Features

- Sentiment analysis of text input (classifies as positive or negative)
- Trained on a dataset of movie reviews for versatile sentiment detection
- Ability to analyze individual texts or bulk process from a file
- Simple and intuitive Python API for easy integration into other projects

## Project Structure

```
sentiment_analysis_tool/
├── src/
│   ├── __init__.py
│   ├── sentiment_analyzer.py
│   └── data_loader.py
├── data/
│   └── sample_reviews.txt
├── tests/
│   ├── __init__.py
│   └── test_sentiment_analyzer.py
├── requirements.txt
├── README.md
└── main.py
```

- `src/`: Source code directory
  - `sentiment_analyzer.py`: Core sentiment analysis functionality
  - `data_loader.py`: Utility for loading text data
- `data/`: Directory for input data files
- `tests/`: Unit tests
- `main.py`: Entry point for running the sentiment analysis tool
- `requirements.txt`: Project dependencies

## Requirements

- Python 3.7+
- NLTK
- pandas
- scikit-learn

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Web3snipe/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. To run the main script with sample texts and file input:
   ```
   python main.py
   ```

2. To use the SentimentAnalyzer in your own Python script:
   ```python
   from src.sentiment_analyzer import SentimentAnalyzer

   analyzer = SentimentAnalyzer()
   sentiment = analyzer.analyze_sentiment("This movie was fantastic!")
   print(f"Sentiment: {sentiment}")
   ```

## Testing

Run the unit tests using:
```
python -m unittest discover tests
```

## How It Works

1. **Data Preparation**: The tool uses the NLTK movie_reviews corpus for training.

2. **Feature Extraction**: It extracts features from the text using a bag-of-words approach, considering the 2000 most frequent words.

3. **Model Training**: A Naive Bayes classifier is trained on these features.

4. **Sentiment Analysis**: New text is processed similarly, and the trained model predicts its sentiment.

## Future Improvements

- Implement more advanced NLP techniques (e.g., word embeddings)
- Add support for multi-class sentiment (e.g., very negative, negative, neutral, positive, very positive)
- Create a web interface for easy use
- Optimize performance for larger datasets
- Add support for multiple languages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
