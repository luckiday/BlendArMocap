import time

import cv2


class VideoLoader:
    def __init__(self,
                 file_directory: str = "",
                 title: str = "Video Detection",
                 width: int = 640,
                 height: int = 480):
        # improved backend for windows
        
        self.capture = cv2.VideoCapture(file_directory, cv2.CAP_DSHOW)
        time.sleep(.25)

        if not self.capture.isOpened():
            # if backend cannot open capture use random backend
            self.capture = cv2.VideoCapture(file_directory)
            time.sleep(.25)

            if not self.capture.isOpened():
                raise IOError("Cannot open file")

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        self.title = title
        self.updated, self.frame = None, None
        self.color_spaces = {
            'rgb': cv2.COLOR_BGR2RGB,
            'bgr': cv2.COLOR_RGB2BGR
        }

    def update(self):
        self.updated, self.frame = self.capture.read()
        # self.frame.flags.writeable = False
        self.frame = cv2.flip(self.frame, 1)

    def set_color_space(self, space):
        self.frame = cv2.cvtColor(self.frame, self.color_spaces[space])

    def draw(self):
        cv2.imshow(self.title, self.frame)

    def exit_stream(self):
        if not self.updated:
            print("Processing Finished")
            return True
        else:
            return False

    def __del__(self):
        print("DEL STREAM")
        self.capture.release()
        cv2.destroyAllWindows()


def main():
    # stream = Webcam()
    stream = VideoLoader("test_video.mp4")
    while stream.updated:
        stream.update()
        stream.set_color_space('rgb')
        stream.set_color_space('bgr')
        stream.draw()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    del stream


if __name__ == "__main__":
    main()
