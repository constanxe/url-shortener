# url-shortener

## app

### database (one-time setup)
import `urls.sql` into the administration tool of your choice


### server
run the following in the `server` folder

1. install Flask dependencies (one-time setup)
```
python -m venv env
env/Scripts/activate
pip install -r requirements.txt
```

2. run app
```
python app.py
```


### client
:warning: ensure that the server app is running before doing either of the following options:

access deployed app on https://urlshortener1.netlify.app/

-OR-

run the following in the `client` folder

1. install Vue dependencies (one-time setup)
```
npm install
```

2. run app
```
npm run serve
```

3. access local app on http://localhost:8080/ or otherwise as provided


## tests

run the following in the `client` folder
```
npm run test:unit
```
