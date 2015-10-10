from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route('/application-form')
def application_page():
    """Show application form"""

    return render_template("application-form.html")


@app.route("/application")
def application_submit():
    first_name = request.args.get('first-name')
    last_name = request.args.get('last-name')
    salary = request.args.get('salary-requirement')
    position = request.args.get('position')
    return render_template("application-response.html",
                            first_name=first_name, last_name=last_name,
                            salary=salary, position=position)

if __name__ == "__main__":
    app.run(debug=True)
