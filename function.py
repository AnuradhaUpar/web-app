FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as file:
        todos_local=file.readlines()
        return todos_local



def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath,'w') as file:
        #todos_locals=file.readline()
        #todos_locals.append(todos_arg)
        file.writelines(todos_arg)

