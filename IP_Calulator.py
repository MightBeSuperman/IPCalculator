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
        iptobin()
        
    elif choice == "2":
        bintoip()
        
    elif choice == "99":
        sys.exit();
        
def iptobin():
    print 'we are still working on this part, hang in there.'
    menu();
    
def bintoip():
    print 'We are still working on this program, hang in there!'
    menu()
        
#Begin Program
if __name__ == "__main__":
    menu()
    

    


