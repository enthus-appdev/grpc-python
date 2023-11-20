### Python setup
```
$ python -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip
```
### grpc für Python
```
$ python -m pip install grpcio
```
### Stargate repo klonen
```
$ git clone git@gitlab.com:mclgmbh/enthus-apis.git
```
### Stargate python interfaces etc. generieren:
Diese Schritte müssen für jede neue Version von Stargate wiederholt werden, 
aber nur wenn die neue Version auch explizit genutzt werden soll. Stargate ist immer Rückwärtskopatibel,
auch ohne Update.
```
$ cd enthus-apis
$ git pull
$ buf generate
```
"stargate" und "buf" aus dem "gen/python" folder in das Python-script-Verzeichnis kopieren
evtl file anlegen in buf folder (python import fail)

```
$ python grpc_example.py
```
