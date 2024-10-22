FROM python:3.10-slim-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p app

COPY ./App app

WORKDIR app 
#cambia el directorio a la carpeta app

EXPOSE 5000
#puerto por donde vamos a recibir y demás

CMD ["python3", "app.py"]

