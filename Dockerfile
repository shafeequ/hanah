FROM python:3.6
WORKDIR /tmp/hanah_assignment/
COPY projectmain  /tmp/hanah_assignment/
RUN python -m venv myenv && . myenv/bin/activate
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
