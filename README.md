# AI_W

## Idea

I want an AI co-streaming partner (similar to vedals's neuro-sama) that can
take in my voice as input and output either a text or audio speech response. I
want it to also possibly take intermitted screenshots of my screen and take
them as input to the AI. The AI must be able to stay in character and be
generally entertaining.

## Tech-Stack

(Server)

- [ollama](https://github.com/ollama/ollama)
  - Potential models:
    - jean-luc/tiger-gemma-9b-v3:q3_K_M (uncensored, decently fast, and decent quality)
    - AnInterestingSurname/gemmasutra-mini-2b-v1:q5_k_m (uncensored, really
      fast, and really good at roleplaying out of the box)
    - 0ssamaak0/xtuner-llava:llama3-8b-v1.1-int4 (multi-modal, uncensored, decently fast)
    - 0ssamaak0/xtuner-llava:phi3-mini-int4 (multi-modal, uncensored, really fast)

(Python)

- [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) for Speech-To-Text
  - With CUDA support
- [RealtimeTTS](https://github.com/KoljaB/RealtimeTTS) for Text-To-Speech
  - With CUDA support
- [mss](https://github.com/BoboTiG/python-mss) for capturing screenshots

- [deepspeed]

<!--TODO: Find Text-To-Speech library-->
<!--A tip I learned from a video is to pass the past few sentences of the back
and forth conversation back to the LLM when prompting it as it helps it to
remember the context.-->

## Installation

- install ollama

- must create a virtual environment with python 3.11

```bash
mkdir ai_w
cd ai_w
python3.11 -m venv venv
source venv/bin/activate
```

- continue installing RealtimeSTT

## TODO

- Implent a good abstraction from making restful API calls to local ollama
