from bottle import route, run, template

#http://localhost:8068/.....<route>

@route("/")
def get_index():
    return ("home page")

@route("/hello")
@route("/hello/<name>")
def get_index(name="world"):
    return template("hello.tpl", name ="Jakub", extra="Happy Birthday")

@route("/greet")
@route("/greet/<name>")
def get_index(name="world"):
    return template("hello.tpl", name ="Jakub", extra="Happy Birthday")

@route("/greetings")
@route("/greetings/<names>")
def get_index(name="world"):
    names = name.split(',')
    return template("hello.tpl", name=None, names =names, extra="Happy Birthday")


run(host="localhost", port=8068)
