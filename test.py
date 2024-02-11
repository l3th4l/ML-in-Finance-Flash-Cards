import json
import random

def load_flashcards(filename):
    with open(filename, 'r') as file:
        flashcards = json.load(file)
    return flashcards

def display_random_flashcards(flashcards, num_flashcards=5):
    random_flashcards = random.sample(flashcards, min(num_flashcards, len(flashcards)))
    for flashcard in random_flashcards:
        print("Question:", flashcard['question'])
        print("Answer:", flashcard['answer'])
        print()

# Replace 'flashcards.json' with the path to your JSON file
filename = 'output.json'

# Load flashcards from the JSON file
flashcards = load_flashcards(filename)

# Display 5 random flashcards
display_random_flashcards(flashcards)