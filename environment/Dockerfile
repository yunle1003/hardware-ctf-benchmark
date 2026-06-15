FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    yosys \
    iverilog \
    python3 \
    python3-pip \
    build-essential

RUN pip3 install pyyaml numpy

WORKDIR /workspace
CMD ["/bin/bash"]
