FROM python:3.13-slim

WORKDIR /app

COPY /Enricher/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY /Tools /app/Tools


COPY /Enricher /app/Enricher


CMD ["python", "-m" , "Enricher.Sub_and_pub"]

