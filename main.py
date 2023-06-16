import time
import keyboard
import spyroSCREAM
#from spyroAlarm import alarm

#variables
danger_val = 0
danger_level = 0
detFire = 0
detSmoke = 0
detHumans = 0


while True:
    
    #check if fire
    if keyboard.is_pressed(" "):
        detFire += 1
    if keyboard.is_pressed("s"):
        detSmoke += 1     

    #danger value progress 
    if detFire > 0 and danger_val < 100:
        danger_val += 10
    elif detFire == 0 and (danger_val-10) >= 0:
        danger_val -= 10
               
    #danger level update
    if danger_val >= 100:
        danger_level = 4
    elif danger_val >= 75:
        danger_level = 3
    elif danger_val >= 50:
        danger_level = 2
    elif danger_val >= 25:
        danger_level = 1
    else:   
        danger_level = 0

    print(f"{detFire} fires! {detSmoke} smoke!")
    print(f"Danger value at: {danger_val}%   Danger level:{danger_level}")
    
    detFire = 0
    detSmoke = 0 

    if danger_val == 100:
        spyroSCREAM.siren()
        #alarm()

    time.sleep(1)
    
