FROM python:3.9-slim

RUN apt-get update && apt-get upgrade -y && apt-get -y install tk

COPY poetry.lock pyproject.toml .

RUN pip install 'poetry==1.5.0'

RUN poetry lock

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache

RUN poetry export -f requirements.txt --output requirements.txt && \
	pip install -r requirements.txt


COPY . .

EXPOSE 8000

#дефолтная команда
CMD [ "python", "app.py"]