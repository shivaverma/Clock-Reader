import csv
import cv2 as cv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy.random import randint, rand, choice


def rotateImage(image, angle):
    
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


def get_angle(a, b):
    
    if a>=0:
        hour_angle = 90-np.arctan(b/a)*(180/np.pi)
    else:
        hour_angle = 270-np.arctan(b/a)*(180/np.pi)        
    return hour_angle        


def get_end_point(length, angle):
    
    if angle < 90:
        angle = 90-angle
        a = int(length*np.sin((angle*np.pi/180)))
        b = int(length*np.cos((angle*np.pi/180)))
    elif angle < 180:
        angle = angle-90
        a = -int(length*np.sin((angle*np.pi/180)))
        b = int(length*np.cos((angle*np.pi/180)))
    elif angle < 270:
        angle = 270-angle
        a = -int(length*np.sin((angle*np.pi/180)))
        b = -int(length*np.cos((angle*np.pi/180)))
    else:
        angle = angle-270
        a =  int(length*np.sin((angle*np.pi/180)))
        b = -int(length*np.cos((angle*np.pi/180)))  
    return a, b    


def get_time():
    
    hour = randint(12)
    minute = randint(60)
    
    hour_angle = int(30*hour + minute/2)
    min_angle = minute*6

    return (hour, minute), (hour_angle, min_angle)


def create_clock(window_len=300, clock_radius_min=90):

    window_size = (window_len, window_len, 3)

    clock_pos_min = clock_radius_min
    clock_pos_max = window_len-clock_radius_min
    clock_pos = (randint(clock_pos_min, clock_pos_max), randint(clock_pos_min, clock_pos_max))
    clock_radius_max = min(min(abs(clock_pos[0]-window_len),clock_pos[0]), min(abs(window_len-clock_pos[1]),clock_pos[1]))
    clock_radius = randint(clock_radius_min, clock_radius_max+1)
    clock_color = [rand() for i in range(3)]

    marker_offset = randint(6, 9)
    marker_radius = randint(4, marker_offset-1)
    marker_color = [rand()*.7 for i in range(3)]
    marker_pos = (clock_pos[0], clock_pos[1]-clock_radius+marker_offset)

    time, angle = get_time()
    hour_angle = angle[0]
    min_angle = angle[1]
    
    hour_hand_offset = (marker_offset+20)
    hour_hand_start = clock_pos
    hour_hand_len = randint(clock_radius//2, clock_radius - hour_hand_offset)
    hour_end_a, hour_end_b = get_end_point(hour_hand_len, hour_angle)
    hour_hand_end_x = clock_pos[0]+hour_end_b
    hour_hand_end_y = clock_pos[1]-hour_end_a
    hour_hand_end = (int(hour_hand_end_x), int(hour_hand_end_y))
    hour_hand_color = [rand()*.7 for i in range(3)]
    hour_hand_thickness = randint(5, 7)

    min_hand_start = clock_pos
    min_hand_len = hour_hand_len + randint(15, 20)
    min_end_a, min_end_b = get_end_point(min_hand_len, min_angle)
    min_hand_end_x = clock_pos[0]+min_end_b
    min_hand_end_y = clock_pos[1]-min_end_a
    min_hand_end = (int(min_hand_end_x), int(min_hand_end_y))
    min_hand_color = hour_hand_color
    min_hand_thickness = hour_hand_thickness - randint(2, 4)

    img = np.ones(window_size)*rand()

    img = cv.circle(img, clock_pos, clock_radius, clock_color, -1)      # clock
    img = cv.circle(img, clock_pos, clock_radius, (.2,.2,.2), 2)        # clock boundry
    img = cv.circle(img, marker_pos, marker_radius, marker_color, -1)   # marker

    img = cv.line(img, hour_hand_start, hour_hand_end, hour_hand_color, hour_hand_thickness)  # hour hand
    img = cv.line(img, min_hand_start, min_hand_end, min_hand_color, min_hand_thickness)      # min hand
    img = cv.circle(img, clock_pos, 5, (0,0,0), -1)                                           # center
        
    return img, time


def generate_data(sample=2, img_dir='images/'):
    
    hour = []
    minute = []
    for i in range(sample):
        img, time = create_clock()
        plt.imsave(img_dir+str(i)+'.jpg', img)
        hour.append(time[0])
        minute.append(time[1])
    label = {'hour':hour, 'minute':minute}
    label = pd.DataFrame(label)
    label.to_csv('label.csv', index=False)
    
    
if __name__ == '__main__':
    
    generate_data(sample=50000)