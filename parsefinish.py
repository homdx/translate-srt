import os
import sys

def merge_srt_and_translation(srt_file, txt_file, output_file):
    # Open the srt and txt files
    with open(srt_file, 'r') as srt, open(txt_file, 'r') as txt:
        srt_lines = srt.readlines()
        txt_lines = txt.readlines()

    # Initialize variables
    srt_index = 0
    txt_index = 0
    output_lines = []

    # Iterate over each line in the srt file
    while srt_index < len(srt_lines) and txt_index < len(txt_lines):
        srt_line = srt_lines[srt_index].strip()
        txt_line = txt_lines[txt_index].strip()

        # If the srt line is a number and matches the txt line, add it to output_lines
        if srt_line.isdigit() and srt_line == txt_line:
            output_lines.append(srt_lines[srt_index])  # Add the number
            output_lines.append(srt_lines[srt_index + 1])  # Add the timestamp

            # Add the original text
            srt_index += 2
            while srt_index < len(srt_lines) and not (srt_lines[srt_index].strip().isdigit() or srt_lines[srt_index].strip() == ''):
                output_lines.append(srt_lines[srt_index])
                srt_index += 1

            # Add the translated text
            txt_index += 1
            while txt_index < len(txt_lines) and not txt_lines[txt_index].strip().isdigit():
                output_lines.append(txt_lines[txt_index])
                txt_index += 1

            output_lines.append('\n')  # Add an empty line
        else:
            # If the numbers don't match, move to the next subtitle in the srt file
            srt_index += 1

    # Write the output lines to the output file
    with open(output_file, 'w') as out:
        out.writelines(output_lines)

def create_translated_srt(srt_file, txt_file, output_file):
    # Open the srt and txt files
    with open(srt_file, 'r') as srt, open(txt_file, 'r') as txt:
        srt_lines = srt.readlines()
        txt_lines = txt.readlines()

    # Initialize variables
    srt_index = 0
    txt_index = 0
    output_lines = []

    # Iterate over each line in the srt file
    while srt_index < len(srt_lines) and txt_index < len(txt_lines):
        srt_line = srt_lines[srt_index].strip()
        txt_line = txt_lines[txt_index].strip()

        # If the srt line is a number and matches the txt line, add it to output_lines
        if srt_line.isdigit() and srt_line == txt_line:
            output_lines.append(srt_lines[srt_index])  # Add the number
            output_lines.append(srt_lines[srt_index + 1])  # Add the timestamp

            # Add the translated text
            txt_index += 1
            while txt_index < len(txt_lines) and not txt_lines[txt_index].strip().isdigit():
                output_lines.append(txt_lines[txt_index])
                txt_index += 1

            output_lines.append('\n')  # Add an empty line

            # Move to the next subtitle in the srt file
            srt_index += 4
        else:
            # If the numbers don't match, move to the next subtitle in the srt file
            srt_index += 1

    # Write the output lines to the output file
    with open(output_file, 'w') as out:
        out.writelines(output_lines)

# Get the source srt filename from the command line
srt_file = sys.argv[1]

# Get the base name of the srt file without the extension
base_name = os.path.splitext(srt_file)[0]

# Call the functions to create the output and translated srt files
merge_srt_and_translation(srt_file, 'translate1.txt', base_name + '-both.srt')
create_translated_srt(srt_file, 'translate1.txt', base_name + '-rus.srt')
