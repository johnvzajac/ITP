def setup():
    size(400, 400) # Set the size of canvas
    noStroke()

def draw():
    fill(0) # Fill in with black color
    rect(150, 250, 100, 20) # handle
    rect(192, 100, 20, 200) # blade
    triangle(192, 100, 212, 100, 202, 70) # tip
    triangle(192, 150, 192, 200, 172, 175) # left tip ornament
    triangle(210, 150, 210, 200, 230, 175) # right tip ornament
