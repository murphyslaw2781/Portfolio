Use this to quickstart flask apps. You can copy or here are my steps.

Set up a virtual environment:
`python -m venv .venv`

Activate using
`source .venv/Scripts/activate`

Grab what you need to start (Flask and python-dotenv)
`pip install -r requirements.txt`

Create source folder, static (CSS), templates (HMTL)

Create __init__.py
```
from flask import Flask, render_template

app = Flask(__name__)
```

Create env files

`.flaskenv` is used to set your flask environment and call the flask app. 
**Note I put the code into a source folder, therefore you have to have an __init__.py file. Then all you have to do in `.flaskenv` is call the folder.** 
```
FLASK_APP=source
FLASK_ENV=development
```
.env
DB creds to come unless you have them ready

.gitignore
[Boilerplate gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)