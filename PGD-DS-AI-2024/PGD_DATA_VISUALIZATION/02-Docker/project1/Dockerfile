# download base image from dockerhub.com
FROM python:3.12-slim

# create new app folder in linux image
WORKDIR /app

# copy from base operating system to linux image
COPY . ./app/

CMD ["python", "./app/my_code.py"]