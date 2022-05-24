from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    session,
    url_for,
    request,
    abort,
)
pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)

"""
Storing my projects here instead of Database.
Using a slug_to_projects Dict to pass to a route for projects
for example slug_to_project = Slug:{All of Data}
Making an Index to make it easier to search.
"""
projects = [
    {
        "name": "What to watch next!?!",
        "thumb": "img/watch-list.png",
        "hero": "img/watchlist-hero.png",
        "categories": ["python", "flask","MongoDB","Heroku"],
        "slug": "movie-watchlist",
        "prod": "https://movie-watchlist-flask-tap.herokuapp.com/",
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
    },
]
slug_to_project = {project["slug"]: project for project in projects}


@pages.route("/")
def home():
    return render_template("home.html", projects=projects)


@pages.route("/about")
def about():
    return render_template("about.html")


@pages.route("/contact")
def contact():
    return render_template("contact.html")

# You need to create "project_"slug".html to render pages
@pages.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])


@pages.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
