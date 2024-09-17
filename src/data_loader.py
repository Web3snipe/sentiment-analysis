# src/data_loader.py

def load_reviews(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reviews = file.readlines()
    return [review.strip() for review in reviews]