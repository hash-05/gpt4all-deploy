# gpt4all-deploy
Deploying gpt4all on a local machine
<hr>

Steps:
1. Set up the environment.
2. Download the `gpt4all-lora-quantized.bin` file from [Direct Link:](https://the-eye.eu/public/AI/models/nomic-ai/gpt4all/gpt4all-lora-quantized.bin) or [Torrent Magnet](https://tinyurl.com/gpt4all-lora-quantized).
3. Convert it to the newer version using `tokenizer.model` using following command.
 ```shell
pyllamacpp-convert-gpt4all path/to/gpt4all_model.bin path/to/llama_tokenizer path/to/gpt4all-converted.bin
```
4.Run `main.py`

#### Official Repositories

[gpt4all](https://github.com/nomic-ai/gpt4all)

[pyllamaCPP](https://github.com/nomic-ai/pyllamacpp#pyllamacpp)

[Documentation for pyllamacpp](https://nomic-ai.github.io/pyllamacpp/#pyllamacpp.constants.LLAMA_CONTEXT_PARAMS_SCHEMA)
