from browser import document, window, alert

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(700, 410)
        p.background(0)
        p.rectMode(p.CENTER)
    

    def draw():
        #p.background(0) 
        p.fill(0,255,0,128)
        p.ellipse(p.mouseX,p.mouseY,50,50)

    
    def mousePressed(self):
        p.background(0)
    

    def keyPressed(self):
      if p.key==" ":
        print("Yo yo yo")
    

    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed
      
myp5 = window.p5.new(sketch)
