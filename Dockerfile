FROM python:3.11-bullseye

WORKDIR /code

COPY . /code/
RUN pip install -e .['dev'] --upgrade --no-cache

ENV FLASK_APP=/code/telecom_carrier/app.py
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
