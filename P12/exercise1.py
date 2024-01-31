'''In computer games, objects are typically approximated by a hitbox and collisions are computed efficiently by checking for intersections between those hitboxes.
Write a Python function number_of_collisions(objects) that returns the number of collisions between each object given in the list objects.

Each object is a dictionary with the following keys: x1, y1, x2, y2, representing the top-left and bottom-right corner of the hitbox. Note that the origin of the coordinates is in the top-left corner.

Hint: it is easier to write a function to check if two rectangles do not intersect than to check if they intersect.
'''

def number_of_collisions(objects):
    collisions =0
    for i,obj in enumerate(objects):
        for j in range(i+1,len(objects)):
            if do_intersect(obj,objects[j]):
                collisions += 1
    return collisions

def do_intersect(a,b):
    return( a["x2"]>=b["x1"]and 
           b["x2"]>=a["x1"] and 
           a["y2"]>=b["y1"]and 
           b["y2"]>=a["y1"])

