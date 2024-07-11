FROM python:3.8.15
LABEL authors="keniwo"

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "app.py"]
CMD ["-p", "8050", "-n"]