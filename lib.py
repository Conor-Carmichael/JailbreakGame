

# Helper methods for protagonist_caught:
# code from: https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/
# solution to if point in triangle
from math import sqrt

def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def area(x1, y1, x2, y2, x3, y3): 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0) 

def is_inside_triangle(sight_tr, player, precalc_area=None): 
    # print('Passed: ', sight_tr)
    a, b, c = sight_tr
    x, y = player
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    # Calculate area of triangle ABC 
    A = area(x1, y1, x2, y2, x3, y3) if precalc_area==None else precalc_area
    # Calculate area of triangle PBC  
    A1 = area(x, y, x2, y2, x3, y3)         
    # Calculate area of triangle PAC  
    A2 = area(x1, y1, x, y, x3, y3) 
    # Calculate area of triangle PAB  
    A3 = area(x1, y1, x2, y2, x, y) 
    # Check if sum of A1, A2 and A3  
    # is same as A 
    if(A == A1 + A2 + A3): 
        return True, None # No need for precalc area if caught, 0 is fine
    else: 
        return (False, A) #to store the sight cone triangle area and pass as precalc area


def get_corner_coords(xy, size):
    x, y = xy
    width, length = size
    return [(x,y), (x+width,y), (x, y+length), (x+width, y+length)]

def encode_point(xy):
    return str(xy[0])+str(xy[1])
