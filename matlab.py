import cmd, re, math, pickle

class Matlab(cmd.Cmd):
    intro = 'Welcome to the MATLAB. Type help or ? to list commands.\n'
    prompt = 'matlab>>>'
    file = None
    
    '''
        Class variable to be used to persist properties
        assigned to the class
    '''
    class_vars = {}
        
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
                matrix = self.create_matrix(array)
                Matlab.class_vars[identifier] = matrix
                print(Matlab.class_vars[identifier])
            elif array.isalpha():
                # Case of simple variable assignment
                Matlab.class_vars[identifier] = array
                print(Matlab.class_vars[identifier])
            else:
                # Normal array
                Matlab.class_vars[identifier] = array
                print(Matlab.class_vars[identifier])
        elif args.find('+') != -1:
            # Case of adding a matrix and a number 
            parts = str(args).split('+')
            left_operand = parts[0].strip()
            right_operand = parts[1].strip()
            self.add_number_to_matrix(left_operand, right_operand)
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
        
    def create_matrix(self, parameter):
        '''
            Construct matrix from an argument that
            resembles an array
        '''
        parameter = parameter.strip('[] ')
        parameter = parameter.replace(',', ' ')
        parameter = parameter.replace(';', '\n')
        return parameter
    
    def add_number_to_matrix(self, number, matrix):
        '''
            Add a number to a matrix
        '''
        matrix = matrix.strip('[] ')
        matrix = matrix.replace(', ', '')
        matrix_order = matrix.find(';') 
        matrix = matrix.replace('; ', '')
        list_matrix = list(matrix)
        result = []
        for item in list_matrix:
            item = int(item)
            item += int(number)
            result.append(str(item))
        print(result)
        
    def do_load(self, filename):
        '''
            Save data from a previous session
            to workspace
        '''
        ext = '.mat'
        file = filename + ext
        with open(file, 'rb') as handle:
            unserialized_data = pickle.load(handle)
            print(unserialized_data)
            
    def do_save(self, filename):
        '''
            Save the variables in the working area
        '''
        ext = '.mat'
        file = filename + ext
        with open(file, 'wb') as handle:
            pickle.dump(Matlab.class_vars, handle)
    
    def do_EOF(self, line):
        print('Exiting Application, Bye')
        return True
        
if __name__ == '__main__':
    Matlab().cmdloop(intro=None)

