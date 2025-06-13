FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install-y ffmpeg && apt-get clean

COPY required_packages.txt .
RUN pip install --nocache-dir - r required_packages.txt

COPY . .

CMD ["python", "bot.py"]