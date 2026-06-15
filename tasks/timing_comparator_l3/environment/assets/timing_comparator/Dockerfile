FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
RUN mkdir -p /app && touch /app/flags.txt && chmod 666 /app/flags.txt
EXPOSE 5000
CMD ["python", "app.py"]
