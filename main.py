import numpy as np
import colorsys
import random
import time
import cv2

from sorts import sorting

def get_color(hue):
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    R, G, B = int(255 * r), int(255 * g), int(255 * b)
    return R, G, B


def get_frame(arr, upscale): # The upscale factor is how large we want to upscale the array
    maxNum = max(lst) # Get the highest number
    length = len(lst) # Get the length of the list

    arr = np.zeros( # Create a 3d array
        (maxNum*upscale[0]+1, length*upscale[1], 3), # Set the array size
        "uint8") # Set the datatype

    indxX = 0
    for i in lst: # Go over the list and draw the lines
        y = i * upscale[0] * -1 # Calculate the y height

        if y == 0: # Make sure we are in the minus so it wraps correctly
            y = -1

        if i != 0: # To avoid ZeroDivisionError
            hue = (i - maxNum)/(maxNum) * -1 # Get the hue
        else:
            hue = 0

        r,g,b = get_color(hue) # Get the rbg values

        arr[y:-1, indxX:indxX + upscale[1]] = [r,g,b] # Draw the rectangles
        indxX += upscale[1] # Increase the x index amount

    return arr

lst = [i for i in range(500)] # Genarate the list

arr = get_frame(lst, (8,16)) # Get the first shuffled frame

cv2.namedWindow("Window") # create the window
cv2.imshow("Window", arr) # Show the array

sorter = sorting()

while True:
    for i in sorter.shuffle(lst): # Shuffle the list
        arr = get_frame(i, (1,3)) # Get the next frame

        cv2.putText(arr,'Shuffeling',
            (10,30), # Bottom Left Corner Of Text
            cv2.FONT_HERSHEY_SIMPLEX,  # Font
            .75, # Font scale
            (255,255,255), # Font color
            1) # Line type

        cv2.imshow("Window", arr) # Show the frame

        key = cv2.waitKey(5)
        if key == 27: # exit on ESC
            break

    start = time.time() # Start the timer

    for i, ifs in sorter.selection(lst): # Sort the list
        arr = get_frame(i, (1,3)) # Get the next frame

        cv2.putText(arr,f'Selection Sort - {time.time() - start:.2f}s - {ifs} Checks',
            (10,30), # Bottom Left Corner Of Text
            cv2.FONT_HERSHEY_SIMPLEX,  # Font
            .75, # Font scale
            (255,255,255), # Font color
            1) # Line type


        cv2.imshow("Window", arr) # Show the frame

        key = cv2.waitKey(1)
        if key == 27: # exit on ESC
            break

    for i in sorter.shuffle(lst): # Shuffle the list
        arr = get_frame(i, (1,3)) # Get the next frame

        cv2.putText(arr,'Shuffleing',
            (10,30), # Bottom Left Corner Of Text
            cv2.FONT_HERSHEY_SIMPLEX,  # Font
            .75, # Font scale
            (255,255,255), # Font color
            1) # Line type

        cv2.imshow("Window", arr) # Show the frame

        key = cv2.waitKey(5)
        if key == 27: # exit on ESC
            break

    start = time.time() # Start the timer

    for i, ifs in sorter.insert(lst): # Sort the list
        arr = get_frame(i, (1,3)) # Get the next frame

        cv2.putText(arr,f'Insertion Sort - {time.time() - start:.2f}s - {ifs} Checks',
            (10,30), # Bottom Left Corner Of Text
            cv2.FONT_HERSHEY_SIMPLEX,  # Font
            .75, # Font scale
            (255,255,255), # Font color
            1) # Line type

        cv2.imshow("Window", arr) # Show the frame

        key = cv2.waitKey(1)
        if key == 27: # exit on ESC
            break

    for i in sorter.shuffle(lst): # Shuffle the list
        arr = get_frame(i, (1,3)) # Get the next frame

        cv2.putText(arr,'Shuffleing',
            (10,30), # Bottom Left Corner Of Text
            cv2.FONT_HERSHEY_SIMPLEX,  # Font
            .75, # Font scale
            (255,255,255), # Font color
            1) # Line type

        cv2.imshow("Window", arr) # Show the frame

        key = cv2.waitKey(5)
        if key == 27: # exit on ESC
            break

    start = time.time() # Start the timer

    for i, ifs in sorter.bubble(lst): # Sort the list
        arr = get_frame(i, (1,3)) # Get the next frame

        cv2.putText(arr,f'Bubble Sort - {time.time() - start:.2f}s - {ifs} Checks',
            (10,30), # Bottom Left Corner Of Text
            cv2.FONT_HERSHEY_SIMPLEX,  # Font
            .75, # Font scale
            (255,255,255), # Font color
            1) # Line type

        cv2.imshow("Window", arr) # Show the frame

        key = cv2.waitKey(1)
        if key == 27: # exit on ESC
            break

while True:
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("Window") # close the window
