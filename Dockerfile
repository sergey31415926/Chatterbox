FROM ghcr.io/ggerganov/llama.cpp:full

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Copy the GGUF model into the container
# COPY DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf /models/model.gguf
# Download model
RUN mkdir -p /models && \
    curl -L https://huggingface.co/SandLogicTechnologies/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf \
    -o /models/model.gguf

# Install Python bindings
ENV LLAMA_CPP_LIB=/llama.cpp/build/libllama.so
RUN pip3 install llama-cpp-python

COPY index.html .
COPY app.py .

# Override the default entrypoint
ENTRYPOINT []

EXPOSE 8000
CMD ["python3", "app.py"]
