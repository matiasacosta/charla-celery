FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /codigo
WORKDIR /codigo
COPY requirements.txt /codigo/
RUN pip install -r requirements.txt
COPY . /codigo/