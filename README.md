# Cactus
Adapter to run an Azure Function Application with a WSGI Web Server.

#### How it works
Given the path of a folder containing a Function App, it builds a WSGI App parsing the Function settings. The app simply calls the Function main according to the route/methods settings.

#### Supported Function
This software is meant to support only Function which use binding httpTrigger as input and http as output. No other binding types. This is not an Azure emulator.

#### Function App structure
```
FunctionApp
|-- host.json
|-- function_1
|	|-- function.json
|	|-- __init__.py
|-- function_2
|	|-- function.json
|	|-- __init__.py
```

#### How to run

###### Create a file "wsgi.py"
```
from cactus.appfactory import build_app
app = build_app("YourFunctionAppFolder")
```
###### Run it with a WSGI Web Server
```
gunicorn wsgi:app
```
Checkout the [examples](examples) for more.
