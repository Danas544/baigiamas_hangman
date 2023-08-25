FROM python:3.10.7
WORKDIR /usr/src/app
COPY ./hangman_project/requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip uninstall -y itsdangerous
RUN pip install itsdangerous==2.0.1
COPY . /usr/src/app/



ENV PYTHONPATH=/app
EXPOSE 81
# CMD ["/usr/src/app/entrypoint.sh"]
CMD ["sh", "-c", "python -m unittest -v && TZ=Europe/Vilnius gunicorn -b 0.0.0.0:5002 run:gunicorn_app --workers 1 --threads 2 --log-config /usr/src/app/logging_config.ini --log-level debug 2>&1 | tee -a /usr/src/app/logs/hangman.log"]
# CMD python run.py
