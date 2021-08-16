FROM python:3.8

RUN pip3 install --upgrade pip

#set a directory for the app
WORKDIR /app

#copy all the files in the root path to the container
COPY . /app

#install the dependencies
RUN pip install flask geopy


#execute the program
CMD ["python3", "app.py"]