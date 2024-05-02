import os
import subprocess

def find_audio_files(directory):
    audio_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mp3', '.wav', '.ogg', '.flac')):
                audio_files.append(os.path.join(root, file))
    return audio_files

def combine_audio_files(audio_files, output_file):
    with open('input.txt', 'w') as f:
        for file in audio_files:
            f.write("file '%s'\n" % file)
    subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'input.txt', '-c', 'copy', output_file])
    os.remove('input.txt')

def compress_audio(input_file, output_file, target_size_mb):
    subprocess.run(['ffmpeg', '-i', input_file, '-b:a', '128k', '-fs', str(target_size_mb) + 'M', output_file])

def main(directory, output_file, target_size_mb):
    audio_files = find_audio_files(directory)
    if not audio_files:
        print("No audio files found.")
        return
    combine_audio_files(audio_files, output_file)
    compress_audio(output_file, 'compressed_' + output_file, target_size_mb)

if __name__ == "__main__":
    directory = input("Enter the directory containing audio files: ")
    output_file = input("Enter the name of the output file (with extension): ")
    target_size_mb = 50
    main(directory, output_file, target_size_mb)
