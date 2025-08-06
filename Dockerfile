FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
WORKDIR /code

COPY apt_requirements.txt /code/
RUN pip3 install pip --upgrade

RUN pip3 install wheel
RUN pip3 install --upgrade setuptools
RUN apt-get update

RUN apt-get update && \
    cat /code/apt_requirements.txt | xargs apt-get install -y && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt /code/
COPY entrypoint.sh /code/
RUN pip install --no-cache-dir -r requirements.txt
RUN rm /code/requirements.txt /code/apt_requirements.txt

# ENTRYPOINT /code/entrypoint.sh
