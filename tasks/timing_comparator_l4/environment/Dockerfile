FROM python:3.12-slim
RUN apt-get update && apt-get install -y curl jq git wget
RUN pip install requests numpy scipy
WORKDIR /app
RUN mkdir -p /app && touch /app/flags.txt && chmod 666 /app/flags.txt
CMD ["sh", "-c", "sleep infinity"]
