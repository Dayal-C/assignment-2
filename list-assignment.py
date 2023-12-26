fruits=['apple','orange','strawberry','mangoes','grapes','banana']
fruits_new='e'
print("Theoriginal list is:",fruits)
for elem in fruits[:]:
    if any(char in elem for char in fruits_new):
        fruits.remove(elem)
    
    
print("The list after removal:",fruits)
