FROM python:alpine3.7
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*

# install the plugin dependencies in the container
RUN pip install --upgrade pip
RUN pip install requirements.txt

# move the code 
COPY ./src/ /bin/
WORKDIR /bin/

ENTRYPOINT ["python", "main.py"]