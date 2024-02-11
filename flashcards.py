import json
import random
import os

def load_flashcards(filename):
    with open(filename, 'r') as file:
        flashcards = json.load(file)
    return flashcards

def initialize_flashcards(flashcards):
    if not os.path.exists("confidence_scores.json"):
        with open("confidence_scores.json", "w") as file:
            initial_confidence_scores = {i: 50 for i, _ in enumerate(flashcards)}
            json.dump(initial_confidence_scores, file)

def load_confidence_scores():
    if not os.path.exists("confidence_scores.json"):
        return {}
    with open("confidence_scores.json", "r") as file:
        return json.load(file)

def update_confidence_score(confidence_score, rating):
    if rating == 1:
        confidence_score = max(1, confidence_score - 10)
    elif rating == 3:
        confidence_score = min(100, confidence_score + 10)
    return confidence_score

def display_random_flashcard(flashcards):
    # Load confidence scores
    confidence_scores = load_confidence_scores()

    # Assign confidence scores to flashcards
    for i, card in enumerate(flashcards):
        if i in confidence_scores:
            card['confidence_score'] = confidence_scores[i]
        else:
            card['confidence_score'] = 50

    # Choose random flashcard based on confidence scores
    random_flashcard = random.choices(flashcards, weights=[1 / card['confidence_score'] for card in flashcards])[0]

    print("\nQuestion:", random_flashcard['question'])
    input("\nPress Enter to reveal the answer...")
    print("\nAnswer:", random_flashcard['answer'])
    rating = int(input("\nRate your confidence level (1 for low, 2 for medium, 3 for high): "))
    confidence_scores[flashcards.index(random_flashcard)] = update_confidence_score(random_flashcard['confidence_score'], rating)

    # Save confidence scores
    with open("confidence_scores.json", "w") as file:
        json.dump(confidence_scores, file)

# Replace 'flashcards.json' with the path to your JSON file
filename = 'flashcards.json'

# Load flashcards from the JSON file
flashcards = load_flashcards(filename)

# Initialize flashcards with confidence scores
initialize_flashcards(flashcards)

# Continuously display random flashcards until the user decides to exit
while True:
    display_random_flashcard(flashcards)
    continue_or_exit = input("\nPress Enter to continue or type 'exit' to quit: ")
    if continue_or_exit.lower() == 'exit':
        break
