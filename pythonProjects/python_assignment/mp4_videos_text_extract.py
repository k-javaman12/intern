# Importing the subprocess module, which is used to spawn and manage separate processes and their interactions.
import subprocess

# Importing the Path class from the pathlib module. Pathlib provides a way to handle filesystem paths in an object-oriented manner.
from pathlib import Path


def extract_audio_from_video(video_path, output_path):
    """
    This function extracts the audio from a given video and saves it to a specified output path.
    """

    # Defining the command to extract audio from video using 'ffmpeg'
    command = [
        'ffmpeg',  # The name of the tool to use
        '-i', str(video_path),  # '-i' specifies the input file. We ensure the path is a string.
        '-q:a', '0',  # Setting audio quality. '0' indicates the highest quality.
        '-map', 'a',  # Extract only audio
        str(output_path)  # Specify the output path for the extracted audio. Ensure it's a string.
    ]

    # Executing the command
    subprocess.run(command)


def transcribe_audio_file(audio_path, output_directory):
    """
    This function transcribes an audio file and saves the transcription to a specified directory.
    """

    # Getting the name of the audio file without its extension using the stem property of Path objects
    # E.g., for "sample.mp3", stem would be "sample"
    folder_path = output_directory / audio_path.stem  # Constructing the path to the folder where results will be saved

    # Create the directory if it doesn't exist
    folder_path.mkdir(exist_ok=True)

    # Construct the command to transcribe the audio using 'whisper'
    cmd = f'cd "{folder_path}" && whisper "{audio_path}" --model small --task transcribe --language Korean'

    # Execute the command
    subprocess.run(cmd, shell=True)


def main():
    # Using the Path class to represent directory paths
    video_directory = Path("C:/intern/pythonProjects/pythonProject/python_assignment/videos")
    audio_directory = video_directory / "audios"  # Construct the path for audios
    text_directory = video_directory / "texts"  # Construct the path for texts

    # Loop through all .mp4 files in the video directory and extract audio from them
    for video_path in video_directory.glob("*.mp4"):
        audio_path = audio_directory / (video_path.stem + ".mp3")  # Create the path for the output audio file
        extract_audio_from_video(video_path, audio_path)  # Extract audio

    # Loop through all .mp3 files in the audio directory and transcribe them
    for audio_path in audio_directory.glob("*.mp3"):
        transcribe_audio_file(audio_path, text_directory)  # Transcribe audio


# The following code ensures the main() function is called only when this script is executed directly, and not when it's imported.
if __name__ == "__main__":
    main()
