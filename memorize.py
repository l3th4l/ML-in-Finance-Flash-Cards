import os
import re
import json

def extract_questions_and_answers(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()

    # Use regular expressions to find questions and answers
    questions_answers = re.findall(r'Question (\d+): "(.*?)"\s+Answer:\s+(.*?)(?=\nQuestion|$)', text, re.DOTALL)

    extracted_data = []
    for idx, (question_number, question, answer) in enumerate(questions_answers, start=1):
        extracted_data.append({
            "question_number": int(question_number),
            "question": question.strip(),
            "answer": answer.strip()
        })

    return extracted_data



def process_files_in_directory(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            data.extend(extract_questions_and_answers(file_path))
    return data

def save_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=2)

def main(input_directory, output_file):
    extracted_data = process_files_in_directory(input_directory)
    save_to_json(extracted_data, output_file)

if __name__ == "__main__":
    input_directory = "./text_files"
    output_file = "output.json"
    main(input_directory, output_file)
