FROM python:3.11.7-alpine3.17

WORKDIR /usr/src/app
COPY . .    

RUN pip install flask

EXPOSE 3000
RUN ls . 
CMD [ "flask", "--app=app", "run", "--host=0.0.0.0", "-p 3000" ]