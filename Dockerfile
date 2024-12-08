FROM python:3.12

ARG AUTHED_ARTIFACT_REG_URL
COPY ./requirements.txt /requirements.txt

RUN pip install --extra-index-url ${AUTHED_ARTIFACT_REG_URL} -r /requirements.txt
