from flask import Blueprint, render_template


views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/")
def index():
    """Renders the main HTML page."""
    return render_template("index.html")


@views_blueprint.route("/run")
def run_page():
    """Renders the run page."""
    return render_template("run.html")


@views_blueprint.route("/review")
def review_page():
    """Renders the review page."""
    return render_template("review.html")
