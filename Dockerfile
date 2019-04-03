FROM python:3.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /usr/src/app

#ADD startme.sh startme.sh

#ENTRYPOINT ["sh", "startme.sh"]

CMD ["python", "./main.py"]
