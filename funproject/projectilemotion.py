from visual import*
from visual.graph import*
funct=gcurve(color=color.cyan)
#ball friction less
theta=(45*pi)/180
ball1=sphere(pos=(-5,0,0),radius=0.035,color=color.red,make_trail=true)
ball1.m=0.155# mass in kg
ball1.s=(100*1609.34)/(60*60)
ball1.v=vector(ball1.s*cos(theta),ball1.s*sin(theta),0)
g=9.8
ball1.p=ball1.m*ball1.v
Ue=ball1.m*9.8*ball1.pos.y
Ke=(1/2)*ball1.m*(mag(ball1.v))*(mag(ball1.v))
E=Ue+Ke
ball1.trail=curve(color=ball1.color)
#ball with friction
ball2=sphere(pos=vector(-5,0,0),radius=0.035,color=color.blue,make_trail=true)
ball2.m=0.155# mass in kg
C=0.35
density=1.3
ball2.s=(100*1609.34)/(60*60)
ball2.v=vector(ball2.s*cos(theta),ball2.s*sin(theta),0)
ball2.trail=curve(color=ball2.color)
g=9.8
ball2.p=ball2.m*ball2.v
Ue=ball2.m*9.8*ball2.pos.y
Ke=(1/2)*ball2.m*(mag(ball2.v))*(mag(ball2.v))
E=Ue+Ke
rangep= (mag(ball2.v))*(mag(ball2.v))*sin(2*theta)/(2*g)
funct1=gcurve(color=color.red)
funct2=gcurve(color=color.yellow)
t=0
dt=0.001
while(ball2.pos.y>=0):
    rate(1000)
    fe=vector(0,-ball2.m*g,0)
    ball1.p=ball1.p+fe*dt
    ball1.v=ball1.p/ball1.m
    ball1.pos=ball1.pos+(ball1.p/ball1.m)*dt
    ball1.trail.append(pos=ball1.pos)
    Ue=ball1.m*9.8*ball1.pos.y
    Ke=(1/2)*ball2.m*(mag(ball1.v))*(mag(ball1.v))
    E1=Ue+Ke
    #ball2
    ff=(-1/2)*C*density*pi*ball2.radius*ball2.radius*(mag(ball2.v))*(mag(ball2.v))*norm(ball2.v)
    ft=fe+ff
    ball2.p=ball2.p+ft*dt
    ball2.v=ball2.p/ball2.m
    ball2.pos=ball2.pos+(ball2.p/ball2.m)*dt
    ball2.trail.append(pos=ball2.pos)
    Ue2=ball2.m*9.8*ball2.pos.y
    Ke2=(1/2)*ball2.m*(mag(ball2.v))*(mag(ball2.v))
    E2=Ue2+Ke2
    t=t+dt
    funct1.plot(pos=(t,E1))
    funct2.plot(pos=(t,E2))
print("the range is=",rangep)
print("total energy=",E1)
print("total energy=",E2)
print("the velocity=",ball1.v)
print("the velocity=",ball2.v)

    





