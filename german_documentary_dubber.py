import os
import yt_dlp
import whisper
import asyncio
import edge_tts
from deep_translator import GoogleTranslator
import subprocess

# YouTube URL already added
VIDEO_URL = "https://youtu.be/Iw_cfbtNt-Y?si=bfJaVcnHJ0lMT4Jl"

# FFmpeg path
FFMPEG_PATH = r"C:\Cffmpeg\ffmpeg-8.1.2-essentials_build\bin\ffmpeg.exe"

# Downloads folder
DOWNLOADS_FOLDER = r"C:\Users\choud\Downloads"

# Download YouTube video
def download_video():
    print("Downloading video...")

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(DOWNLOADS_FOLDER, 'original_video.%(ext)s'),
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(VIDEO_URL, download=True)
        ext = info.get('ext', 'mp4')

    return os.path.join(DOWNLOADS_FOLDER, f"original_video.{ext}")

# Transcribe video
def transcribe_video(video_file):
    print("Transcribing video...")

    os.environ["PATH"] += os.pathsep + os.path.dirname(FFMPEG_PATH)

    # Faster model for 30-min video
    model = whisper.load_model("tiny")
    result = model.transcribe(video_file)

    print("Transcription completed!")
    return result["text"]

# Translate large text in chunks
def translate_text(text):
    print("Translating to English...")

    translator = GoogleTranslator(source='auto', target='en')
    translated_parts = []

    chunk_size = 4500
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        translated_chunk = translator.translate(chunk)
        translated_parts.append(translated_chunk)

    print("Translation completed!")
    return " ".join(translated_parts)

# Generate English speech
async def text_to_speech(text):
    print("Generating English speech...")

    audio_path = os.path.join(DOWNLOADS_FOLDER, "english_audio.mp3")

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AriaNeural"
    )

    await communicate.save(audio_path)

    print("English speech generated!")
    return audio_path

# Merge audio and video
def merge_audio_video(video_file, audio_file):
    print("Merging audio with video...")

    output_file = os.path.join(DOWNLOADS_FOLDER, "dubbed_video.mp4")

    command = [
        FFMPEG_PATH,
        "-y",
        "-i", video_file,
        "-i", audio_file,
        "-c:v", "copy",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",
        output_file
    ]

    subprocess.run(command, check=True)

    print(f"Dubbed video saved as: {output_file}")

# Main program
async def main():
    print("=== Automated Video Dubbing System ===")

    try:
        video_file = download_video()
        text = transcribe_video(video_file)
        translated_text = translate_text(text)
        audio_file = await text_to_speech(translated_text)
        merge_audio_video(video_file, audio_file)

        print("\nAssignment completed successfully!")
        print("Final file is in Downloads folder: dubbed_video.mp4")

    except Exception as e:
        print(f"Error: {e}")

# Run program
if __name__ == "__main__":
    asyncio.run(main())