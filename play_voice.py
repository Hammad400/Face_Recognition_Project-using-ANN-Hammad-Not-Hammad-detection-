from playsound import playsound
playsound('output.mp3')
# from pydub import AudioSegment
# from pydub.playback import play

# # Load the MP3 file
# audio = AudioSegment.from_mp3("D:/Data Science projects/ML Projects/Sports celeberty detection/output.mp3")

# # Play the audio
# play(audio)
import subprocess

# Specify the MP3 file you want to play
mp3_file = "urdu_output1.mp3"

# Use the "start" command to open the default audio player
subprocess.Popen(["start", "cmd", "/c", mp3_file], shell=True)
