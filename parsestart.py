import os

def parse_srt(srt_file):
    # Open the srt file
    with open(srt_file, 'r') as f:
        lines = f.readlines()

    # Initialize variables
    file_count = 1
    output_file = open(f'translate{file_count}.txt', 'w')
    text_lines = []
    write_text = False

    # Iterate over each line in the srt file
    for line in lines:
        stripped_line = line.strip()
        
        # If the line is a number, add it to text_lines and set write_text to True
        if stripped_line.isdigit():
            text_lines.append(line)
            write_text = True
        # If the line contains '-->', set write_text to False
        elif '-->' in stripped_line:
            write_text = True  # Change this line
        # If write_text is True and the line is not empty, add it to text_lines
        elif write_text and stripped_line != '':
            text_lines.append(line)
            text_lines.append('\n')  # Add an empty line after each line of text

        # Calculate the size of the text lines
        text_size = sum(len(text) for text in text_lines)

        # If the size of the text lines is greater than or equal to 3KB, write the lines to the current file, close it, and open a new one
        if text_size >= 4096:
            output_file.writelines(text_lines)
            output_file.close()
            text_lines = []
            file_count += 1
            output_file = open(f'translate{file_count}.txt', 'w')


    # Write any remaining text lines to the last output file
    if text_lines:
        output_file.writelines(text_lines)

    # Close the last output file
    output_file.close()

# Call the function to parse the srt file
parse_srt('source.srt')

# Print a success message
print("The srt file was successfully parsed and the text was written to the output files.")
