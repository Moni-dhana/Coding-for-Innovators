import time
# Constants for light durations (in seconds)
GREEN_LIGHT_DURATION = 30
YELLOW_LIGHT_DURATION = 5
RED_LIGHT_DURATION = 5
WALK_SIGNAL_DURATION = 20
# Simulate the state of the pedestrian button
pedestrian_button_pressed = False
def turn_on_green_light():
    print("Green light ON")
def turn_on_yellow_light():
    print("Yellow light ON")
def turn_on_red_light():
    print("Red light ON")
def turn_on_walk_signal():
    print("Walk signal ON")
def turn_off_walk_signal():
    print("Walk signal OFF")
def pedestrian_button_press():
    global pedestrian_button_pressed
    pedestrian_button_pressed = True

# Main loop
while True:
    # Vehicle light sequence
    turn_on_green_light()
    time.sleep(GREEN_LIGHT_DURATION)
    turn_on_yellow_light()
    time.sleep(YELLOW_LIGHT_DURATION)
    turn_on_red_light()
    time.sleep(RED_LIGHT_DURATION)
    
    # Check pedestrian button
    if pedestrian_button_pressed:
        turn_on_walk_signal()
        time.sleep(WALK_SIGNAL_DURATION)
        turn_off_walk_signal()
        pedestrian_button_pressed = False  # Reset the button state
    
    # Red light continues for RED_LIGHT_DURATION
    time.sleep(RED_LIGHT_DURATION)