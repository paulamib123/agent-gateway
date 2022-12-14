# Create a data folder inside validateAgentOutputAPI folder
# docker run -p 5000:5000 -v <your-path-to-data-folder>:/server/data <container-name>

FROM python:3.9

RUN mkdir /server

COPY . /server

ENV PYTHONPATH=/server

RUN mkdir /server/data

WORKDIR /server

RUN pip3 install -r requirements.txt

WORKDIR /server/validateAgentOutputAPI/api

CMD ["python3", "app.py"]