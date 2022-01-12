FROM python:3.9.5

RUN pip install gunicorn --upgrade pip

ADD . /first
WORKDIR /app

COPY . /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
EXPOSE 8000

CMD ["gunicorn", "--config=gunicorn.py", "run:app"]