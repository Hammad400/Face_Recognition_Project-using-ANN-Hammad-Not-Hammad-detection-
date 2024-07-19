from gtts import gTTS

# # Define the text you want to convert to speech
# text = "Hello, This is Hammaad"

# # Create a gTTS object
# tts = gTTS(text)

# # Save the speech as an MP3 file
# tts.save("output.mp3")

# text = "Hello, This is not Hammaad"

# # Create a gTTS object
# tts = gTTS(text)

# # Save the speech as an MP3 file
# tts.save("output1.mp3")
from gtts import gTTS

# Define the Urdu text you want to convert to speech
urdu_text = "یہ حماد ہے"

# Create a gTTS object with the language set to 'ur' for Urdu
tts = gTTS(text=urdu_text, lang='ur')

# Save the speech as an MP3 file
tts.save("urdu_output.mp3")

urdu_text = "یہ حماد نہیں ہے۔"

# Create a gTTS object with the language set to 'ur' for Urdu
tts = gTTS(text=urdu_text, lang='ur')

# Save the speech as an MP3 file
tts.save("urdu_output1.mp3")
