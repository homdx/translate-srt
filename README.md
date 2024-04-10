# SRT File Parser: parsestart.py

This Python application parses SRT (SubRip Text) files, which are commonly used for adding subtitles to videos. The application reads the SRT file, extracts the subtitle text, and writes the text to multiple output files.

## How it Works

The application works by reading an SRT file line by line. It identifies lines that contain subtitle text based on the SRT file format. Specifically, it looks for lines that are numbers (which indicate the start of a new subtitle) and lines that contain '-->' (which indicate the time range for the subtitle). The text following these lines is the actual subtitle text.

The application writes the subtitle text to an output file. When the size of the output file reaches 3KB, the application closes the current file and opens a new one. This process continues until all the subtitle text from the SRT file has been written to the output files.

After the text has been extracted to the .txt files, these files can be sent to a translation service for translation. The translated text can then be merged back into the original SRT file using another program `parsefinish.py`.

## Usage

To use the application, simply call the `parsestart.py` function with the path to the SRT file as the argument:

```python
parsestart.py('path_to_your_srt_file.srt')
```


# SRT and Translation Merger: parsefinish.py

This Python application is designed to merge SubRip (SRT) subtitle files with translated text files. It can create bilingual subtitles or replace original subtitles with translated ones.

## Features

- Merges SRT files with translated text files.
- Creates two types of output files:
  - One with both the original and translated text.
  - One with only the translated text.
- The output filenames are based on the original SRT filename.

## Usage

The appl# SRT File Parser

This Python application parses SRT (SubRip Text) files, which are commonly used for adding subtitles to videos. The application reads the SRT file, extracts the subtitle text, and writes the text to multiple output files.

## How it Works

The application works by reading an SRT file line by line. It identifies lines that contain subtitle text based on the SRT file format. Specifically, it looks for lines that are numbers (which indicate the start of a new subtitle) and lines that contain '-->' (which indicate the time range for the subtitle). The text following these lines is the actual subtitle text.

The application writes the subtitle text to an output file. When the size of the output file reaches 3KB, the application closes the current file and opens a new one. This process continues until all the subtitle text from the SRT file has been written to the output files.

After the text has been extracted to the .txt files, these files can be sent to a translation service for translation. The translated text can then be merged back into the original SRT file using another program.

## Usage

To use the application, simply call the `parsefinish.py` function with the path to the SRT file as the argument:

```python
parsefinish.py('path_to_your_srt_file.srt')
```
ication takes the source SRT filename from the command line. The output filenames are based on this filename.

```bash
python parsefinish.py path_to_your_srt_file.srt
```
