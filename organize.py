import os
import shutil

def organize_audio_files(folder_path):
    less_than_1s_dir = os.path.join(folder_path, "less_than_1s")
    less_than_3s_dir = os.path.join(folder_path, "less_than_3s")
    other_files_dir = os.path.join(folder_path, "other_files")
    specific_files_dir = os.path.join(folder_path, "specific_files")

    # Create directories if they don't exist
    for directory in [less_than_1s_dir, less_than_3s_dir, other_files_dir, specific_files_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".wav") or filename.endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            if filename.endswith("s.wav") or filename.endswith("s.mp3") or filename.endswith("se.wav") or filename.endswith("se.mp3"):
                shutil.move(file_path, specific_files_dir)
            else:
                duration = get_audio_duration(file_path)
                if duration < 1:
                    shutil.move(file_path, less_than_1s_dir)
                elif duration < 3:
                    shutil.move(file_path, less_than_3s_dir)
                else:
                    shutil.move(file_path, other_files_dir)

def get_audio_duration(file_path):
    # Function to get the duration of audio file (you need to implement this)
    # You can use libraries like librosa, pydub, audioread, etc. to get audio duration
    # Here's a sample implementation using pydub:
    from pydub import AudioSegment
    audio = AudioSegment.from_file(file_path)
    return len(audio) / 1000  # Duration in seconds

# Example usage
folder_path = "audio"
organize_audio_files(folder_path)
