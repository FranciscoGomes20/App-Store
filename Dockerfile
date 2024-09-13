FROM python:3.12.4-alpine3.20

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /APP_STORE

COPY requirements.txt .

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip

RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
     build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"

USER django-user

COPY . .

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
