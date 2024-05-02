import speech_recognition as sr
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def transcribe_audio(audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    # Transcribe audio
    try:
        transcript = recognizer.recognize_google(audio_data)
        return transcript
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

def mark_timestamps(audio_file, text_file, interval=10):
    # Extract audio duration
    video = ffmpeg_extract_subclip(audio_file, 0, 1)
    duration = video.duration
    video.close()

    # Transcribe audio
    transcript = transcribe_audio(audio_file)

    # Write transcript with timestamps
    with open(text_file, 'w') as f:
        f.write("Transcript:\n\n")
        for i in range(0, int(duration), interval):
            f.write(f"{i}s: ")
            f.write(transcript)
            f.write("\n")

if __name__ == "__main__":
    audio_file = "all.mp3"  # Your audio file
    text_file = "transcript.txt"    # Output text file
    mark_timestamps(audio_file, text_file)
