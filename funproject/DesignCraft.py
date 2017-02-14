#Sujita Shah
#space.py
# This program is about sending Apollo from the earth and sending aliens's satelite from aliens's planet.
#input=10 clicks to display the stars and 1 click for the Indian flag
from graphics import *
def main():

##################################################
##        The weird text such as すじた          ##
##        is Japanese Hiragana being used       ##
##        as alien text                         ##
##################################################


    
    win = GraphWin("Apollo vs. すじた to the Moon", 500, 500)
    win.setBackground("black")

#Earth
    
    earth = Circle(Point(224,400), 56)
    earth.setFill("blue")
    earth.setOutline("green")
    earth.draw(win)

#Spudnik (Russian satalight)
   
    sline1= Line(Point(150,380), Point(130, 400))
    sline1.setFill("green")
    sline1.draw(win)
    sline2 = Line(Point(150, 380), Point(170, 400))
    sline2.setFill("green")
    sline2.draw(win)
    spudnik=Circle(Point(150, 380),10)
    spudnik.setFill("grey")
    spudnik.draw(win)

#Alien Planet

    aliensplanet=Oval(Point(30,200),Point(60,300))
    aliensplanet.setFill("red")
    aliensplanet.setOutline("black")
    aliensplanet.draw(win)
    aliensplanet1=Oval(Point(10,280),Point(80,220))
    aliensplanet1.setFill("red")
    aliensplanet1.setOutline("black")
    aliensplanet1.draw(win)
    aliensplanetn = Text(Point(45, 250), "げうつん")
    aliensplanetn.setTextColor("cyan")
    aliensplanetn.draw(win)
    alient = Text(Point(100,93), "すじた")
    alient.setTextColor("green")
    alient.draw(win)

#Apollo Spaceship

    Apollo=Polygon([Point(275, 255),Point(240,240),Point(275,160),Point(305,140),Point(310, 170)])
    Apollo.setFill("white")
    Apollo.setOutline("orange")
    Apollo.draw(win)
    Apolloline = Line(Point(258, 248), Point(305, 140))
    Apolloline.setFill("orange")
    Apolloline.draw(win)
    line1=Line(Point(250,236),Point(210,270))
    line1.setFill("orange")
    line1.draw(win)
    line2=Line(Point(258,248),Point(235,285))
    line2.setFill("orange")
    line2.draw(win)
    line3=Line(Point(270,250),Point(265,295))
    line3.setFill("orange")
    line3.draw(win)
    text=Text(Point(279,190),"Apollo")
    text.setTextColor("orange")
    text.draw(win)

#Moon

    moon=Circle(Point(380,45),38)
    moon.setFill("white")
    moon.setOutline("black")
    moon.draw(win)


#Alien Space Craft
    
    bar = Rectangle(Point(95,50),Point(105,70))
    bar.setFill("Blue")
    bar.setOutline("Blue")
    bar.draw(win)

    top = Circle(Point(100, 50), 5)
    top.setFill("yellow")
    top.setOutline("yellow")
    top.draw(win)

    fo = Oval(Point (85, 70), Point(115, 80))
    fo.setFill("blue")
    fo.setOutline("blue")
    fo.draw(win)
    so = Oval(Point (75, 80), Point(125, 90))
    so.setFill("blue")
    so.setOutline("blue")
    so.draw(win)

    bottom = Rectangle(Point(70, 95), Point(135, 115))
    bottom.setFill("yellow")
    bottom.setOutline("yellow")
    bottom.draw(win)

    end = Polygon([Point(135, 100),Point(135, 90),Point(155,90),Point(165,95),Point(155, 100)])
    end.setFill("yellow")
    end.setOutline("yellow")
    end.draw(win)
    
    to = Oval(Point (65, 85), Point(135, 100))
    to.setFill("blue")
    to.setOutline("blue")
    to.draw(win)
    alient = Text(Point(100,93), "すじた")
    alient.setTextColor("green")
    alient.draw(win)


##########################################################################
##                          Stars                                       ##
##    (A while loop would have been better but I was trying to clone  ##  
##     them orignaly and then the idea just hit me to do this)          ##
##########################################################################

    print("Click 10 places to create 10 stars")
    p = win.getMouse()
    
    
    star1 = Polygon(Point(p.getX(),p.getY()), Point(p.getX()-10,p.getY()+10), Point(p.getX()+10,p.getY()+10))
    star1.setFill("yellow")
    star1.setOutline("yellow")
    star1.draw(win)
    star2 = Polygon(Point(p.getX(),p.getY()+15), Point(p.getX()-10,p.getY()+5), Point(p.getX()+10,p.getY()+5))
    star2.setFill("yellow")
    star2.setOutline("yellow")
    star2.draw(win)
    

    p = win.getMouse()

    star12 = Polygon(Point(p.getX(),p.getY()), Point(p.getX()-10,p.getY()+10), Point(p.getX()+10,p.getY()+10))
    star12.setFill("yellow")
    star12.setOutline("yellow")
    star12.draw(win)
    star22 = Polygon(Point(p.getX(),p.getY()+15), Point(p.getX()-10,p.getY()+5), Point(p.getX()+10,p.getY()+5))
    star22.setFill("yellow")
    star22.setOutline("yellow")
    star22.draw(win)

    p = win.getMouse()

    star13 = Polygon(Point(p.getX(),p.getY()), Point(p.getX()-10,p.getY()+10), Point(p.getX()+10,p.getY()+10))
    star13.setFill("yellow")
    star13.setOutline("yellow")
    star13.draw(win)
    star23 = Polygon(Point(p.getX(),p.getY()+15), Point(p.getX()-10,p.getY()+5), Point(p.getX()+10,p.getY()+5))
    star23.setFill("yellow")
    star23.setOutline("yellow")
    star23.draw(win)

    p = win.getMouse()

    star14 = Polygon(Point(p.getX(),p.getY()), Point(p.getX()-10,p.getY()+10), Point(p.getX()+10,p.getY()+10))
    star14.setFill("yellow")
    star14.setOutline("yellow")
    star14.draw(win)
    star24 = Polygon(Point(p.getX(),p.getY()+15), Point(p.getX()-10,p.getY()+5), Point(p.getX()+10,p.getY()+5))
    star24.setFill("yellow")
    star24.setOutline("yellow")
    star24.draw(win)

    p = win.getMouse()

    star15 = Polygon(Point(p.getX(),p.getY()), Point(p.getX()-10,p.getY()+10), Point(p.getX()+10,p.getY()+10))
    star15.setFill("yellow")
    star15.setOutline("yellow")
    star15.draw(win)
    star25 = Polygon(Point(p.getX(),p.getY()+15), Point(p.getX()-10,p.getY()+5), Point(p.getX()+10,p.getY()+5))
    star25.setFill("yellow")
    star25.setOutline("yellow")
    star25.draw(win)

    p = win.getMouse()

    star16 = Polygon(Point(p.getX(),p.getY()), Point(p.getX()-10,p.getY()+10), Point(p.getX()+10,p.getY()+10))
    star16.setFill("yellow")
    star16.setOutline("yellow")
    star16.draw(win)
    star26 = Polygon(Point(p.getX(),p.getY()+15), Point(p.getX()-10,p.getY()+5), Point(p.getX()+10,p.getY()+5))
    star26.setFill("yellow")
    star26.setOutline("yellow")
    star26.draw(win)

    p = win.getMouse()

    star17 = Polygon(Point(p.getX(),p.getY()), Point(p.getX()-10,p.getY()+10), Point(p.getX()+10,p.getY()+10))
    star17.setFill("yellow")
    star17.setOutline("yellow")
    star17.draw(win)
    star27 = Polygon(Point(p.getX(),p.getY()+15), Point(p.getX()-10,p.getY()+5), Point(p.getX()+10,p.getY()+5))
    star27.setFill("yellow")
    star27.setOutline("yellow")
    star27.draw(win)

    p = win.getMouse()

    star18 = Polygon(Point(p.getX(),p.getY()), Point(p.getX()-10,p.getY()+10), Point(p.getX()+10,p.getY()+10))
    star18.setFill("yellow")
    star18.setOutline("yellow")
    star18.draw(win)
    star28 = Polygon(Point(p.getX(),p.getY()+15), Point(p.getX()-10,p.getY()+5), Point(p.getX()+10,p.getY()+5))
    star28.setFill("yellow")
    star28.setOutline("yellow")
    star28.draw(win)

    p = win.getMouse()
    
    star19 = Polygon(Point(p.getX(),p.getY()), Point(p.getX()-10,p.getY()+10), Point(p.getX()+10,p.getY()+10))
    star19.setFill("yellow")
    star19.setOutline("yellow")
    star19.draw(win)
    star29 = Polygon(Point(p.getX(),p.getY()+15), Point(p.getX()-10,p.getY()+5), Point(p.getX()+10,p.getY()+5))
    star29.setFill("yellow")
    star29.setOutline("yellow")
    star29.draw(win)

    p = win.getMouse()
    
    star10 = Polygon(Point(p.getX(),p.getY()), Point(p.getX()-10,p.getY()+10), Point(p.getX()+10,p.getY()+10))
    star10.setFill("yellow")
    star10.setOutline("yellow")
    star10.draw(win)
    star20 = Polygon(Point(p.getX(),p.getY()+15), Point(p.getX()-10,p.getY()+5), Point(p.getX()+10,p.getY()+5))
    star20.setFill("yellow")
    star20.setOutline("yellow")
    star20.draw(win)
    
    print("Click the Moon to plot the Indian flag")
    p=win.getMouse()

    #Indian flag
    flag = Rectangle(Point(370,40),Point(385,50))
    flag.setFill("green")
    flag.setOutline("black")
    flag.draw(win)
    flag1=Rectangle(Point(370,40),Point(385,43))
    flag1.setFill("orange")
    flag1.setOutline("black")
    flag1.draw(win)
    flag2=Rectangle(Point(370,43),Point(385,47))
    flag2.setFill("white")
    flag2.setOutline("black")
    flag2.draw(win)
    flagpole=Line(Point(370,40),Point(370,57))
    flagpole.setFill("black")
    flagpole.draw(win)
    chakra=Circle(Point(377,45),2)
    chakra.setFill("blue")
    chakra.draw(win)
    
    print("Click window to close")

    win.getMouse()
    #print("x ", win.getX(), "y ",win.getY())
    win.close()
main()
