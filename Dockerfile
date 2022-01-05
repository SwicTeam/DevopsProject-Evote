FROM ubuntu:latest
# install python 3 and pip
RUN apt-get update
RUN apt-get install python3 -y
RUN apt install python3-pip -y && pip3 install --upgrade pip
RUN alias python=python3
RUN mkdir pfe_project
COPY . pfe_project/
RUN cd pfe_project/ && pip install -r requirements.txt
CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
