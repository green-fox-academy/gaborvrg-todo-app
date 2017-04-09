import sys
import os


class Controller():
    """Controller for listening command line arguments and sending parameters for Opendb class"""
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
        pars = Parser()

        if len(sys.argv) == 1:
            os.system('clear')
            self.help_txt()
            # pass
        else:
            # return sys.argv[1:]
            if ( sys.argv[1] == '-l' ):
                
                db.open_db(self.file, self.arg)
                db.view()

            elif ( sys.argv[1] == '-a' ):
                if len(sys.argv) == 2:
                    os.system('clear')
                    print('\n', 'Unable to add: no task provided' ,'\n')
                    db.open_db(self.file, self.arg)
                    db.view()
                else:
                    # db = Database()
                    db.open_db(self.file, self.arg)
                    pars.add_line(self.file)
                    os.system('clear')
                    db.view()

            elif ( sys.argv[1] == '-c' ):
                # db = Database()
                db.open_db(self.file, self.arg)
                pars.complete(self.file)
                os.system('clear')
                db.view()

            elif ( sys.argv[1] == '-r' ):
                if len(sys.argv) == 2:
                    os.system('clear')
                    print('\n', 'Unable to remove: index is not a number' ,'\n')
                    db.open_db(self.file, self.arg)
                    db.view()
                else:
                    # db = Database()
                    db.open_db(self.file, self.arg)
                    pars.remove(self.file)
                    os.system('clear')
                    db.view()
            else:
                os.system('clear')
                print('\n' + 'Unsupported argument!!! Try again: ' + '\n')
                db.open_db(self.file, self.arg)
                db.view()




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

        return self.line_list


    def view(self):

        for line in self.line_list:
            if line[1] == '0':
                print('\n',line[0], '[ ]' , ','.join(line[2:]))
            
            else:
                print('\n',line[0], '[X]' , ','.join(line[2:]))



class Parser(Database):
    """docstring for Parser"""

    def add_line(self, file):

        len_list = len(self.line_list) + 1
        extend_list = [str(len_list),'0',sys.argv[2]]
        self.line_list.append(extend_list)

        file = open(file, 'w')

        for item in self.line_list:
            join_item = ';'.join(item[1:])
            file.write(join_item + '\n')
            
        file.close()


    def remove(self,file):

        for item in self.line_list:
            if item[0] == sys.argv[2]:
                self.line_list.remove(item)

        file = open(file, 'w')

        for item in self.line_list:
            join_item = ';'.join(item[1:])
            file.write(join_item + '\n')
            
        file.close()


    def complete(self,file):

        for line in self.line_list:
            if sys.argv[2] == line[0] and line[1] != '1':
                line[1] = '1'
            else:
                pass

        file = open(file, 'w')

        for item in self.line_list:
            join_item = ';'.join(item[1:])
            file.write(join_item + '\n')
        file.close()




control = Controller()
control.arg_reader()

