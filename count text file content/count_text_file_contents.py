def count_text_file_contents(input_file_path, output_file_path):
    try:
        # Initialize counters
        line_count = 0
        word_count = 0
        char_count = 0

        # Opening the input file for reading
        with open(input_file_path, 'r', encoding='utf-8') as inpu_file:
            # Read each line in the file
            for line in inpu_file:
                # Update line count
                line_count += 1
                
                # Update word count
                words = line.split()
                word_count += len(words)
                
                # Update character count
                char_count += len(line)
        
        # Prepare the results to be written to the output file
        results = (
            f"Number of lines: {line_count}\n"
            f"Number of words: {word_count}\n"
            f"Number of characters: {char_count}\n"
        )

        # Open the output file for writing the result
        with open(output_file_path, 'w', encoding='utf-8') as outpu_file:
            outpu_file.write(results)
        
        print(f"Results written to output.txt")

    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
    

#Giving input File
input_file = 'count text file content/input.txt'  
output_file = 'count text file content/output.txt'
#Calling the function with input and output file paths
#function Calling
count_text_file_contents(input_file, output_file)
