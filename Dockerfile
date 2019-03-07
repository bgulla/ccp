FROM python:2-alpine
MAINTAINER Brandon Gulla "hey@bgulla.dev"

COPY ./src /app

# Create no privelged user
RUN addgroup -S dev && \
    adduser -S -G dev dev && \
    chown -R dev:dev /app
WORKDIR /app

# Install the dependencies from PIP
RUN pip install -r requirements.txt

USER dev

ENTRYPOINT ["python"]
CMD ["app.py"]
