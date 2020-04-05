FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev


COPY ./src /src

COPY requirements.txt /src

WORKDIR /src

RUN pip install --no-cache-dir -r requirements.txt


RUN adduser -D user
RUN chown user:user -R /src/
USER user

COPY entrypoint.sh /src
CMD ["/entrypoint.sh"]
