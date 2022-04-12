import time

import cv2


class Webcam:
    def __init__(self,
                 camera_index: int = 0,
                 title: str = "Stream Detection",
                 width: int = 640,
                 height: int = 480):
        # improved backend for windows
        self.capture = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        time.sleep(.25)

        if not self.capture.isOpened():
            # if backend cannot open capture use random backend
            self.capture = cv2.VideoCapture(camera_index)
            time.sleep(.25)

            if not self.capture.isOpened():
                raise IOError("Cannot open webcam")

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
        self.updated, frame = self.capture.read()
        self.frame = cv2.flip(frame, 1)

    def set_color_space(self, space):
        self.frame = cv2.cvtColor(self.frame, self.color_spaces[space])

    def draw(self):
        cv2.imshow(self.title, self.frame)

    def exit_stream(self):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("ATTEMPT TO EXIT STEAM")
            return True
        else:
            return False

    def __del__(self):
        print("DEL STREAM")
        self.capture.release()
        cv2.destroyAllWindows()


class VideoLoader:
    def __init__(self,
                 file_directory: str,
                 title: str = "Stream Detection",
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
        self.success, self.frame = None, None
        self.color_spaces = {
            'rgb': cv2.COLOR_BGR2RGB,
            'bgr': cv2.COLOR_RGB2BGR
        }

    def update(self):
        self.success, self.frame = self.capture.read()
        # self.frame.flags.writeable = False
        # self.frame = cv2.flip(frame, 1)

    def set_color_space(self, space):
        self.frame = cv2.cvtColor(self.frame, self.color_spaces[space])

    def draw(self):
        cv2.imshow(self.title, self.frame)

    def exit_stream(self):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("ATTEMPT TO EXIT STEAM")
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
    while stream.success:
        stream.update()
        stream.set_color_space('rgb')
        stream.set_color_space('bgr')
        stream.draw()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    del stream


if __name__ == "__main__":
    main()
