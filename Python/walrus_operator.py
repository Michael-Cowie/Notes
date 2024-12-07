"""The walrus operator is used for assignment of variables inside expressions"""
sum_result = 10 + 5
if (sum_result > 10):
    print(sum_result) # 15
    
# Can now become
if (sum_result := 10 + 5) > 10:
    print(sum_result) # 15
    
# However remember the parentheses 
if sum_result := 10 + 5 > 10:
    print(sum_result) # True, because it is doing sum_result = (10 + 5 > 10)
 
############################################################################   
    
# Another example
command = input("> ")
while command != "quit":
    print("You entered:", command)
    command = input("> ")
    
# Can become
while (command := input("> ")) != "quit":
    print("You entered:", command)