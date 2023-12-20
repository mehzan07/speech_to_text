import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\GoogleServiceAccount\\natural-osprey-408612-73337e3649b4.json"


from google.cloud import speech

# Create a SpeechClient object
client = speech.SpeechClient()

# Specify the audio file to transcribe
audio_file = "C:\\Utvecklingprogram\\OpenAI\\speech_to_text\\audio_files\\synthesis.wav"
sample_rate = 24000  # Replace this with the actual sample rate of your audio file




# Load the audio file
with open(audio_file, "rb") as audio_file:
    audio_data = audio_file.read()

# Configure the speech recognition
audio = speech.RecognitionAudio(content=audio_data)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=sample_rate,
    language_code="en-US",
)

# Perform the speech recognition
response = client.recognize(config=config, audio=audio)

# Print the recognized text
for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
