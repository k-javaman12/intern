# # whisper japanese.mp3 --language Korean --task transcribe
#
# import whisper
# from whisper.utils import get_writer
# import os
#
#
# def transcribe_mp3_files(directory):
#     model = whisper.load_model("base")
#
#     # List all files in the given directory
#     files = os.listdir(directory)
#
#     # Filter only .mp3 files
#     mp3_files = [f for f in files if f.endswith('.mp3')]
#
#     for mp3_file in mp3_files:
#         vtt_writer = get_writer("vtt", output_directory)
#         vtt_writer(result, audio)
#
#         # Construct the full path to the mp3 file
#         mp3_file_path = os.path.join(directory, mp3_file)
#
#         # Construct the command
#         cmd = f'whisper "{mp3_file_path}" --model small --task transcribe --language Korean'
#
#         # Execute the command
#         os.system(cmd)
#
#
# # Call the method
# directory = "C:/intern/pythonProjects/pythonProject/python_assignment/videos/audios"
# output_directory = "C:/intern/pythonProjects/pythonProject/python_assignment/videos/texts"
# transcribe_mp3_files(directory)

import whisper
from whisper.utils import get_writer

model = whisper.load_model("base")
audio = "1sample.mp3"
result = model.transcribe(audio)
output_directory = "C:\intern\pythonProjects\pythonProject\python_assignment\videos\texts"

# Save as an SRT file
srt_writer = get_writer("srt", output_directory)
srt_writer(result, audio)


# Save as a VTT file
vtt_writer = get_writer("vtt", output_directory)
vtt_writer(result, audio)
