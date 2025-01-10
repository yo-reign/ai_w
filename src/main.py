import requests
from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, PiperEngine, PiperVoice

def process_text(text):
    print(text)
    try:
        # Send request to ollama server
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "0ssamaak0/xtuner-llava:phi3-mini-int4",
                "prompt": text,
                "stream": False,
                # TODO: Add parameters for custom model behavior
            },
        )
        # Check if the request was successful
        response.raise_for_status()

        result = response.json()
        if "response" in result:
            # Extract the generated text from the response
            generated_text = result["response"]
            print(generated_text)

            # Play the generated text
            stream.feed(generated_text)
            stream.play_async()
        else:
            print("Key 'response' not found in response.")

    except requests.exceptions.RequestException as e:
        print(f"Error with the request: {e}")
    except ValueError:
        print("Error: Unable to parse response as JSON.")

def print_text(text):
    print(text)

if __name__ == '__main__':
    print("Wait until it says 'speak now'")

    # Initialize the TTS engine
    voice = PiperVoice(
        model_file="/home/reign/Documents/PiperVoices/kathleen-low/en_US-kathleen-low.onnx",
        config_file="/home/reign/Documents/PiperVoices/kathleen-low/en_en_US_kathleen_low_en_US-kathleen-low.onnx.json",
    )
    engine = PiperEngine(
        piper_path="/home/reign/dev/libs/piper/piper",
        voice=voice,
        #debug=True,
    )
    stream = TextToAudioStream(engine, frames_per_buffer=256)

    # Initialize the speech recognition engine
    recorder = AudioToTextRecorder(
        language="en",
        post_speech_silence_duration=.5,
    )

    while True:
        recorder.text(process_text)
