FROM python:3.13-slim

WORKDIR /app

COPY /Preprocessor/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY /Tools /app/Tools


COPY /Preprocessor /app/Preprocessor


CMD ["python", "-m" , "Preprocessor.Sub_And_Push"]

