import cv2
from cv_helper import open_camera, picture_loop, timer


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
