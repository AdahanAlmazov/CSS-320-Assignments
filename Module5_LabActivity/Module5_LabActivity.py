

set_x = {}      #empty set
print(set_x)

set_n = { 0, 1, 2, 3, 4} #none empty set
print(set_n)

set_colors = set()
set_colors.add("red")       #Add colors
print("Colors in set:", set_colors)
set_colors.update(["blue", "green"])         #Update colors 
print("Updated colors in set:", set_colors)

set_x = {"green", "blue"}
set_y = {"blue", "yellow"}
intersection_set = set_x.intersection(set_y)        #easier way to find an intersaction
print("Intersection of sets:", intersection_set)
set_z = set_x & set_y       #finding intersection of set_x and set_y
print("Intersection of sets:", set_z)

sets_x = {"green", "blue"}
sets_y = {"blue", "yellow"}
union_sets = sets_x.union(sets_y)       #easier way to find a union of sets_x and sets_y
print("Union of sets:", union_sets)
sets_z = sets_x | sets_y        #finding intersection of sets_x and sets_y 
print("Union of sets:", sets_z)

sets_x = {"apple", "mango"}
sets_y = {"mango", "orange"}
print(sets_x.issubset(sets_y))      #neither of them is subset
print(sets_y.issubset(sets_x))      #neither of them is subset
print("Easier way of Difference of sets_x and sets_y:", sets_x.difference(sets_y))    #more easier way to find difference
print("Easier way of Difference of sets_y and sets_x:", sets_y.difference(sets_x))    #more easier way to find difference

difference_x_easysets = sets_x.difference(sets_y)     #easy way to find difference
difference_y_easysets = sets_y.difference(sets_x)     #easy way to find difference
print("Easy difference of sets_x:", difference_x_easysets)
print("Easy difference of sets_y:", difference_y_easysets)
difference_x_sets = sets_x - sets_y       #finding difference
difference_y_sets = sets_y - sets_x      #finding difference
print("Difference of sets_x:", difference_x_sets)
print("Difference of sets_y:", difference_y_sets)      

sets_x = {"apple", "mango"}
sets_y = {"mango", "orange"}
sets_z = {"mango"}
print(sets_x.issubset(sets_y))      #neither of them is subset
print(sets_y.issubset(sets_x))      #neither of them is subset
print(sets_z.issubset(sets_x))      #sets_z is a subset of sets_x
print(sets_z.issubset(sets_y))      #sets_z is a subset of sets_y

sets_x = {1,2,3,4}
sets_y = {4,5,6,7}
sets_z = {8}
print("Is sets_x disjoint with sets_y?", sets_x.isdisjoint(sets_y))      #disjoin() finding not common elements
print("Is sets_y disjoint with sets_x?", sets_y.isdisjoint(sets_x))
print("Is sets_z disjoint with sets_x?", sets_z.isdisjoint(sets_x))      
print("Is sets_z disjoint with sets_y?", sets_z.isdisjoint(sets_y))     


