FROM python:3.12-alpine3.19
LABEL maintainer="Tonny-Bright Sogli"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./scripts /scripts

COPY ./ /app
WORKDIR /app

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /vol && \
    mkdir -p /vol/web && \
    mkdir -p /vol/web/media && \
    mkdir -p /var/log && \
    touch /var/log/backend.log && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chown -R django-user:django-user /var/log/backend.log && \
    chmod -R +x /var/log && \
    chmod -R +x /scripts

EXPOSE 8000

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

# CMD ["run.sh"]

