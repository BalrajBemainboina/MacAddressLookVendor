FROM python:2.7-slim

WORKDIR /Macapp

COPY . /Macapp

CMD ["python","/Macapp/MacAddressLook.py"]