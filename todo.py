import sys


def help_txt():

    file = open('help.txt','r')
    helptxt = file.read()
    print(helptxt)


def arg_reader():

    if len(sys.argv) == 1:
        help_txt()
    else:
        # return sys.argv[1:]
        if ( sys.argv[1] == '-l' ):
            todo_db()
        elif ( sys.argv[1] == '-a' ):
            add_line()


def todo_db():
    file = open('todo-db.txt','r')
    todo_db = file.read()
    print(todo_db)
    file.close()


def add_line():
    # print(sys.argv[2])

    file = open('todo-db.txt','a') 
    file.write("\n0;" + sys.argv[2].rstrip())
    file.close()
    view()


def view():
    file = open('todo-db.txt','r')
    view_file = file.readline().rstrip()
    view_list = view_file.split(';')
    file.close()
    print(view_list)



arg_reader()




