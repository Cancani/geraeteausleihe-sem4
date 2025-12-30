FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libffi-dev \
    libcairo2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /srv

RUN addgroup --system app && adduser --system --ingroup app app

COPY service/requirements.txt /srv/requirements.txt
RUN pip install --no-cache-dir -r /srv/requirements.txt

COPY service/ /srv/

USER app

ENV PORT=8080
EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app"]
