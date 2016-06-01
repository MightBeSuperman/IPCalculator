import sys
#Variables

yes = set(['yes', 'Yes', 'Y', 'y'])
no = set(['no', 'No', 'N', 'n'])

def logo():
    print """
 /$$$$$$ /$$$$$$$          /$$                     /$$$$$$$  /$$$$$$ /$$   /$$            
|_  $$_/| $$__  $$        | $$                    | $$__  $$|_  $$_/| $$$ | $$            
  | $$  | $$  \ $$       /$$$$$$    /$$$$$$       | $$  \ $$  | $$  | $$$$| $$            
  | $$  | $$$$$$$/      |_  $$_/   /$$__  $$      | $$$$$$$   | $$  | $$ $$ $$            
  | $$  | $$____/         | $$    | $$  \ $$      | $$__  $$  | $$  | $$  $$$$            
  | $$  | $$              | $$ /$$| $$  | $$      | $$  \ $$  | $$  | $$\  $$$            
 /$$$$$$| $$              |  $$$$/|  $$$$$$/      | $$$$$$$/ /$$$$$$| $$ \  $$            
|______/|__/               \___/   \______/       |_______/ |______/|__/  \__/            
                                                                                          
                                                                                          
                                                                                          
  /$$$$$$                                                      /$$                        
 /$$__  $$                                                    | $$                        
| $$  \__/  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$       /$$__  $$| $$__  $$|  $$  /$$//$$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$      | $$  \ $$| $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \__/  | $$    | $$$$$$$$| $$  \__/
| $$    $$| $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$        | $$ /$$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/| $$  | $$   \  $/  |  $$$$$$$| $$        |  $$$$/|  $$$$$$$| $$      
 \______/  \______/ |__/  |__/    \_/    \_______/|__/         \___/   \_______/|__/        
                                                    v0.1 (Alpha)
    """

def menu():
    print """
 /$$$$$$ /$$$$$$$          /$$                     /$$$$$$$  /$$$$$$ /$$   /$$            
|_  $$_/| $$__  $$        | $$                    | $$__  $$|_  $$_/| $$$ | $$            
  | $$  | $$  \ $$       /$$$$$$    /$$$$$$       | $$  \ $$  | $$  | $$$$| $$            
  | $$  | $$$$$$$/      |_  $$_/   /$$__  $$      | $$$$$$$   | $$  | $$ $$ $$            
  | $$  | $$____/         | $$    | $$  \ $$      | $$__  $$  | $$  | $$  $$$$            
  | $$  | $$              | $$ /$$| $$  | $$      | $$  \ $$  | $$  | $$\  $$$            
 /$$$$$$| $$              |  $$$$/|  $$$$$$/      | $$$$$$$/ /$$$$$$| $$ \  $$            
|______/|__/               \___/   \______/       |_______/ |______/|__/  \__/            
                                                                                          
                                                                                          
                                                                                          
  /$$$$$$                                                      /$$                        
 /$$__  $$                                                    | $$                        
| $$  \__/  /$$$$$$  /$$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$       /$$__  $$| $$__  $$|  $$  /$$//$$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$      | $$  \ $$| $$  \ $$ \  $$/$$/| $$$$$$$$| $$  \__/  | $$    | $$$$$$$$| $$  \__/
| $$    $$| $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$        | $$ /$$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/| $$  | $$   \  $/  |  $$$$$$$| $$        |  $$$$/|  $$$$$$$| $$      
 \______/  \______/ |__/  |__/    \_/    \_______/|__/         \___/   \_______/|__/        
                                                    v0.1 (Alpha)
                                                
    Select Your Operation: 
    1 : Convert from IPv4 to Binary 
    2 : Conver from Binary to IPv4
    99 : Exit
    """
    choice = raw_input("Enter Your Choice:")
    
    if choice == "1":
        iptobin_first()
        
    elif choice == "2":
        bintoip()
        
    elif choice == "99":
        sys.exit();
        
def iptobin_first():
    first = raw_input("Enter the First Octet: ___.XXX.XXX.XXX")
    if first == "128":
        print " 1 0 0 0  0 0 0 0"
        iptobin_second();
    
    elif first == "192":
        print " 1 1 0 0  0 0 0 0"
        iptobin_second();
    
    elif first == "224":
        print " 1 1 1 0  0 0 0 0"
        iptobin_second();
    
    elif first == "240":
        print " 1 1 1 1  0 0 0 0"
        iptobin_second();
    
    elif first == "248":
        print " 1 1 1 1  1 0 0 0"
        iptobin_second();
    
    elif first == "252":
        print " 1 1 1 1  1 1 0 0"
        iptobin_second();
    
    elif first == "254":
        print " 1 1 1 1  1 1 1 0"
        iptobin_second();
    
    elif first == "255":
        print " 1 1 1 1  1 1 1 1"
        iptobin_second();
    
    elif choice == " ":
        menu();
    
def bintoip():
    print 'We are still working on this program, hang in there!'
    menu()
    
def iptobin_second():
        if choice == "128":
            print " 1 0 0 0  0 0 0 0"
            iptobin_second();
    
        elif choice == "192":
            print " 1 1 0 0  0 0 0 0"
            print 
    
        elif choice == "224":
            print " 1 1 1 0  0 0 0 0"
            iptobin_second();
    
        elif choice == "240":
            print " 1 1 1 1  0 0 0 0"
            iptobin_second();
    
        elif choice == "248":
            print " 1 1 1 1  1 0 0 0"
            iptobin_second();
    
        elif choice == "252":
            print " 1 1 1 1  1 1 0 0"
            iptobin_second();
    
        elif choice == "254":
            print " 1 1 1 1  1 1 1 0"
            iptobin_second();
    
        elif choice == "255":
            print " 1 1 1 1  1 1 1 1"
            iptobin_second();
    
        elif choice == " ":
            menu();
    

        
#Begin Program
if __name__ == "__main__":
    menu()
    

    


