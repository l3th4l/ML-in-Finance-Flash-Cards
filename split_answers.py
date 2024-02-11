def split_text_into_files(input_file_path, output_prefix):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    chunk_size = 3000
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    for i, chunk in enumerate(chunks):
        # Find the nearest space to avoid cutting words in half
        if len(chunk) == chunk_size:
            last_space_index = chunk.rfind(' ')
            if last_space_index != -1:
                chunk = chunk[:last_space_index]

        with open(f"{output_prefix}_{i+1}.txt", 'w', encoding='utf-8') as out_file:
            out_file.write(chunk)


# Example usage:
split_text_into_files("lecture_questions.txt", "output_chunk")
