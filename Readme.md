Workflow:

Users can type a text description or record their voice.
Recorded audio is captured using SoundDevice and saved as a WAV file.
Whisper transcribes the audio to text.
The transcribed or typed text is sent to DALL-E via the Requests library.
DALL-E generates an image based on the text description.

The generated image is displayed on the Streamlit web interface.
