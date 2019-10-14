import logging, time
from ipmp.emu.neo import NeoPanel
from ipmp.pages.rest.api import GuiApi
import threading
import json


class SimpleEmu(object):
    def __init__(self, ip='0.0.0.0', serial='1245ABCDEF90'):
        self.ip = ip
        self.serial = serial

    def new_neo_panel(self, account='1234567890'):
        self.account = account
        '''
        formatter = logging.Formatter('%(asctime)s::: %(message)s')
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)
        '''
        self.panel = NeoPanel(serial=self.serial, account=self.account, media='IP', model='HS3128', logger=logger)
        self.panel.config.host = self.ip

    def add_devices(self):
        self.panel.add_device("CONTACT", 11) #device 1
        #set alarm for device 1 zone 11
        self.panel.set_device_alarm('tamper', 1, 11, 'detector')
        self.panel.add_device("MOTION_SENSOR", 12) #device 2
        # set trouble and alarm for device 2 zone 12
        self.panel.set_device_trouble('low_battery', 1, 12, 'detector')
        self.panel.set_device_alarm('tamper', 1, 12, 'detector')

    def start_process(self):
        self.panel.connectITv2()
        self.panel.stopITv2Session()
        self.panel.config.VK.active = False


class RestAnswers(object):
    def __init__(self, ip='0.0.0.0', serial='1245ABCDEF90'):
        self.ip = ip
        self.serial = serial

    def show_warnings(self):
        api = GuiApi(self.ip, logger=logger, formt='json')
        api.Login.login(usr_email='admin@tycomonitor.com', usr_password='Admin123')
        while not self.panel_is_discovered():
            time.sleep(5)
        unt_id = api.Units.getUnitId(self.serial)
        response_list = api.Diagnostic.getDevices(unitId=unt_id)
        #response = api.Unit.info(unt_id=unt_id)
        #response_info = api.Units.getPanelInfo(response=response)
        for i in response_list:
            if i['warnings'] is not None:
                for list_i in i['warnings']:
                    print("Device({}): {}, Problem: {}, Title: {}"
                          .format(i['enrollment_id'], i['subtype'], list_i['severity'], list_i['type']))
        '''        
        response_data = response.json()
        for key, value in response_data['data'].items():
            print("{}, {}".format(key, value))
        '''

    def panel_is_discovered(self):
        api = GuiApi(self.ip, logger=logger, formt='json')
        api.Login.login(usr_email='admin@tycomonitor.com', usr_password='Admin123')
        unt_id = api.Units.getUnitId(self.serial)
        response_list = api.Diagnostic.getDevices(unitId=unt_id)
        if response_list:
            for i in response_list:
                if i['warnings'] is not None:
                    for list_i in i['warnings']:
                        if list_i['type'] == 'NOT_DISCOVERED':
                            return False
            return True


if __name__ == '__main__':
    #----------precondition----------------------
    logging.basicConfig(level='DEBUG')
    logger = logging.getLogger()
    ip = '94.125.123.68'
    serial = '1245ABCDEF96'
    #-----------create_classes-------------------
    emu_test = SimpleEmu(ip=ip, serial=serial)
    emu_test.new_neo_panel()
    emu_test.add_devices()
    answers = RestAnswers(ip=ip, serial=serial)
    #------------start---------------------------
    my_thread = threading.Thread(target=emu_test.start_process)
    my_thread.start()
    my_thread = threading.Thread(target=answers.show_warnings)
    my_thread.start()







