FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt ./src/requirements.txt

WORKDIR /src
RUN pip install --no-cache-dir -r requirements.txt

ADD ./src /src

RUN adduser -D user
RUN chown user:user -R /src/
USER user

# COPY ./run_web.sh /src/run_web.sh
# COPY ./entrypoint.sh /src/entrypoint.sh
# CMD sh ./entrypoint.sh
