from pydub import AudioSegment
import os

def combine_audio_files(input_dir, output_file, verbose=True):
    # Check if the output file already exists, if so, delete it
    if os.path.exists(output_file):
        os.remove(output_file)

    # Create an empty audio segment to store the combined audio
    combined_audio = AudioSegment.silent(duration=0)

    # Loop through all files in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.mp3') or file_name.endswith('.wav'):
            # Load the audio file
            audio = AudioSegment.from_file(os.path.join(input_dir, file_name))

            # Append the audio to the combined audio segment
            combined_audio += audio

            if verbose:
                print(f"Added '{file_name}' to the combined audio.")

    # Export the combined audio to the output file
    combined_audio.export(output_file, format="mp3")

    if verbose:
        print("Audio files combined successfully!")

# Example usage:
input_directory = "audio"
output_file = "all.mp3"
combine_audio_files(input_directory, output_file)
