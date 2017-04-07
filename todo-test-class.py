import sys


class Controller():
    """Controller for listening command line 
    arguments and sending parameters for Opendb class"""
    def __init__(self):
        # super(Controller, self).__init__()
        # self.arg = arg
        pass

    def help_txt(self):
        """

        Python Todo application
            =======================

            Command line arguments:
             -l   Lists all the tasks
             -a   Adds a new task
             -r   Removes an task
             -c   Completes an task

             """
        print(self.help_txt.__doc__)


    def arg_reader(self):

        if len(sys.argv) == 1:
            self.help_txt()
        else:
            # return sys.argv[1:]
            if ( sys.argv[1] == '-l' ):
                db = Database()
                db.open_db('todo-db.txt','r')
                view = Database()
                view.view()

            elif ( sys.argv[1] == '-a' ):
                self.add_line()
            # pass


class Database():
    """Open database for further working process"""
    def __init__(self, line_list = []):
        # super(Database, self).__init__()
        self.line_list = line_list


    def open_db(self, openfile = '', open_arg = ''):
        self.openfile = openfile
        self.open_arg = open_arg
        number = 1

        file = open(self.openfile, self.open_arg)
        for line in file:
            x = line.rstrip().split(";")
            x.insert(0, number)
            # print(x)
            line_list = self.line_list.append(x)
            number += 1   

        return self.line_list

    def view(self):
            # print(self.line_list)
            for line in self.line_list:
                if line[1] == '0':
                    print('\n',line[0], '[ ]' , line[2:], '\n')
                else:
                    print('\n',line[0], '[X]' , line[2:], '\n')
        

    
        # for line in self.line_list:
        #     print(line)
        # line_list = line.rstrip().split(";")
        # if line_list[0] == '1':
        #     print(number,'[X] ',line_list[1])
        # else:
        #     print(number,'[ ] ',line_list[1])
        # number += 1







# class Parser(object):
#     """docstring for Parser"""
#     def __init__(self, arg):
#         super(Parser, self).__init__()
#         self.arg = arg
        


control = Controller()
control.arg_reader()
# control.help_txt()
    

# opendb_var = Database()
# print(opendb_var.open_db('todo-db.txt','r'))





















# def view():

#     file = open('todo-db.txt','r')
#     number = 1
#     for line in file:
#         line_list = line.rstrip().split(";")
#         if line_list[0] == '1':
#             print(number,'[X] ',line_list[1])
#         else:
#             print(number,'[ ] ',line_list[1])
#         number += 1
#     file.close()