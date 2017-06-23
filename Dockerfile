FROM alpine:3.6

ENV PYTHONUNBUFFERED 1

# runtime dependencies
RUN \
    apk add --no-cache \
        curl \
        bash \
        python3 \
        python3-dev \
        libpq \
        libjpeg-turbo \
        postgresql

RUN \
    apk add --no-cache \
        ca-certificates \
        openssl && \
    wget -O /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py" && \
    python3 /tmp/get-pip.py && \
    rm -f /tmp/get-pip.py

RUN mkdir -p /code/requirements
WORKDIR /code
ADD requirements /code/requirements/


# build dependencies + install requirements
RUN \
    apk add --no-cache \
        gcc \
        musl-dev \
        postgresql-dev \
        git \
        zlib-dev \
        jpeg-dev \
        linux-headers && \
    pip3 install -r requirements/devel.txt && \
    apk del \
        gcc \
        musl-dev \
        postgresql-dev \
        git \
        jpeg-dev \
        zlib-dev \
        linux-headers

ADD . /code