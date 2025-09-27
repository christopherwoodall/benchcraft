import os
import json
import re
from flask import Flask, render_template, request, jsonify
import benchcraft


def main():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/static",
    )

    app.register_blueprint(benchcraft.routes.views.views_blueprint)
    app.register_blueprint(benchcraft.routes.api.api_blueprint)

    app.run(debug=True)


if __name__ == "__main__":
    main()
