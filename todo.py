import sys


def arg_reader():

    if len(sys.argv) == 1:
        file = open('help.txt','r')
        helptxt = file.read()
        return helptxt

    else:
        return sys.argv[1:]





arguments = arg_reader()
print(arguments)

# if len(arguments) == 0:
#     print('help text')

# elif:
#     if( arguments[0] == '-l' ):
#         print('Addolunk ilyet', arguments[1])
# elif:
#     if( arguments[0] == '-a' ):
#         print('Addolunk ilyet', arguments[1])
# else:
#     if( arguments[0] == '-c' ):
#         print('Addolunk ilyet', arguments[1])