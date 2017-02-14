from visual import *
from visual.graph import*
# sending a space craft from the earth to the moon
# Sujita Shah
earth=sphere(pos=(0,0,0),radius=6.4e6,color=color.blue)
earth.mass=6e24
moon=sphere(pos=(40e7,0,0),radius=1.75e6,color=color.white)
moon.mass=7e22
craft = cone(pos=vector(6.45e6,0,0),axis=(1.70e7,0,0),radius=1.25e7, color=color.red)
craft.mass=173
craft.velocity=vector(1.13e4,0,0)
craft.p=craft.mass*craft.velocity
earth.trail=curve()
moon.r=1.75e6
earth.r=6.4e6
We=0
Wm=0
k1=(1/2)*craft.mass*mag(craft.velocity)**2
G=6.7e-11
Ue=-G*earth.mass*craft.mass/mag(craft.pos-earth.pos)
Um=-G*moon.mass*craft.mass/mag(craft.pos-moon.pos)
Et=k1+Ue+Um
funct=gcurve(color=color.cyan)
funct2=gcurve(color=color.blue)
funct3=gcurve(color=color.red)
t=0
dt=6
while(craft.pos.x<=(moon.pos.x-moon.r)):
    rate(1000)
    r1=craft.pos-earth.pos
    r2=craft.pos-moon.pos
    fe=-G*earth.mass*craft.mass*norm(r1)/mag(r1)**2
    fm=-G*moon.mass*craft.mass*norm(r2)/mag(r2)**2
    ft=fe+fm
    craft.p=craft.p+ft*dt
    craft.pos=craft.pos+(craft.p/craft.mass)*dt
    dx=(craft.p/craft.mass)*dt
    We=We-mag(fe*mag(dx))
    Wm=Wm+mag(fm*mag(dx))
    Wt=We+Wm
    k2=(1/2)*craft.mass*(mag(craft.p/craft.mass)**2)
    Ue2=-G*earth.mass*craft.mass/mag(r1)
    Um2=-G*moon.mass*craft.mass/mag(r2)
    Et=k2+Ue2+Um2
    earth.trail.append(pos=craft.pos)
    funct.plot(pos=(craft.pos.x,k2))
    funct2.plot(pos=(craft.pos.x,Ue2+Um2))
    funct3.plot(pos=(craft.pos.x,Et))

print("impact velocity=",craft.p/craft.mass)
print("total work=",Wt)
print("change in energy=",k2-k1)


# a) the delta t should be 6
#b) the minium speed is 1.13e4 to launch the craft other vise it will come back in the
#gravitational pull of the earth.
#c) it will take approximately 10 days to reach on the moon
#d)the impact velocity is <3116.41,0,0>

  
    
 
    
    
    




    
    
    


