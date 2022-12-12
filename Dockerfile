FROM  python:3.6

RUN mkdir /app
WORKDIR /app
COPY ./uwsgi.ini /app
COPY ./wsgi.py /app
COPY ./entrypoint.sh /app
COPY ./requirements.txt /app
ADD devops_app /app

RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt
RUN chmod +x ./entrypoint.sh
RUN ls