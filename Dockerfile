FROM ubuntu:14.04
MAINTAINER Gauree

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install the necessary Django specific packages
RUN sudo apt-get update && \
  sudo apt-get -y upgrade && \
  sudo apt-get install -y python2.7 python2.7-dev python-pip sqlite3 && \
   pip install django && \
  sudo apt-get clean && \
  sudo rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/eventbrite 
ADD helloworld/ /opt/eventbrite/helloworld
ADD mysite /opt/eventbrite/mysite
ADD manage.py /opt/eventbrite

USER root
EXPOSE 8000
CMD ["sudo","python", "/opt/eventbrite/manage.py", "runserver", "0.0.0.0:8000", "--traceback"]
