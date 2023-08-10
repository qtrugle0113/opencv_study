import cv2 as cv

path = 'videos/'
# load video
video = cv.VideoCapture(path + 'test_vid.mp4')
# new video with x2 fps
fps = int(video.get(cv.CAP_PROP_FPS)) * 2
width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
wid1, hei1 = 0, 0
# convert video to .avi
# codec = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
# convert video to mp4
codec = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
out_video = cv.VideoWriter(path + 'new_test_vid(x2_fps).mp4', codec, fps, (width, height))

if not video.isOpened():
    print('Load video fail')
    exit(1)
# loop through each frame in the video
while True:
    ret, frame = video.read()

    # ret is true when still having frame to read
    # ret is false when no more frames are available (end of video)
    if not ret:
        print('Convert done')
        break

    # Write frame to achieve a new video
    out_video.write(frame)

video.release()
out_video.release()
cv.destroyAllWindows()
