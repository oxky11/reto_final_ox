FROM python:3.9.21

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN bash ./manage.sh

CMD [ "python", "./run.py" ]