FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /simple_solutions

COPY requirements.txt /simple_solutions/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

COPY . /simple_solutions/