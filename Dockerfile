FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ARG WORKDIR=/app

WORKDIR ${WORKDIR}

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ${WORKDIR}

# copy & enable entrypoint
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]