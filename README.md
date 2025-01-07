# AI_W

## Idea

## Tech-Stack

(Server)

- [ollama](https://github.com/ollama/ollama)
  <!--TODO: figure out best llm to use that is not too slow-->

(Python)

- [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) for Speech-To-Text
  - With GPU support (CUDA)

(Zig)

- [http.zig](https://github.com/karlseguin/http.zig) for RESTful API calls to ollama

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
