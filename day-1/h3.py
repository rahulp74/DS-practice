b = []
f = []
cur = "Home"

def visit(place):
    global cur
    b.append(cur)
    cur = place
    f.clear()
    print("cur Location:", cur)

def back():
    global cur
    if not b:
        print("No Previous Location")
    else:
        f.append(cur)
        cur = b.pop()
        print("cur Location:", cur)

def forward():
    global cur
    if not f:
        print("No Forward Location")
    else:
        b.append(cur)
        cur = f.pop()
        print("cur Location:", cur)

visit("Mall")
visit("Hospital")
visit("Airport")

back()
back()
forward()