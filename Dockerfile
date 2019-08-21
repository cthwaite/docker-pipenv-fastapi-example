FROM python:3.6-alpine

RUN apk add --no-cache --virtual .deps build-base
RUN pip install --upgrade pip setuptools pipenv

RUN mkdir /app
WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --deploy
RUN apk del .deps

ADD app.py /app
EXPOSE 8070
CMD ["uvicorn", "app:api", "--port", "8070", "--host", "0.0.0.0"]
