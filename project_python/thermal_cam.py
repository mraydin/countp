import sys
import numpy as np
import cv2
import matplotlib as mpl
import matplotlib.cm as mtpltcm

def main(argv):
    cap = cv2.VideoCapture(0)

    #initialize the colormap
    colormap = mpl.cm.jet
    cNorm = mpl.colors.Normalize(vmin=0, vmax=255)
    scalarMap = mtpltcm.ScalarMappable(norm=cNorm, cmap=colormap)


    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#add blur to make it more realistic
        blur = cv2.GaussianBlur(gray,(11,11),0)
        #thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)[1]
        #thresh = cv2.erode(thresh, None, iterations=4)
        #thresh = cv2.dilate(thresh, None, iterations=6)
		#assign colormap
        colors = scalarMap.to_rgba(blur, bytes=False)

        # Display the resulting frame
        cv2.imshow('frame', colors)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
