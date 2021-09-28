FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

RUN mkdir -p /app/rec

COPY main.py /app

EXPOSE 9011

CMD [ "python", "-u", "main.py" ]