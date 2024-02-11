import json
import random
import os

def load_flashcards(filename):
    with open(filename, 'r') as file:
        flashcards = json.load(file)
    
    # Check if each flashcard has a confidence_score attribute, if not, add it with a default value of 50
    for card in flashcards:
        if 'confidence_score' not in card:
            card['confidence_score'] = 50
    
    return flashcards

def update_flashcards(filename, flashcards):
    with open(filename, 'w') as file:
        json.dump(flashcards, file, indent=4)

def update_confidence_score(flashcards, flashcard_index, rating):
    if rating == 0:
        flashcards[flashcard_index]['confidence_score'] = 50
    else:
        confidence_score = flashcards[flashcard_index].get('confidence_score', 50)
        if rating == 1:
            confidence_score = max(1, confidence_score - 10)
        elif rating == 3:
            confidence_score = min(100, confidence_score + 10)
        flashcards[flashcard_index]['confidence_score'] = confidence_score
    return flashcards

def display_random_flashcard(flashcards):
    # Calculate weights for random choice based on inverse of confidence score
    weights = [1 / card['confidence_score'] for card in flashcards]

    # Choose random flashcard with weights inversely proportional to confidence score
    random_flashcard = random.choices(flashcards, weights=weights)[0]

    print("\nQuestion:", random_flashcard['question'])
    input("\nPress Enter to reveal the answer...")
    print("\nAnswer:", random_flashcard['answer'])
    
    rating = int(input("\nRate your confidence level (0 to reset, 1 for low, 2 for medium, 3 for high): "))
    flashcard_index = flashcards.index(random_flashcard)
    flashcards = update_confidence_score(flashcards, flashcard_index, rating)

    # Update flashcards JSON file
    update_flashcards(filename, flashcards)

# Replace 'flashcards.json' with the path to your JSON file
filename = 'flashcards.json'

# Load flashcards from the JSON file
flashcards = load_flashcards(filename)

# Continuously display random flashcards until the user decides to exit
while True:
    display_random_flashcard(flashcards)
    continue_or_exit = input("\nPress Enter to continue or type 'exit' to quit: ")
    if continue_or_exit.lower() == 'exit':
        break
