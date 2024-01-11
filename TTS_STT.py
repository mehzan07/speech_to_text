import os
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import texttospeech

# Set up Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\GoogleServiceAccount\\natural-osprey-408612-73337e3649b4.json"

# Function for Speech-to-Text (STT)
def speech_to_text(audio_file, sample_rate):
    # Create a SpeechClient object
    client = speech.SpeechClient()

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

# Function for Text-to-Speech (TTS)
def text_to_speech(text):
    # Initialize a Text-to-Speech client
    tts_client = texttospeech.TextToSpeechClient()

    # Set text input
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Select voice parameters and audio format
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # Choose language code
        name="en-US-Wavenet-D",  # Choose voice name
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL  # Choose gender
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16  # Choose audio format
    )

    # Generate the speech
    response = tts_client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Save the audio response to a file
    with open("output_audio.wav", "wb") as out:
        out.write(response.audio_content)

    print("Text-to-Speech conversion completed. Output saved as output_audio.wav")

# Ask the user for their choice
print("Choose an option:")
print("1. Speech to Text")
print("2. Text to Speech")
option = input("Enter your choice (1 or 2): ")

# Perform the selected action based on user input
if option == "1":
    # Assuming the audio file and sample rate are already defined
    audio_file = "C:\\Utvecklingprogram\\OpenAI\\speech_to_text\\audio_files\\synthesis.wav"
    sample_rate = 24000  # Replace this with the actual sample rate of your audio file
    speech_to_text(audio_file, sample_rate)
elif option == "2":
    text_to_convert = input("Enter the text you want to convert to speech: ")
    text_to_speech(text_to_convert)
else:
    print("Invalid choice. Please enter either 1 or 2.")
