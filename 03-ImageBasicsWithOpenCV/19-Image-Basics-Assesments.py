import cv2

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (255, 0, 0), 5)

img = cv2.imread('../DATA/dog_backpack.jpg')

cv2.namedWindow(winname="Puppy")
cv2.setMouseCallback("Puppy", draw_circle)
while True:
    cv2.imshow('Puppy', img)

    # if we've waited 1ms AND we've pressed the ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
