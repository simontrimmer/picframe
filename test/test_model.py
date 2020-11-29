import pytest
import logging

import os


from picframe import model

logger = logging.getLogger("test_model")
logger.setLevel(logging.DEBUG)

def test_model_init():
    m = model.Model('/home/pi/dev/picture_frame/picframe/configuration.yaml')
    mqtt = m.get_mqtt_config()
    assert mqtt['server'] == 'home'
    viewer = m.get_viewer_config()
    assert viewer['test_key'] == 'test_value'
  

def test_for_file_changes():
    m = model.Model('/home/pi/dev/picture_frame/picframe/configuration.yaml')
    m.subdirectory = 'testdir'
    testfile = m.get_model_config()['pic_dir'] + "/"+ 'testdir' + "/testfile.jpg"
    assert m.check_for_file_changes() == False
    os.mknod(testfile)
    assert m.check_for_file_changes() == True
    os.remove(testfile)

def test_get_files():
    m = model.Model('/home/pi/dev/picture_frame/picframe/configuration.yaml')
    num = m.get_number_of_files()
    assert num == 443 # actual image folder 

def test_get_file_for_empty_dir():
    m = model.Model('/home/pi/dev/picture_frame/picframe/configuration.yaml')
    m.subdirectory = 'testdir'
    file = m.get_next_file()
    assert file == '/home/pi/dev/picture_frame/picframe/PictureFrame2020img.jpg'

def test_getter_setter_fade_time():
    m = model.Model('/home/pi/dev/picture_frame/picframe/configuration.yaml')
    assert m.fade_time == 10.0
    m.fade_time = 20.0
    assert m.fade_time == 20.0

def test_getter_setter_time_delay():
    m = model.Model('/home/pi/dev/picframe/picframe/configuration.yaml')
    assert m.time_delay == 200.0
    m.time_delay = 21.0
    assert m.time_delay == 21.0

def test_getter_setter_subdirectory():
    m = model.Model('/home/pi/dev/picframe/picframe/configuration.yaml')
    assert m.subdirectory == ''
    m.subdirectory = 'testdir'
    assert m.subdirectory == 'testdir'

def test_getter_setter_shuffle():
    m = model.Model('/home/pi/dev/picframe/picframe/configuration.yaml')
    assert m.shuffle == True
    m.shuffle = False
    assert m.shuffle == False
