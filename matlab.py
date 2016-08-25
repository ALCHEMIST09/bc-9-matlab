import cmd, re

class Matlab(cmd.Cmd):
    intro = 'Welcome to the MATLAB. Type help or ? to list commands.\n'
    prompt = 'matlab>>>'
    file = None
    
    class_vars = {}
        
    commands = ['ARRAY', 'MATRIX', 'ADD', 'MULTIPLY']
        
    def default(self, args):
        '''
            Overide parent object default method and determine
            the kind of operation executed
        '''
        # Check for assignment expression e.g a = [1, 2, 3, 4]
        args = str(args)  
        if args.find('=') != -1:
            parts = str(args).split('=')
            identifier = parts[0].strip()
            array = parts[1]
            # Check if array contains semicolons, to determine
            # if it's a matrix
            if array.find(';') != -1:
                array = array.strip('[] ')
                array = array.replace(',', ' ')
                array = array.replace(';', '\n')
                Matlab.class_vars[identifier] = array
                print(Matlab.class_vars[identifier])
            elif array.isalpha():
                # Case of simple variable assignment
                Matlab.class_vars[identifier] = array
                print(Matlab.class_vars[identifier])
            else:
                # Normal array
                Matlab.class_vars[identifier] = array
                print(Matlab.class_vars[identifier])
        else:
            if args in Matlab.class_vars:
                print(Matlab.class_vars[args])
            elif args.isnumeric():
                print(args)
            else:
                print('Undefined variable: ', args)
    
    
    def do_zeros(self, num_rows):
        '''
            Create a vector of zeros that is of size num_rows
        '''
        vector = "0\n"
        vector *= int(num_rows)
        Matlab.class_vars[vector] = result
        print(Matlab.class_vars[vector])
        
    def compute_sum(self, a, b):
        '''
            Compute sum of two numbers
        '''
        return int(a) + int(b)
        
    def do_add_number_to_matrix(self, number):
        '''
            Add a number to a matrix. Convert the matrix
            into a single long list then add the number to
            each list element before turning it back into
            a matrix once again
        '''
#        matrix = Matlab.class_vars[matrix]
#        r = list(self.compute_sum(number, matrix))
        print(number)
        
    def do_greet(self, name):
        '''
            Greet name 
        '''    
        if name != None:
            print(name)
        else:
            print('Hey you folks')
    
    def do_EOF(self, line):
        print('Exiting Application, Bye')
        return True
        
if __name__ == '__main__':
    Matlab().cmdloop(intro=None)

