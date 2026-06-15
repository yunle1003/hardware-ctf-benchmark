FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    yosys \
    iverilog \
    python3 \
    python3-pip \
    build-essential \
    git \
    curl \
    nano

RUN pip3 install \
    pyyaml \
    numpy \
    jsonschema

WORKDIR /workspace

RUN mkdir -p /app /logs/agent /logs/verifier

ENV YOSYS_VERSION=0.66
ENV IVERILOG_VERSION=12.0

RUN echo "Yosys $(yosys --version 2>&1)" && \
    echo "iverilog $(iverilog -V 2>&1 | head -1)"

CMD ["/bin/bash"]
