InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Paige",  
               "LastName": "McCartin",  
               "DOB": "April 30",  
               "Residence": "San Diego",  
               "Email": "pmccartin43005@gmail.com",  
               "Owns_Cars":["Range Rover","Tesla Model S","Volkswagen Passat"]  
              })  

InfoDb.append({  
               "FirstName": "Bria",  
               "LastName": "Gilliam",  
               "DOB": "September 27",  
               "Residence": "Los Angelus",  
               "Email": "briagee101@gmail.com",  
               "Owns_Cars":["BMW","Nissan","Toyota"]  
              })  

          
# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)
# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

def fibonacci(a, b, n):
  if n < 10:
    c = a+b
    print(str(a) + " + " + str(b) + " = " + str(c))
    fibonacci(b, c, n+1)

fibonacci(1, 2, 0)

def tester():
  print(“For loop:“)
  printFor()
  print(“While loop:“)
  printWhile(0)
  print(“Recursive loop:“)
  printRecursive(0)
tester()