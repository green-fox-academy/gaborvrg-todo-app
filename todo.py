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
            view()
            # todo_list()
        elif ( sys.argv[1] == '-a' ):
            add_line()
        # elif ( sys.argv[1] == '-c' ):
        #     complete()
        # elif ( sys.argv[1] == '-c' ):
        #     pass



def add_line():
    # print(sys.argv[2])

    file = open('todo-db.txt','a') 
    file.write("\n0;" + sys.argv[2].rstrip())
    file.close()
    view()


def view():

    file = open('todo-db.txt','r')
    number = 1
    for line in file:
        line_list = line.rstrip().split(";")
        if line_list[0] == '1':
            print(number,'[X] ',line_list[1])
        else:
            print(number,'[ ] ',line_list[1])
        number += 1
    file.close()


# def complete():

#     file = open('todo-db.txt','r')
#     line_num = 1

#     for lines in file:
#         # line_list = lines.rstrip().split(";")
#         if line_num == sys.argv[2]:
#             print >>file, lines + lines



#         # print(line_list)
#         # print(line_num, lines.rstrip())
#         line_num += 1

    

arg_reader()











# # outF = open("myOutFile.txt", "w")
# # >>>for line in textList:
# # ...  print >>outF, line
# # >>>outF.close()

# def todo_list():

#     file = open('todo-db.txt','r')
#     todo_db = file.read()
#     print(todo_db)
#     file.close()
