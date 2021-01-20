'''WIP controller'''

wip = [
    {'id': 1, 'name': 'javaScript', 'body': 'q. How do you comfort a JavaScript bug? a. You console it'},
    {'id': 2, 'name': 'Python', 'body': ""},
    {'id': 3, 'name': 'Node', 'body': "q. Why was the JavaScript developer sad? a. Because they didn't Node how to Express himself"},
    {'id': 2, 'name': 'React', 'body': "q. Why did the functional component feel lost? a. Because it didn't know what state it was in!"}
    
    ]

def index(req):
    return [item for item in wip], 200


def create(req):
    new_wip = req.get_json()
    new_wip['id'] = sorted([c['id'] for c in wip])[-1] + 1
    wip.append(new_wip)
    return new_wip, 201

# url = https://v2.jokeapi.dev/joke/Programming:

# r = request.get(url)
# r_dict = r.json()


