FROM python:3.10.7
WORKDIR /app/
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY . .


ENV PYTHONPATH=/app
CMD python -m unittest -v ;python run.py