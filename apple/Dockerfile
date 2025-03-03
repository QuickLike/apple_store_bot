FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN python manage.py collectstatic --noinput

RUN mkdir -p /backend_static/static

RUN cp -r /app/collected_static/. /backend_static/static/

RUN cp -r /app/media/. /media/

CMD ["sh", "-c", "python manage.py migrate && python manage.py loaddata db.json && python manage.py runserver 0:8000"]