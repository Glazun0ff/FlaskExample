from flask import Flask, escape, request

application = Flask(__name__)


@application.route("/")
def index():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@application.route("/help")
def helppage():
    return "<b><font color=blue>This is Help Page</font></b>"


@application.route("/user")
def usermain_page():
    return "User's Main Page"


@application.route("/user/<username>")
def show_user_page(username):
    return "Hello " + username.upper()


@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return "SubPath is: " + subpath


@application.route("/kvadrat/<int:x>")
def calc_kvadrat(x):
    return "Квадрат от " + str(x) + " = " + str(x*x)


@application.route("/calc")
def show_html_page():
    myfile = open("templates/calc.html", mode='r', encoding="utf-8")
    page   = myfile.read()
    myfile.close()
    return page


#--------Main------------------
if __name__ == "__main__":
#    application.debug = True
#    application.env   = "Working Hard"
    application.run()
#------------------------------
