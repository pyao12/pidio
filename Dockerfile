FROM python:3.14-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN python csuh.py

EXPOSE 8000
CMD ["waitress-serve", "--listen=0.0.0.0:8000", "pidio.wsgi:application"]