import sys


class Controller():
    """Controller for listening command line 
    arguments and sending parameters for Opendb class"""
    def __init__(self, file = 'todo-db.txt', arg = 'r'):
        # super(Controller, self).__init__()
        self.file = file
        self.arg = arg


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

        db = Database()

        if len(sys.argv) == 1:
            self.help_txt()
            # pass
        else:
            # return sys.argv[1:]
            if ( sys.argv[1] == '-l' ):
                
                db.open_db(self.file, self.arg)
                db.view()

            elif ( sys.argv[1] == '-a' ):
                # db = Database()
                db.open_db(self.file, self.arg)
                db.add_line()



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
            x.insert(0, str(number))
            line_list = self.line_list.append(x)
            number += 1

        file.close()
        print(self.line_list)

        return self.line_list


    def view(self):
            # print(self.line_list)
            for line in self.line_list:
                if line[1] == '0':
                    # print('\n',line[0], '[ ]' , line[2:], '\n')
                    print(line)
                    # print(','.join(line))

                else:
                    # print('\n',line[0], '[X]' , line[2:], '\n')
                    print(line)

                    # print ', '.join(mylist)





control = Controller()
control.arg_reader()











    # def add_line(self):
    #     print(self.line_list)
    #     # file.write("\n0;" + sys.argv[2].rstrip())

    #     self.line_list.append(sys.argv[2])
    #     print(self.line_list)

# class Parser(object):
#     """docstring for Parser"""
#     def __init__(self, arg):
#         super(Parser, self).__init__()
#         self.arg = arg
        


# control.help_txt()
    

# opendb_var = Database()
# print(opendb_var.open_db('todo-db.txt','r'))
