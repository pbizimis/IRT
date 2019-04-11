# IRT

The new website for the IRT in Frankfurt.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites and Installing

What things you need to install the software and how to install them
- Python3
- Virtualenv
- Flask
- waitress

Start by creating the virtual environment:
```
/IRT/
python3 -m venv venv
```

Activate the virtual environment
```
/IRT/
source venv/bin/activate
```

Install waitress (Use pip not pip3)
```
/IRT/
pip install waitress
```

Install Flask (Use pip not pip3)
```
/IRT/
pip install Flask
```

## Starting the Server/Website

Activate the virtual environment if not already
```
/IRT/
source venv/bin/activate
```

Start the Server (You need sudo permission because the server runs on Port 80)
```
/IRT/
sudo python3 server.py
```
Serving on http://0.0.0.0:80