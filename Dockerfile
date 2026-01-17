FROM python:3.14-slim
WORKDIR /app
COPY . .

RUN mkdir -p /app/data
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py collectstatic --noinput
RUN chmod +x start.sh

EXPOSE 8000
CMD ["./start.sh"]