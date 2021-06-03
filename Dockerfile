From python:3.8

ADD . .

RUN pip install discord requests

CMD [ "python3", "./main.py" ]