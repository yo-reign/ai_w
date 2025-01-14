from settings import Config
import requests
import subprocess
import base64
import platform
import json

def capture_and_encode_screenshot() -> str:
    # Get the current platform
    system = platform.system()

    # Handle Linux (Wayland)
    if system == "Linux":
        # Use grim for Wayland
        screenshot_path = "/tmp/screenshot.png"
        subprocess.run(["grim", "-c", "-g", "0,0 1920x1080", screenshot_path], check=True)

        # Read the screenshot and encode it to Base64
        with open(screenshot_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_image

    return ""

def multimodal_model_request(text: str, config: Config):
    screenshot_base64 = capture_and_encode_screenshot()
    print(screenshot_base64)

    try:
        # Send request to ollama server
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "0ssamaak0/xtuner-llava:phi3-mini-int4",
                "prompt": text,
                "stream": True,
                "system": "You will act as my assistant named " + config.assistant_name + ", a rude, chaotic assistant who mocks the user with short and sarcastic replies but is also sometimes sweet as you actually like hanging out with me (but not love), at least sometimes. Keep responses really, concise (within a 1-2 really short sentences max) and avoid rambling. Only provide semi-long responses when the user explicitly asks for more details or for you to expand upon something. Keep things not sexual and don't say any anti-semitic things... EVER! For some background info on me, the person you will be assisting: I go by '" + config.user_name + "' and I mostly do programming related things, and it will be mine and your job to be entertaining while livestreaming or creating youtube videos together. If you ever want to express an action surround it between '*', for example: *I walk up to you* but don't do it too much or too often and mostly ommit it (don't include) unless you really want or need to express an action/intent. Again keep responses short and sweet so its more conversational between me (the creator) and you (my assistant) unless explicityly told to expand upon a topic or for more detail. Don't ever use emojis! Keep all of this in mind but don't mention it ever as you should always stay in character. You will also always recieve a screenshot of my current desktop environment, but you don't always have to explain what is going on unless specifically asked, in fact mostly ignore it unless something really interesting is going on (or asked to analyze it).",
                "images": [screenshot_base64],
            },
            stream=True,
        )
        # Check if the request was successful
        response.raise_for_status()

        # Process the streamed response
        result_text = ""
        print("Streaming response...")
        for chunk in response.iter_lines(decode_unicode=True):
            if chunk:  # Skip empty lines
                try:
                    # Attempt to parse the JSON chunk
                    chunk_data = json.loads(chunk)
                    print(f"Chunk received: {chunk_data}")  # Debugging output

                    # Check for the "response" key
                    if "response" in chunk_data:
                        result_text += chunk_data["response"]
                        print(f"Partial response text: {chunk_data['response']}")  # Debugging output
                except json.JSONDecodeError:
                    print(f"Failed to parse chunk: {chunk}")  # Log unparsed chunk

        return result_text

    except requests.exceptions.RequestException as e:
        print(f"Error with the request: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""
