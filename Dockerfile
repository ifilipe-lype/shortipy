FROM python:3.8.10

RUN mkdir /usr/src/shortipy

WORKDIR /usr/src/shortipy

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn", "shortipy.infra.http.server:app", "--host", "0.0.0.0", "--port", "80"]
