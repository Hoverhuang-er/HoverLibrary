import cv2
import cv2.cv as cv
import numpy as np
import time


def load_image(path):
    """Read image"""
    img = cv2.imread(path, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, gray


def init_camera():
    camera_id = 0
    camera = cv2.VideoCapture(camera_id)
    return camera


def take_picture(camera):
    retval, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, gray


def release_camera(camera):
    del(camera)


def detect_circle(gray):
    """Find circles on the given image"""
    # Reduce the noise to avoid false circle detection
    gray_blured = cv2.medianBlur(gray, 27)

    # Apply the Hough transform to find the circles
    circles = cv2.HoughCircles(gray_blured, cv.CV_HOUGH_GRADIENT,
    1, 20, param1 = 50, param2 = 30, minRadius = 2, maxRadius = 0) #50 30

    if (circles == None):
        return None

    # Round to integers
    circles = np.uint16(np.around(circles))

    ball = circles[0][0]
    return ball


def detect_color(image, ball):
    """Recognize the color of the detected ball"""
    # Crop the ball region for color detection
    # [y1:y2, x1:x2], x1y1 - top left, x2y2 - bottom right
    ball_img = image[ball[1]-ball[2]/2 : ball[1]+ball[2]/2,
        ball[0]-ball[2]/2 : ball[0]+ball[2]/2]

    # Convert cropped image to HSV
    ball_img = cv2.cvtColor(ball_img, cv2.COLOR_BGR2HSV)
    # Get color
    ball_hsv_mean = cv2.mean(ball_img)
    hue = ball_hsv_mean[0]

    if (hue < 11):
        color = 'RED'
    elif (hue < 18):
        color = 'ORANGE'
    elif (hue < 39):
        color = 'YELLOW'
    elif (hue < 76):
        color = 'GREEN'
    elif (hue < 131):
        color = 'BLUE'
    elif (hue < 161):
        color = 'VIOLET'
    elif (hue < 180):
        color = 'RED'
    else:
        color = 'UNKNOWN'
    return color


def mark_image(image, ball):
    """Mark the detected ball on the image"""
    # Draw the outer circle
    cv2.circle(image, (ball[0], ball[1]), ball[2], (0, 255, 0), 2)
    # Draw the center of the circle
    cv2.circle(image, (ball[0], ball[1]), 2, (0, 0, 255), 3)
    return image


def main():
    cam = init_camera()

    time.sleep(3)
    img, gray = take_picture(cam)
    ball = detect_circle(gray)
    while (ball == None):
        print "No ball detected..."
        time.sleep(3)
        img, gray = take_picture(cam)
        ball = detect_circle(gray)

    # Ball detected
    ball_color = detect_color(img, ball)
    marked_image = mark_image(img, ball)
    # Show results
    print "Ball with radius", ball[2], "found at position (", ball[0], ",", ball[1], ")"
    print "Color: ", ball_color
    print
    cv2.imshow('Ball detected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    release_camera(cam)


if __name__ == '__main__':
    main()
