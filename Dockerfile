FROM python:3.7.3-stretch

WORKDIR /app

COPY . app.py /app/

# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip && pip install -r --no-cache-dir requirements.txt 
# RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python" , "app.py"]
