from google.cloud import texttospeech
client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text="""
    Welcome to your new Python course. Today we will be learning the
    basics of how to get started with Python.
    We will learn how to install python, build a vee e en vee, and then run a 
    simple Python program.
    Finally, we will install Pycharm so you can develop programs.

    """)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", 
    name="en-US-Neural2-I"
)


audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')