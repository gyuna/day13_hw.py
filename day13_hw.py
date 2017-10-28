import turtle as t                   # 거북이 함수를 사용.  
import random                        # random 함수를 사용.  

t.bgcolor("green")
t.color("red")
t.pensize(3)
t.shape("triangle")                   
t.speed(0)                           # 거북이의 속도를 가장 빠르게 지정
 
t.up()                             
t.goto(250, 250)                     # 좌표 (250, 250)으로 이동.
t.down()                            
                                   
for x in range(4):                   # 한변의 길이가 500인 사각형을 만듬.
    t.rt(90)                     
    t.fd(500)                   
  
t.up()                                
t.home()                             # 좌표 (0, 0)으로 이동.
t.down()                            

n = random.randint(0, 360)           # 0부터 360중 임의의 수를 n에 저장.  
t.setheading(n)                      # 거북이가 0~360도 중 하나의 각도로 출발~  

while True:                          # True인 경우 계속 반복  
    while -250 < t.xcor() < 250 and  -250 < t.ycor() < 250:  # while 함수로 정해진 범위 안에서 반복.   
        n = t.heading()              # 거북이가 벽에 충돌해 방향을 바꿀 때마다 n각도 방향으로 향하게 함.
        t.forward(1)
                                     

        if -251 < t.xcor() <= -250:  # 왼쪽벽에 충돌할 때 들어오는 각도를 통해 반사각을 저장.  
            if 180 < n < 270:  
                t.setheading(540-n)  
                t.forward(1)  
            elif 90 < n < 180:  
                t.setheading(180-n)  
                t.forward(1)
                
                
        if 250 <= t.xcor() < 251:    # 오른쪽벽에 충돌할 때 들어오는 각도를 통해 반사각을 저장.
            if 270 < n < 360 :  
                t.setheading(540-n)  
                t.forward(1)  
            elif 0 < n < 90:  
                t.setheading(180-n)  
                t.forward(1)
                
        if -251 < t.ycor() <= -250:  # 아랫쪽벽에 충돌할 때 들어오는 각도를 통해 반사각을 저장. 
            if 180 < n < 360:  
                t.setheading(360-n)  
                t.forward(1)
                
        if 250 <= t.ycor() < 251:    # 윗쪽벽에 충돌할 때 들어오는 각도를 통해 반사각을 저장.  
            if 0 < n < 180:  
                t.setheading(360-n)
                t.forward(1)
                
