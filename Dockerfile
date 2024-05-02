FROM python:3.10.8
WORKDIR /app
COPY . /app
RUN pip install Flask

EXPOSE 8000

CMD ["python3", "main.py"]