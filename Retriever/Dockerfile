FROM python:3.13-slim

WORKDIR /app

COPY /Retriever/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY /Tools /app/Tools


COPY /Retriever /app/Retriever


CMD ["python", "-m" , "Retriever.main"]

