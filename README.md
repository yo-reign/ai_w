# AI_W

## Idea

## Tech-Stack

(Python)

- [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) for Speech-To-Text
  - With GPU support (CUDA)

(Zig)

- [ollama-zig](https://github.com/tr1ckydev/ollama-zig) for IO to local LLM

<!--TODO: Find Text-To-Speech library-->
<!--A tip I learned from a video is to pass the past few sentences of the back
and forth conversation back to the LLM when prompting it as it helps it to
remember the context.-->

## Installation

must create a virtual environment with python 3.11

```bash
mkdir ai_w
cd ai_w
python3.11 -m venv venv
source venv/bin/activate
```

continue installing RealtimeSTT
