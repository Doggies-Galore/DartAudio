from pydub import AudioSegment
import os

def split_audio(file_path):
    # Load the audio file
    audio = AudioSegment.from_file(file_path)

    # Define the duration of each smaller audio file in milliseconds (5 minutes)
    segment_duration = 5 * 60 * 1000

    # Calculate the total number of smaller segments
    total_segments = len(audio) // segment_duration

    # Create a directory to store the smaller audio files
    output_dir = 'elevenlabs'
    os.makedirs(output_dir, exist_ok=True)

    # Split the audio file into smaller segments
    for i in range(total_segments):
        start_time = i * segment_duration
        end_time = (i + 1) * segment_duration
        segment = audio[start_time:end_time]

        # Export the segment as a smaller audio file
        segment.export(f"{output_dir}/segment_{i+1}.mp3", format="mp3")

    print("Audio file has been successfully split into smaller segments.")

if __name__ == "__main__":
    file_path = input("Enter the path of the audio file: ")
    split_audio(file_path)
