FROM python:3.13-slim

WORKDIR /app

COPY /DataPersister/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY /Tools /app/Tools


COPY /DataPersister /app/DataPersister


CMD ["python", "-m" , "DataPersister.main"]

