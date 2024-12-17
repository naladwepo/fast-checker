FROM python:3.9-slim

WORKDIR /model

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "model_service.py"] 