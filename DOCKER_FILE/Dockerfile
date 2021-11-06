FROM python  
MAINTAINER Teste
CMD yes | apt install python3-pip 
ADD back.py /opt/
WORKDIR /opt
RUN python back.py 
EXPOSE 7070