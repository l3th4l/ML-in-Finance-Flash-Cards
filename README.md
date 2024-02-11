# Flashcards Program

## Overview
The Flashcards Program is a Python script designed to help users study a set of flashcards stored in a JSON file. It allows users to randomly display flashcards, reveal answers, rate their confidence level for each flashcard, and update the confidence scores accordingly.

## Prerequisites
- Python 3.x installed on your system

## Getting Started
1. Clone this repository to your local machine by executing the following command in your terminal or command prompt:
    ```
    git clone <repository_url>
    ```
    Replace `<repository_url>` with the URL of this GitHub repository.

2. Navigate to the directory containing the cloned repository.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the cloned repository.
3. Run the script by executing the following command:
    ```
    python flashcards.py
    ```
4. Follow the on-screen prompts to interact with the program:
   - Press Enter to display a random flashcard.
   - After reading the question, press Enter again to reveal the answer.
   - Rate your confidence level for the flashcard:
        - Enter "1" for low confidence.
        - Enter "2" for medium confidence.
        - Enter "3" for high confidence.
   - The program will update the confidence score of the flashcard based on your rating.
   - You can choose to continue or exit the program after each flashcard.

## Notes
- The flashcards are stored in the `flashcards.json` file included in the repository.
- The confidence score is initially set to 50 (average confidence) for each flashcard.
- When rating your confidence level, selecting "1" decreases the confidence score by 10, and selecting "3" increases it by 10.
- Flashcards are randomly sampled, with a chance for even high-confidence flashcards to be selected rarely.
