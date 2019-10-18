import cv2
import time
import functools


def open_camera(camera_num):
    """
    Generator that initialize camera and read read images from it in loop

    :param camera_num: number of camera to initialize and read
    :yield: image in OpenCV format
    """
    camera = cv2.VideoCapture(camera_num)
    while camera.isOpened():
        ret, frame = camera.read()
        if ret:
            yield frame
    camera.release()


def picture_loop(wait_for_key='q', camera_num=0):
    """
    Decorator that read pictures from camera
    and execute wrapping function with picture as function argument
    until corresponding key is pressed.

    :param wait_for_key: char that must be pressed to stop wrapping function call
    :param camera_num: number of camera to take pictures from
    :return:
    """
    def function_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for picture in open_camera(camera_num):
                if func(picture) & 0xFF == ord(wait_for_key):
                    break
            return
        return wrapper
    return function_wrapper


def timer(func):
    """
    Decorator that prints function execution time

    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print("Time of function {} execution  is {} sec".format(func.__name__, duration))
        return result
    return wrapper


@picture_loop(wait_for_key='q', camera_num = 0)
@timer
def process_frame(frame):
    """
    Flip received picture and show it in window
    After read keyboard and return value of pressed key

    :param frame: picture to display
    :return: cide of pressed key
    """
    frame = cv2.flip(frame, 1)
    cv2.imshow('frame', frame)
    return cv2.waitKey(1)


if __name__ == "__main__":
    process_frame(None)
    cv2.destroyAllWindows()
