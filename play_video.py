import cv2 as cv

path = 'videos/'
# load video
video = cv.VideoCapture(path + 'test_vid.mp4')
fps = video.get(cv.CAP_PROP_FPS)
frame_delay = int(1000/fps)
print('fps = ', fps, 'frame delay =', frame_delay)

if not video.isOpened():  # or if cap.isOpen() == False
    print('Load video fail')
    exit(1)

# loop through each frame in the video
while True:
    ret, frame = video.read()

    # ret is true when still having frame to read
    # ret is false when no more frames are available (end of video)
    if not ret:
        print('Video end')
        break

    # show current frame
    cv.imshow('Video', frame)
    # press any key to break the loop/quit video
    if cv.waitKey(frame_delay) > 0:
        print('Stop playing video')
        break
video.release()
# cv.destroyWindow('Video')
cv.destroyAllWindows()
