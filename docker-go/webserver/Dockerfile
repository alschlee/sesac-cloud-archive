#FROM ubuntu 
#ENV DEBIAN_FRONTEND=noninteractive
#RUN apt-get update
#RUN apt-get install apache2 -y
#RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
#ADD hello.html /var/www/html/
#CMD apachectl -D FOREGROUND

#FROM    ubuntu
#WORKDIR /var/www/html
#ENV     DEBIAN_FRONTEND=noninteractive
#RUN     apt-get update
#RUN     apt-get install apache2 -y
#RUN     echo "ServerName localhost" >> /etc/apache2/apache2.conf
#ADD     hello.html .
#EXPOSE  80
#CMD     apachectl -D FOREGROUND

FROM    ubuntu
WORKDIR /var/www/html
ENV     DEBIAN_FRONTEND=noninteractive
RUN     apt-get update
RUN     apt-get install apache2 -y
RUN     echo "ServerName localhost" >> /etc/apache2/apache2.conf
ADD     hello.html .
EXPOSE  80
CMD     ["apachectl", "-D FOREGROUND"]