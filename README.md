# Chatterbox

Small project that provides a LLM inside docker container.

- Model: DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf

- Base image: ghcr.io/ggerganov/llama.cpp:full

**Build docker image:**

```bash
git clone https://github.com/sergey31415926/Chatterbox.git
cd Chatterbox
docker build -t deepseek-chat .
```

**Run server locally inside container:**

```bash
docker run -p 8000:8000 deepseek-chat
# Server is running on http://localhost:8000
```