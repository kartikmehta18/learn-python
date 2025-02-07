

from click import File


try:
    f=  open("testfile.txt")
except Exception:
    print("Sorry, this file does not exist")
    
try:
    f=  open("testfile.txt")
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

