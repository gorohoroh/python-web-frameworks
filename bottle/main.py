from bottle import run, route, template

@route('/')
def home():
    return (''
            '<h1>This is a site powered by bottle</h1>'
            '')

about_me = """
<h1>About me</h1>
<ul>
    <li>Technical writer</li>
    <li>Product marketer</li>
    <li>Amateur developer</li>
</ul>
"""

@route('/about')
def about():
    return about_me

people_list = [
    {'name': 'John', 'age': 45, 'job': 'Software Engineer'},
    {'name': 'Christina', 'age': 32, 'job': 'QA Engineer'},
    {'name': 'Josh', 'age': 30, 'job': 'Administrator'}
]

@route('/people')
def people():
    return template('people', people = people_list)

run(debug=True, reloader=True)