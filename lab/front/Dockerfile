FROM php:7.2-apache
#FROM python
#run pip install mysql-connector-python 
USER root
WORKDIR /var/www/html/
RUN touch query
RUN chmod 777 query
ADD index.php index.php 
ADD recebe_upload.php recebe_upload.php
EXPOSE 8080
#ADD conectar.py conectar.py
#CMD python conectar.py
