def setup():
    size(400, 400) # Set the size of canvas
    noStroke()

def drawObject(x, y, s):
    push()
    translate(x, y)
    scale(s)
    fill(0) # Fill in with black color
    rect(150, 250, 100, 20) # handle
    rect(192, 100, 20, 200) # blade
    triangle(192, 100, 212, 100, 202, 70) # tip
    triangle(192, 150, 192, 200, 172, 175) # left tip ornament
    triangle(210, 150, 210, 200, 230, 175) # right tip ornament
    pop()

def draw():
    rows = int(height / 40) # calculates amount of rows
    cols = int(width / 40) # calculates amount of columns
    for i in range(rows): # counts rows
        for j in range(cols): # counts columns
            x_cell = j * 40 # 40 x cells
            y_cell = i * 40 # 40 y cells
            drawObject(x_cell, y_cell, 0.4) # draws in a 40x40 grid
