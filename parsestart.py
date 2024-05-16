import os
import argparse

def parse_srt(srt_file):
    # Open the srt file
    with open(srt_file, 'r') as f:
        lines = f.readlines()

    # Initialize variables
    file_count = 0
    output_file = open(f'translate{file_count}.txt', 'w')
    text_lines = []
    write_text = False

    # New variables for aggregation
    current_text = None
    current_start_time = None
    current_end_time = None

    # Iterate over each line in the srt file
    for line in lines:
        stripped_line = line.strip()

        # If the line is a number, add it to text_lines and set write_text to True
        if stripped_line.isdigit():
            # Calculate the size of the text lines
            text_size = sum(len(text) for text in text_lines)

            # If the size of the text lines is greater than or equal to 3KB, write the lines to the current file, close it, and open a new one
            if text_size >= 4096:
                output_file.writelines(text_lines)
                output_file.close()
                text_lines = []
                file_count += 1
                output_file = open(f'translate{file_count}.txt', 'w')

            write_text = True
        # If the line contains '-->', set write_text to False
        elif '-->' in stripped_line:
            times = stripped_line.split(' --> ')
            if current_text is not None:
                current_end_time = times[1]
            else:
                current_start_time = times[0]
                current_end_time = times[1]
            write_text = True
        # If write_text is True and the line is not empty, add it to text_lines
        elif write_text and stripped_line != '':
            if current_text is None:
                current_text = stripped_line
            elif current_text != stripped_line:
                # If the current text is different from the previous text, write the previous text and its time interval to the text_lines
                text_lines.append(f'{current_start_time} --> {current_end_time}\n')
                text_lines.append(f'{current_text}\n\n')
                current_text = stripped_line
                current_start_time = current_end_time
            else:
                # If the current text is the same as the previous text, do not append it to text_lines
                continue

    # Write any remaining text lines to the last output file
    if text_lines:
        output_file.writelines(text_lines)

    # Close the last output file
    output_file.close()

# Create the parser
parser = argparse.ArgumentParser(description="Parse an SRT file")

# Add the arguments
parser.add_argument('Path', metavar='path', type=str, help='the path to the srt file')

# Execute the parse_args() method
args = parser.parse_args()

# Call the function to parse the srt file
parse_srt(args.Path)
