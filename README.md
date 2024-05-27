## Setup

Requires a config.json file
with the following values
```
{
    "POCKET_CONSUMER_KEY": "consumer key from pocket setup",
    "REDIRECT_URI": "url on site you would like pocket to redirect you to",
    "SECRET_KEY": "secret"
}
```

## running

after installing flask you can run the following to start in debug mode:
```
flask --app app run --debug
```