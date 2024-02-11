import json
import random

def load_flashcards(filename):
    with open(filename, 'r') as file:
        flashcards = json.load(file)
    return flashcards

def add_confidence_score(flashcards):
    for flashcard in flashcards:
        # Assign an initial confidence score of 50
        flashcard['confidence_score'] = 50
    return flashcards

def display_random_flashcard(flashcards):
    # Weighted random choice based on confidence scores with slight reduction for higher scores
    confidence_scores = [flashcard['confidence_score'] for flashcard in flashcards]
    total_confidence = sum(confidence_scores)
    probabilities = [score / total_confidence for score in confidence_scores]
    random_flashcard = random.choices(flashcards, weights=probabilities)[0]
    
    print("\nQuestion:", random_flashcard['question'])
    input("\nPress Enter to reveal the answer...")
    print("\nAnswer:", random_flashcard['answer'])
    return random_flashcard

def update_confidence_score(flashcard, confidence_score):
    # Bound the confidence score between 1 and 100
    flashcard['confidence_score'] = max(1, min(100, confidence_score))
    return flashcard

# Replace 'flashcards.json' with the path to your JSON file
filename = 'output.json'

# Load flashcards from the JSON file
flashcards = load_flashcards(filename)

# Add confidence scores to each flashcard
flashcards_with_confidence = add_confidence_score(flashcards)

while True:
    # Display a random flashcard weighted by confidence scores
    random_flashcard = display_random_flashcard(flashcards_with_confidence)
    
    confidence_score = int(input("\nHow confident do you feel about this flashcard? (1: Low, 2: Medium, 3: High): "))
    
    if confidence_score == 1:
        random_flashcard = update_confidence_score(random_flashcard, random_flashcard['confidence_score'] - 10)
    elif confidence_score == 3:
        random_flashcard = update_confidence_score(random_flashcard, random_flashcard['confidence_score'] + 10)
    
    repeat = input("\nDo you want to continue? (yes/no): ")
    if repeat.lower() != 'yes':
        break
