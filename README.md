# Run app via Docker

```
docker-compose up --build
```

# Local development

## Setup

Go to project dir and create new virtual environment
```
/app $: python3 -m venv env
```
Activate virtual environment
```
/app $: source env/bin/activate
```
Install packages
```
(env) /app $: pip install -r requirements.txt
```
Make database (sqlite)
```
(env) /app $: python manage.py makemigrations
(env) /app $: python manage.py migrate
```
## Run app
```
(env) /app $: python manage.py runserver
```
Run tests
```
(env) /app $: python manage.py test
```

# Other

## Admin

http://127.0.0.1:8000/admin/

```
login - admin
password - admin
```

## Endpoints

```
/<str:path>       
/most_popular        
/shorten_url     
/shortened_urls_count        
/shortened_urls_count/unique      
/test-redirect
```

## Load balancing

Provided example of docker-compose, Dockerfile and nginx.conf.
So DevOps Engineer can configure load balancing via nginx,
make several instances of the app.

Also you may configure gunicorn configuration