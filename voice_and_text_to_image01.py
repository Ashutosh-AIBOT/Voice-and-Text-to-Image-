import streamlit as st
import requests
import sounddevice as sd
import wavio
import openai
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "HERE YOUR API KEY"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to record audio
def record_audio(filename, duration, fs):
    st.info("Recording audio...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    wavio.write(filename, recording, fs, sampwidth=2)
    st.success(f"Audio recorded and saved as {filename}")

# Function to generate an image from text
def generate_image_from_text(text):
    with st.spinner("Generating image..."):
        response = openai.Image.create(
            prompt=text,
            n=1,
            size="1024x1024"
        )
    image_url = response['data'][0]['url']
    image_response = requests.get(image_url)

    # Save and display the image
    image_path = "generated_image.jpg"
    with open(image_path, "wb") as f:
        f.write(image_response.content)
    st.success("Image generated successfully!")
    st.image(image_path, caption="Generated Image")

# Streamlit interface
st.title("Voice and Text to Image Generator")
st.write("Use your voice or enter text to generate an image based on the input using AI.")

# Radio buttons to select input method
input_method = st.radio("Select input method:", ("Voice", "Text"))

if input_method == "Voice":
    if st.button("Click here to speak"):
        audio_filename = "input.wav"
        duration = 5  # Duration of the recording in seconds
        fs = 44100  # Sample rate
        record_audio(audio_filename, duration, fs)  # User input recorded and stored

        # Converting to text using OpenAI's Whisper model
        with st.spinner("Transcribing audio..."):
            audio_file = open(audio_filename, "rb")
            transcript = openai.Audio.transcribe(
                model="whisper-1", 
                file=audio_file
            )
        a = transcript['text']
        st.write("Transcribed Text:", a)

        # Generate image from transcribed text
        generate_image_from_text(a)

elif input_method == "Text":
    user_input = st.text_area("Enter your text here:")
    if st.button("Generate Image"):
        generate_image_from_text(user_input)

st.write("Powered by OpenAI")




