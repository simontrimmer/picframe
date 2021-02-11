"""Keyboard interface of picture_frame."""

import logging
import sys
import threading
import time
sys.path.insert(1,'/home/herbe/dev/pi3d')
import pi3d


class InterfaceKbd:
    """Keyboard interface of picture_frame.
    
    This interface interacts via keyboard with the user to steer the image display.

    Attributes
    ----------
    controller : Controler 
        Controller for picture_frame
   

    Methods
    -------

    """

    def __init__(self, controller):
        self.__logger = logging.getLogger("interface_kbd.InterfaceKbd")
        self.__logger.info('creating an instance of InterfaceKbd')
        self.__controller = controller
        self.__keyboard = pi3d.Keyboard()
        self.__keep_looping = True
        t = threading.Thread(target=self.__loop)
        t.start()

    def __loop(self):
        while self.__keep_looping:
            key = self.__keyboard.read()
            if key == 27:
                self.__keep_looping = False
            elif key == ord('a'):
                self.__controller.back()
            elif key == ord('d'):
                self.__controller.next()
            time.sleep(0.025)
        self.__keyboard.close() # contains references to Display instance
        self.__controller.stop()
    