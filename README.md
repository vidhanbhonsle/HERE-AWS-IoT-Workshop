# HERE AWS IoT Workshop

Creating and sustaining an IoT ecosystem can be a complex task. One of the key challenges is to track assets and derive actionable insights from their location data. This can be achieved by leveraging the full power of modern map and location services.

This repo will teach you how to integrate the location services and analytics in an IoT ecosystem consisting of an IoT edge device, AWS and user application.

#### Sign up for AWS Cloud at https://aws.amazon.com 
#### Get your HERE API Key at https://developer.here.com/events/NIPP

## Prerequisites

- Code IDE
- Python 3.X (https://www.python.org/downloads/)
- HERE Developer Account (https://developer.here.com/events/NIPP)
- AWS Cloud account (https://aws.amazon.com)
- Bring your Coffee/Tea and enjoy the journey 

## Steps

### Step 1: Create a Thing on AWS IoT

Create a thing and download the certificates and keys required for Authentication and Autorization.

- xxxx.cert.pem
- xxxx.private.key
- xxxx.public.key
- root-CA.crt

### Step 2: Create a Publisher code

Check geocode_data_publish.py file

install following Python library -
- pip install paho-mqtt

### Step 3: Create a Subscriber code

Check flaskserver.py file

install following Python library -
- pip install Flask-MQTT
- pip install Flask

### Step 4: Running the code

Open two different terminals or command prompt 

- python geocode_data_publish.py
- python flaskserver.py

### Resources

Following are the resources -

- Documentation
    - https://developer.here.com/documentation
- Tutorials
    - https://developer.here.com/tutorials
- Blogs 
    - https://developer.here.com/blog
- Github
    - https://github.com/heremaps 


