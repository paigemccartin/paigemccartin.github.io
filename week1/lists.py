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


InfoDb.append({  
               "FirstName": "Natalie",  
               "LastName": "Cohen",  
               "DOB": "July 6",  
               "Residence": "San Diego",  
               "Email": "ncohen6@gmail.com",  
               "Owns_Cars":["Mercedes","G-Wagan","Ford"]  
              })  


InfoDb.append({  
               "FirstName": "Calissa",  
               "LastName": "Tyrell",  
               "DOB": "June 5",  
               "Residence": "San Diego",  
               "Email": "Calissaty@gmail.com",  
               "Owns_Cars":["Honda","Audi","Porche"]  
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

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return


def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

if __name__ == "__main__":
    tester()