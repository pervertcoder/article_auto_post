FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:main", "--host", "0.0.0.0", --port, "8000"]