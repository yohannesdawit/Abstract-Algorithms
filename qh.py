#  Quickhull.py
#  By Yohannes Dawit


from graphics import *
from random import randrange

def quick_hull(points):
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

        hull1 = half_hull(p_first, p_last, s1, determinants_s1)
        hull2 = half_hull(p_last, p_first, s2, determinants_s2)
        convex_hull = hull1 + hull2
        return convex_hull

    else:
        return points

def half_hull(p1, pn, s, determinants):
    size = len(s)
    hull = []
    if size == 0:
        return [(p1, pn)]
    if size >= 1:
        pmax_d = 0
        pmax = p1
       
        for p in s:
            d_determ = abs(determinant(p1, pn, p))
            if d_determ > pmax_d:
                pmax_d = d_determ
                pmax = p

        s1 = [p for p in s if determinant(p1, pmax, p) > 0]
        s2 = [p for p in s if determinant(pmax, pn, p) > 0]

        d1 = {p: determinant(p1, pmax, p) for p in s1}
        d2 = {p: determinant(pmax, pn, p) for p in s2}
        
        half1 = half_hull(p1, pmax, s1, d1)
        half2 = half_hull(pmax, pn, s2, d2)
        
        return half1 + half2
        
def determinant(p1, p2, p3):
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return (x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3)

def main():

    print("This program allows the user to visualize a convex hull of random point")
    print("The user can choose the number of points from which to draw the convex hull,")
    n = int(input("Please enter the number of points: "))

    width = 800
    height = 800
    win = GraphWin("Quick Hull Zelle Graphics", width, height)
    win.setCoords(0, 0, width, height)
    
    points = [(randrange(1,800), randrange(1,800)) for i in range(n)]

    for point in points:
        dot = Circle(Point(point[0], point[1]), 1.5)
        dot.draw(win)

    lines = quick_hull(points)
    for line in lines:
        p1 = Point(line[0][0], line[0][1])
        p2 = Point(line[1][0], line[1][1])
        p1p2 = Line(p1,p2)
        p1p2.draw(win)

    message = Text(Point(width/2, height*0.95), "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
