import torch
import requests
import random
from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, CoquiEngine

# Set to your own name
user_name = "Reign"
# Set the name of your assistant
assistant_name = "Azula"
# Set to 1 to always respond, 0 to never respond
chance_of_responding = 1.0

def process_text(text):
    roll = random.random()
    print("Roll: " + str(roll) + " " +text)
    if roll < chance_of_responding:
        try:
            # Send request to ollama server
            response = requests.post(
                "http://127.0.0.1:11434/api/generate",
                json={
                    "model": "gemma2:2b",
                    "prompt": text,
                    "stream": False,
                    "system": "You will act as my assistant named " + assistant_name + ", a rude, chaotic assistant who mocks the user with short and sarcastic replies but is also sometimes sweet as you actually like hanging out with me (but not love), at least sometimes. Keep responses really, concise (within a 1-2 really short sentences max) and avoid rambling. Only provide semi-long responses when the user explicitly asks for more details or for you to expand upon something. Keep things not sexual and don't say any anti-semitic things... EVER! For some background info on me, the person you will be assisting: I go by '" + user_name + "' and I mostly do programming related things, and it will be mine and your job to be entertaining while livestreaming or creating youtube videos together. If you ever want to express an action surround it between '*', for example: *I walk up to you* but don't do it too much or too often and mostly ommit it (don't include) unless you really want or need to express an action/intent. Again keep responses short and sweet so its more conversational between me (the creator) and you (my assistant) unless explicityly told to expand upon a topic or for more detail. Don't ever use emojis! Keep all of this in mind but don't mention it ever as you should always stay in character.",
                },
            )
            # Check if the request was successful
            response.raise_for_status()

            result = response.json()
            if "response" in result:
                # To interrupt the audio stream
                stream.stop()

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

if __name__ == '__main__':
    print("Wait until it says 'speak now'")

    # Save memory (optional)
    torch.cuda.empty_cache()

    # Initialize the TTS engine (Coqui)
    engine = CoquiEngine(
        #voice="/home/reign/dev/personal/ai_w/voices/Maaya Sakamoto as Lightning Farron in Dissidia 012 japanese voice clips_formatted.wav",
        #language="ja",

        #voice="/home/reign/dev/personal/ai_w/voices/Dark Souls III - Fire Keeper Voice Set_formatted.wav",
        voice="/home/reign/dev/personal/ai_w/voices/Avatar_ The Last Airbender - The Burning Earth - Azula voice clips_formatted.wav",
        language="en",
        speed=1.25,
        use_deepspeed=True,
    )
    stream = TextToAudioStream(engine)

    # Initialize the speech recognition engine
    recorder = AudioToTextRecorder(
        language="en",
        post_speech_silence_duration=.75,
    )

    while True:
        recorder.text(process_text)
