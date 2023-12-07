import requests
from pprint import pprint

#get
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
pprint(resultado_get.json())

#get id
getWithId = requests.get('https://jsonplaceholder.typicode.com/todos/2')
pprint(getWithId.json())

#post
nova_tarefa = {'completed': False,
 'id': 2,
 'title': 'lavar o carro',
 'userId': 1}

rasultadoPost = requests.post('https://jsonplaceholder.typicode.com/todos/', nova_tarefa)
pprint(rasultadoPost.json())


#put
tarefaAlterada = {'completed': False,
 'id': 2,
 'title': 'lavar a moto',
 'userId': 1}
resultadoPut = requests.put('https://jsonplaceholder.typicode.com/todos/2', tarefaAlterada)
pprint(resultadoPut.json())


#delete
resultadoDelete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultadoDelete.json())








