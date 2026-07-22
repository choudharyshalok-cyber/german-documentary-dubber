# German Documentary Dubber

An automated video dubbing system built with Python.

This project takes a YouTube video URL as input and:

- Downloads the video.
- Extracts and transcribes the speech using OpenAI Whisper.
- Translates the transcription into English.
- Generates natural English speech using Edge-TTS.
- Replaces the original audio with the English dubbed audio using FFmpeg.
- Saves the final dubbed video.

## Features

- YouTube video downloading
- Speech-to-text transcription
- English translation
- Natural sounding English voice generation
- Audio and video merging
- Command line execution

## Technologies Used

- Python 3.x
- yt-dlp
- OpenAI Whisper
- Edge-TTS
- FFmpeg
- MoviePy

## Installation

Clone the repository:

```bash
git clone https://github.com/choudharyshalok-cyber/german-documentary-dubber.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install FFmpeg and add it to your system PATH.

## Run

```bash
python german_documentary_dubber.py
```

Enter the YouTube URL when prompted.

## Project Workflow

1. Download video.
2. Extract audio.
3. Transcribe speech.
4. Translate into English.
5. Generate English voice.
6. Merge dubbed audio with video.
7. Save the final output video.

## Output

The final dubbed English video is saved as:

```
DW_Documentary_English_Dubbed.mp4
```

## Author

Shlok Choudhary
