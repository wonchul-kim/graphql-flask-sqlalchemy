FROM python:3.9

WORKDIR /usr/src/app 

COPY requirements.txt .

RUN pip install --upgrade pip 
# RUN apt-get install libpq-dev python3-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]