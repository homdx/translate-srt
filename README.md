# SRT File Parser and Translation Merger

This Python application consists of two main components: `parsestart.py` and `parsefinish.py`. The former is used to parse SRT (SubRip Text) files, commonly used for adding subtitles to videos, while the latter merges the parsed SRT files with translated text files.

## SRT File Parser: parsestart.py

The `parsestart.py` application reads the SRT file, extracts the subtitle text, and writes the text to multiple output files.

### How it Works

The application works by reading an SRT file line by line. It identifies lines that contain subtitle text based on the SRT file format. Specifically, it looks for lines that are numbers (which indicate the start of a new subtitle) and lines that contain '-->' (which indicate the time range for the subtitle). The text following these lines is the actual subtitle text.

The application writes the subtitle text to an output file. When the size of the output file reaches 3KB, the application closes the current file and opens a new one. This process continues until all the subtitle text from the SRT file has been written to the output files.

### Usage

To use the application, simply call the `parsestart.py` function with the path to the SRT file as the argument:

```python
parsestart.py path_to_your_srt_file.srt
```

## SRT and Translation Merger: parsefinish.py

The `parsefinish.py` application is designed to merge the parsed SRT files with translated text files. It can create bilingual subtitles or replace original subtitles with translated ones.

### Features

- Merges SRT files with translated text files.
- Creates two types of output files:
  - One with both the original and translated text.
  - One with only the translated text.
- The output filenames are based on the original SRT filename.

### Usage

The application takes the source SRT filename from the command line. The output filenames are based on this filename.

```bash
python parsefinish.py path_to_your_srt_file.srt
```
