#quickhull.py
#By: Isaac Nguyen
#This program implements the quickhull algorithm and graphs it.
'''Input: a list of ordered pairs representing the points.
Output: a list of segments (pairs of points), that describe the convex hull polygon
(connecting the segments in order gives the hull polygon).
'''

#include driver program using zellegraphics
#generate random set of points
#compute convex hull
#show results graphically, plot points and draw convex polygon

from graphics import *
from random import randrange

def quickhull(points):
    '''s1 {p when p is left of p1pn} , s2 {p when p is right of p1pn}
'''
    lst_size = len(points)
    if lst_size > 2:
        p_first = min(points)
        p_last = max(points)

        s1 = [p for p in points if determinant(p_first, p_last, p) > 0]
        s2 = [p for p in points if determinant(p_first, p_last, p) < 0]
        determinants_s1 = {p: determinant(p_first, p_last, p) for p in s1}
        determinants_s2 = {p: determinant(p_first, p_last, p) for p in s2}

        hull1 = halfhull(p_first, p_last, s1, determinants_s1)
        hull2 = halfhull(p_last, p_first, s2, determinants_s2)
        convex_hull = hull1 + hull2
        return convex_hull

    else:
        return points

def halfhull(p1, pn, s, determinants):
    s_size = len(s)
    halfl = []
    if s_size == 0:
        return [(p1, pn)]
    if s_size >= 1:
        pmax_determinants_so_far = 0
        pmax = p1
       
        for p in s:
            determ = abs(determinant(p1, pn, p))
            if determ > pmax_determinants_so_far:
                pmax_determinants_so_far = determ
                pmax = p
        #return p

        s1 = [p for p in s if determinant(p1, pmax, p) > 0]
        s2 = [p for p in s if determinant(pmax, pn, p) > 0]

        determinant_lst1 = {p: determinant(p1, pmax, p) for p in s1}
        determinant_lst2 = {p: determinant(pmax, pn, p) for p in s2}
        
        half1 = halfhull(p1, pmax, s1, determinant_lst1)
        half2 = halfhull(pmax, pn, s2, determinant_lst2)

        '''half1.append(pmax)
        half1.extend(half2)'''
        
        return half1 + half2
        
def determinant(p1, p2, p3):
    '''takes 3 tuples and returns the determinant of the 3 points (p1, p2, p3)
'''
    '''x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]'''
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    
    return (x1*y2) + (x3*y1) + (x2*y3) - (x3*y2) - (x2*y1) - (x1*y3)

def main():
    #qh = quickhull([(0,0),(1,1),(3,1),(4,5),(5,3),(6,-6),(7,-1),(8,-3),(9,-4),(10,6),(11,3)])
    #qh = quickhull([(0,0),(2,3),(3,-8),(4,-6),(5,-2),(6,3),(7,11),(10,2)])
    #print("Quick Hull: ", qh)
    print("This program visualizes a convex hull of random points in zellegraphics using quickhull algorithm.")
    n = int(input("Choose a number of points to generate to draw the convex hull: "))

    width = 800
    height = 800
    win = GraphWin("Quick Hull Zelle Graphics", width, height)
    win.setCoords(0, 0, width, height)
    
    points = [(randrange(1,800), randrange(1,800)) for i in range(n)]

    for point in points:
        dot = Circle(Point(point[0], point[1]), 5)
        dot.setFill("lightblue")
        dot.setOutline("red")
        dot.draw(win)

    lines = quickhull(points)
    for line in lines:
        p1 = Point(line[0][0], line[0][1])
        p2 = Point(line[1][0], line[1][1])
        p1p2 = Line(p1,p2)
        p1p2.setFill("blue1")
        p1p2.draw(win)

    message = Text(Point(width/2, height*0.98), "Click anywhere in the window to quit.")
    message.setStyle("bold")
    message.setTextColor("red")
    name = Text(Point(width/2, height*0.95), "By: Isaac Nguyen")
    name.setStyle("italic")
    name.setTextColor("red")
    message.draw(win)
    name.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
