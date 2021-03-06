# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

WORKDIR /app
COPY requirments.txt requirments.txt
RUN pip3 install -r requirments.txt
COPY . .
#CMD ["/bin/sh"]
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]