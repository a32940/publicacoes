FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY pubicacoesApp/ ./code/

ADD requirements.txt /code/

RUN pip install -r requirements.txt

#RUN python manage.py migrate

#CMD ["python","manage.py", "migrate"]
