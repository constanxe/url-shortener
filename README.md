# url-shortener

## app

### database (one-time setup)
import `urls.sql` with the administration tool of your choice


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

:warning: <b>assumes database credentials of `root` username, empty password, `3306` port</b>
> update configuration in `settings.py` if needed


### client
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

access local app on http://localhost:8080/ or otherwise as provided


## tests

run this in the `client` folder for the unit tests [here](client/tests/unit/example.spec.js)
```
npm run test:unit
```
