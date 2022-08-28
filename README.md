# shortitpy
A URL shortener restfull api


## Set up
1. clone this repo
```bash
git clone git@github.com:ifilipe-lype/shortitpy.git
```
2. setup the enviroment
```bash
cd shortitpy
python3 -m venv venv
source venv/bin/activate
```
3. installs the dependencies
```bash
pip install -r requirements.txt
```
## Enviroments vars
2. creates a **.env** file, and fill in the blanks with your own data based on **.env.example file**

## Docker
1. You need to have both docker and docker-compose installed on your machine
```bash
docker-compose up --build -d
```
1. Or if you want to run the dev version (in watch mode)
```bash
docker-compose -f docker-compose.dev.yml up -d
```
## Run Development Server
1. The api is fastapi based and using uvicorn for dealing with async stuffs
```bash
uvicorn shortitpy.infra.http.server:app --reload
```

## TESTS (DEV)
1. Everything is setup for you, just run:
```bash
docker exec -it shortitpy-api ptw shortitpy
docker exec -it shortitpy-api pytest shortitpy --integration
```