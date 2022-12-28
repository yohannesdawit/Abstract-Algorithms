# quickhull.py
# Quickhull Algorithm
# By: Shahzeb Jadoon


def quick_hull(ordered_points):


    lst_size = len(ordered_points)

    if lst_size > 2:
        p_first = ordered_points[0]
        p_last = ordered_points[-1]

        determ_lst = [determ(p_first, p_last, p) for p in ordered_points]
        left_points = [(ordered_points[i], determ_lst[i]) for i in range(lst_size) if determ_lst[i] > 0]
        right_points = [(ordered_points[i], determ_lst[i]) for i in range(lst_size) if determ_lst[i] < 0]

        upper_hull = half_hull(p_first, p_last, left_points)
        ower_hull = half_hull(p_first, p_last, right_points)

        lower_points = reverse(lower_points)

        convex_hull_lst = [p_first] + upper_points + [p_last] + lower_points

        return convex_hull_lst

    else:
        return ordered_points

def half_hull(p1, pn, s, determ):
    
    size = len(s)
    halfr = []
    if size == 0:
        return [(p1, pn)]
    if size >= 1:
        pmax_determ = 0
        pmax = p1
       
        for p in s:
            determ_item = abs(determ(p1, pn, p))
            if determ_item > pmax_determ:
                pmax_determ = determ_item
                pmax = p
                
        s1 = [p for p in s if determinant(p1, pmax, p) > 0]
        s2 = [p for p in s if determinant(pmax, pn, p) > 0]

        determinant_lst1 = {p: determ(p1, pmax, p) for p in s1}
        determinant_lst2 = {p: determ(pmax, pn, p) for p in s2}
        
        half_up = halfhull(p1, pmax, s1, determinant_lst1)
        half_down = halfhull(pmax, pn, s2, determinant_lst2)

        return half_up + half_down



def determ(p1, p2, p3):
  
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return (x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3)




def main():
    """ Allows the user to visualize a convexx hull based on random points. The user
        can choose the number of points.
        post: displays the points on a graphical window as circles, with line segments
              that connect the points that form the convex hull. 
    """
    
    print("This program allows the user to visualize a convex hull of random point")
    print("The user can choose the number of points from which to draw the convex hull,")
    n = int(input("thus enter the number of points: "))
    
    unordered_points = []
    width = 800
    height = 600

    for i in range(n):
        unordered_points.append((randrange(width*0.1, width*0.9), randrange(height*0.1, height*0.9)))
    
    convex_hull_lst = quick_hull(unordered_points)

    win = GraphWin("Convex Hull Implementation", width, height, autoflush=False)
    win.setCoords(0, 0, width, height)
    
    for point in unordered_points:
        Circle(Point(point[0], point[1]), 1.5).draw(win)

    for i in range(len(convex_hull_lst) - 1):
        Line(Point(convex_hull_lst[i][0], convex_hull_lst[i][1]), Point(convex_hull_lst[i + 1][0], convex_hull_lst[i + 1][1])).draw(win)

    Line(Point(convex_hull_lst[0][0], convex_hull_lst[0][1]), Point(convex_hull_lst[-1][0], convex_hull_lst[-1][1])).draw(win)

    message = Text(Point(width/2, height*0.95), "Click anywhere to quit.")
    message.draw(win)
    win.getMouse()
    win.close()

if __name__ == "__main__":
    from graphics import GraphWin, Point, Line, Text, Circle
    from random import randrange
    
    main()
