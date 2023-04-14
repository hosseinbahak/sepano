<h1 align="center"> Store </h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Backend&message=Django DRF&color=blue">
  <img src="https://img.shields.io/static/v1?label=Database&message=SQLite&color=important">
</p>


Sepano is a basic api base store that provides jwt for users to authentication and request calls.  

## How to run
clone the project to your local machine. you can build and run dockerfile or run by virtual env.
dockerfile:
\ndocker build -t shipnow .
\ndocker run -p 8001:8000 shipnow

\nvirtual env:
\nvirtualenv .venv
\nsource .venv/bin/activate
\npython manage.py runserver 0.0.0.0:8000

## Documentation
The documentaions is available on homepage (localhost:8000/)

<img src="https://github.com/hosseinbahak/sepano/tree/main/media/doc.png">

## Contributor
* [hossein bahak](https://github.com/hosseinbahak) back-end and database developer
## License
The Moovie App is open source software licensed as [GPL-3.0](https://github.com/hosseinbahak/SE2/blob/main/LICENSE).

