FROM python:3.8-alpine3.12
LABEL developer="importhuman"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]