FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV CURRENT_ENVIRONMENT=development

CMD ["python", "./app.py"]
