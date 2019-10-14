import logging, time
from ipmp.emu.neo import NeoPanel
from ipmp.pages.rest.api import GuiApi
import threading
import json

class RestAnswers(object):
    def __init__(self, ip='0.0.0.0', serial='1245ABCDEF90'):
        self.ip = ip
        self.serial = serial

    def show_warnings(self):
        api = GuiApi(self.ip, logger=logger, formt='json')
        api.Login.login(usr_email='admin@tycomonitor.com', usr_password='Admin123')
        while not self.panel_is_activated():
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

    def panel_is_activated(self):
        api = GuiApi(self.ip, logger=logger, formt='json')
        api.Login.login(usr_email='admin@tycomonitor.com', usr_password='Admin123')
        unt_id = api.Units.getUnitId(self.serial)
        response_list = api.Diagnostic.getDevices(unitId=unt_id)
        if response_list:
            for i in response_list:
                if i['warnings'] is not None:
                    for list_i in i['warnings']:
                        if i['device_type'] == 'CONTROL_PANEL' and list_i['type'] == 'NOT_DISCOVERED':
                            return False
            return True

    def walk_test(self):
        api = GuiApi(self.ip, logger=logger, formt='json')
        api.Login.login(usr_email='admin@tycomonitor.com', usr_password='Admin123')
        unt_id = api.Units.getUnitId(self.serial)
        #response_list = api.Diagnostic.getDevices(unitId=unt_id)
        response = api.Unit.info(unt_id=unt_id)
        print(api.Units(unt_id, response))


if __name__ == '__main__':
    #----------precondition----------------------
    logging.basicConfig(level='DEBUG')
    logger = logging.getLogger()
    ip = '94.125.123.68'
    serial = '1245ABCDEF96'
    #-----------create_classes-------------------
    answers = RestAnswers(ip=ip, serial=serial)
    #------------start---------------------------
    answers.walk_test()


