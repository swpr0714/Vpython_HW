from vpython import *
v,a,t,dt,n,h = 0, -9.8, 0, 0.001, 0,10

scene = canvas(width=1920, height=1080, x=0, y=0, center=vec(0,0,0))
floor = box (size=vec(10,0.5,10),pos=vec(0,-0.25,0),color=color.cyan)
ball = sphere (pos=vec(0,h,0),radius=0.2,color=color.red)

while(n<=3):
    rate(1000)
    ball.pos.y+=v*dt
    v+=a*dt
    t+=dt
    if (ball.pos.y<=0.2):
        v=-0.9*v
        n+=1
print(t)