import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
score = Scoreboard()
car_manager = CarManager()
pl1 = Player()
screen.onkey(pl1.up,"w")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(pl1) <20:
            game_is_on = False
            score.game_over()
            
    
    if pl1.is_at_finish_line():
        pl1.go_to_start()
        score.increase_level()
        car_manager.increase_speed()
    
        

screen.exitonclick()



