import os
import subprocess

def combine_audio_files(input_dir, output_file, target_size_mb=100, verbose=True):
    # Check if the output file already exists, if so, delete it
    if os.path.exists(output_file):
        os.remove(output_file)

    # Create a list of audio files to combine
    audio_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(('.mp3', '.wav'))]

    # Create a temporary text file with the list of audio files
    with open('file_list.txt', 'w') as file_list:
        for file_path in audio_files:
            file_list.write(f"file '{file_path}'\n")

    # Calculate the required bitrate to achieve the target file size (in kilobits)
    total_duration_sec = sum([subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 
                                                       'format=duration', '-of', 
                                                       'default=noprint_wrappers=1:nokey=1', file]).decode('utf-8') 
                              for file in audio_files])
    total_duration_sec = float(total_duration_sec)
    target_bitrate_kbps = (target_size_mb * 8 * 1024) / total_duration_sec

    # Combine audio files using ffmpeg
    subprocess.call(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'file_list.txt', 
                     '-c:a', 'libmp3lame', '-b:a', f'{target_bitrate_kbps}k', output_file])

    if verbose:
        print("Audio files combined and compressed successfully!")

# Example usage:
input_directory = "DART"
output_file = "all.mp3"
combine_audio_files(input_directory, output_file)
