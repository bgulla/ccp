FROM python:2
MAINTAINER Brandon Gulla "hey@brandongulla.com"
COPY ./src /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
