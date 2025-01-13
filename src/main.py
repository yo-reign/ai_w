from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, CoquiEngine
from settings import Config, ModelType
import torch
import random
import regular_model
import multimodal_model

config = Config(ModelType.MULTIMODAL, "Reign", "Azula", 1.0)

def process_text(text: str):
    roll = random.random()
    print("Roll: " + str(roll) + " " +text)
    if roll < config.chance_of_responding:
        if config.model_type == ModelType.REGULAR:
            generated_text = regular_model.regular_model_request(text, config)
        elif config.model_type == ModelType.MULTIMODAL:
            generated_text = multimodal_model.multimodal_model_request(text, config)
        else:
            print("Error: Invalid model type.")
            return

        if generated_text != "":
            print(generated_text)
            # To interrupt the audio stream
            stream.stop()


            # Play the generated text
            stream.feed(generated_text)
            stream.play_async()
        else:
            print("Error: No generated text found.")

if __name__ == '__main__':
    # Save memory (optional)
    torch.cuda.empty_cache()

    print("Wait until it says 'speak now'")

    # Initialize the TTS engine (Coqui)
    engine = CoquiEngine(
        #voice="/home/reign/dev/personal/ai_w/voices/Maaya Sakamoto as Lightning Farron in Dissidia 012 japanese voice clips_formatted.wav",
        #language="ja",
        voice="/home/reign/dev/personal/ai_w/voices/Dark Souls III - Fire Keeper Voice Set_formatted.wav",
        #voice="/home/reign/dev/personal/ai_w/voices/Avatar_ The Last Airbender - The Burning Earth - Azula voice clips_formatted.wav",

        device="cpu", # Set to "cuda" to use CUDA (cost more cuda memory)
        language="en",
        speed=1.25,
        use_deepspeed=True,
    )
    stream = TextToAudioStream(engine)

    # Initialize the speech recognition engine
    recorder = AudioToTextRecorder(
        device="cpu", # Set to "cuda" to use CUDA (cost more cuda memory)
        language="en",
        post_speech_silence_duration=.75,
    )

    while True:
        recorder.text(process_text)
