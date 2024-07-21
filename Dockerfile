FROM python:3.10-slim

ARG OPEN_API_KEY
ENV OPEN_API_KEY=${OPEN_API_KEY}

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]