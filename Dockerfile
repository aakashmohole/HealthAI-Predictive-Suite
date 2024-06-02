FROM python:3.12.1
COPY . /app 
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python app.py