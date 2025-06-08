

from click import File


try:
    f=  open("testfile.txt")
except Exception:
    print("Sorry, this file does not exist")
    
try:
    f=  open("testfile.txt")
    # var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else :
    print(f.read())
    f.close()
finally:
    print("Executing finally...")
    
# now we will create our own exception

try:
    f=  open("currupt_file.txt")
    if f.name == 'currupt_file.txt':
        raise Exception # manually raise exception
    # var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("err")
else :
    print(f.read())
    f.close()
finally:
     
    print("Executing finally...")
   
