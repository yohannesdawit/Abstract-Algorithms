#quickhull.py
#By Steve Setefane

def quickHull(pts):
    n = len(pts)
    p1 = pts[0]
    pn = pts[n - 1]
    dists = [determ(p1, pn, p) for p in pts]
    s = [pts[i] for i in range(len(pts)) if dists[i] > 0]
    s1 = [pts[i] for i in range(len(pts)) if dists[i] < 0]
    du = [i for i in dists if i > 0]
    dl = [i for i in dists if i < 0]
    upper_hull = upperhull(p1, pn, s, du)
    lower_hull = lowerhull(p1, pn, s1, dl)

    return upper_hull + lower_hull


def upperhull(p1, pn, s, dists):
    upper_hull = []
    if not s:
        return [(p1, pn)]
    else:
        pmaxIndex = argmax(dists)
        pmax = s[pmaxIndex]
        dst_left = [determ(p1, pmax, p) for p in s]
        dst_right = [determ(pmax, pn, p) for p in s]
        s1 = [s[i] for i in range(len(s)) if dst_left[i] > 0]
        s2 = [s[i] for i in range(len(s)) if dst_right[i] > 0]
        d1 = [i for i in dst_left if i > 0]
        d2 = [i for i in dst_right if i > 0]
        pts1 = upperhull(p1, pmax, s1, d1)
        pts2 = upperhull(pmax, pn, s2, d2)
        upper_hull += pts1 + pts2

        return upper_hull


def lowerhull(p1, pn, s, dists):
    lower_hull = []
    if not s:
        return [(pn, p1)]
    else:
        pminIndex = argmin(dists)
        pmin = s[pminIndex]
        dst_left = [determ(p1, pmin, p) for p in s]
        dst_right = [determ(pmin, pn, p) for p in s]
        s1 = [s[i] for i in range(len(s)) if dst_left[i] < 0]
        s2 = [s[i] for i in range(len(s)) if dst_right[i] < 0]
        d1 = [i for i in dst_left if i < 0]
        d2 = [i for i in dst_right if i < 0]
        pts1 = lowerhull(p1, pmin, s1, d1)
        pts2 = lowerhull(pmin, pn, s2, d2)
        lower_hull += pts2 + pts1

        return lower_hull


def determ(p0, pn, p3):
    x1, y1 = p0
    x2, y2 = pn
    x3, y3 = p3
    return x1 * y2 + x3 * y1 + x2 * y3 - x3 * y2 - x2 * y1 - x1 * y3


def argmax(lst):
    return max(range(len(lst)), key=lst.__getitem__)


def argmin(lst):
    return min(range(len(lst)), key=lst.__getitem__)
