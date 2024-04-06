FROM alpine:latest
RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev 
RUN pip install --break-system-packages --upgrade pip
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install --break-system-packages -r requirements.txt
CMD ["python3", "app.py"]