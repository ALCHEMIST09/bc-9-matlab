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
            Matlab.class_vars[identifier] = array
            print(Matlab.class_vars[identifier])
        else:
            if args in Matlab.class_vars:
                print(Matlab.class_vars[args])
            elif args.isnumeric():
                print(args)
            else:
                print('Undefined variable: ', args)
   
    
    def do_EOF(self, line):
        return True
        
if __name__ == '__main__':
    Matlab().cmdloop(intro=None)

