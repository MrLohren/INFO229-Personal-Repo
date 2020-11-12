FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="xoxb-1443028917904-1416123583557-tk4CLFlbM3xQ4Xgl3HVlIKHC"
ENV SIGNING_SECRET="92df80f41db5ad53e8b71f68cbd5381d"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor-wikipedia

COPY ./nestorbot.py /nestorbot.py
COPY ./nestorbot_wikipedia.py /nestorbot_wikipedia.py

EXPOSE 5000

CMD [ "python", "/nestorbot_wikipedia.py" ]