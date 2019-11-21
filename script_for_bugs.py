import logging, time
from ipmp.emu.neo import NeoPanel
from ipmp.pages.rest.api import GuiApi
import threading
import random

class DowloadConfig(object):
    def __init__(self, ip='0.0.0.0', serial='1245ABCDEF90', account='0234567890', model='HS248'):
        self.ip = ip
        self.serial = serial
        self.account = account
        self.api = api
        self.model = model


    def create_panel(self):
        self.panel = NeoPanel(serial=self.serial, account=self.account, media='IP', model=self.model, logger=logger)
        self.panel.config.host = self.ip
        self.panel.config.system_account = '00ABC' + serial[7:]
        #add devices with troubles
        self.panel.add_device("CONTACT", 11)  # device 1
        self.panel.set_device_alarm('tamper', 1, 11, 'detector')
        self.panel.add_device("MOTION_SENSOR", 12)  # device 2
        self.panel.set_device_trouble('low_battery', 1, 12, 'detector')
        self.panel.set_device_alarm('tamper', 1, 12, 'detector')
        #start session
        print('Start session {}'.format(self.serial))
        my_thread = threading.Thread(target=self.panel.connectITv2)
        my_thread.start()

    def panel_is_discovered(self):
        self.unt_id = self.api.Units.getUnitId(self.serial)
        response_list = self.api.Diagnostic.getDevices(unitId=self.unt_id)
        if not response_list: return False
        if len(response_list[0]['warnings']) == 1:
            return False
        elif len(response_list[0]['warnings']) == 0:
            return True
        elif response_list[0]['warnings'][0]['type'] == 'NOT_DISCOVERED':
            return False
        return True

    def start_configuration_process(self):
        while not self.panel_is_discovered():
            time.sleep(10)
            print('waiting for discovery finished {}'.format(self.serial))
        print('Discovery finished {}'.format(self.serial))
        self.api.Configuration.refresh(unt_id=self.unt_id)
        data = self.api.Processes.getProcesses()
        for process in data:
            if process['unt_serial'] == self.serial and process['prs_status'] == 'start' and process['prs_type'] == 'ConfigDownload':
                pr_id = process['prs_id']
        while self.api.Processes.getProcessStatus(pr_id) != 'succeeded':
            time.sleep(15)
            print('waiting for process succeeded {}'.format(self.serial))
        print('Panel remove {}'.format(self.serial))
        self.api.Units.removeUnit(id=self.serial)

    def test_once(self):
        self.unt_id = self.api.Units.getUnitId(self.serial)
        response_list = self.api.Diagnostic.getDevices(unitId=self.unt_id)
        for i in response_list:
            print(i['warnings'])


if __name__ == '__main__':
    #logging.basicConfig(level='DEBUG')
    logger = logging.getLogger()
    ip = '94.125.123.68'
    ip = '94.125.123.69'
    api = GuiApi(ip, logger=logger, formt='json')
    api.Login.login(usr_email='admin@tycomonitor.com', usr_password='Admin123')
    n = 1000
    serials = ['%X' % (i + 0xC00000080000) for i in range(n)]
    objs = tasks = []
    model_list = ['HS3248', 'HS3128', 'HS3248_12', 'HS3032']
    for i, serial in enumerate(serials):
        #serial = '7030A6A87A96'
        #serial = 'A00000'
        #objs.append(DowloadConfig(ip=ip, serial=serial, account=serial[2:], model=random.choice(model_list)))
        #objs[i].test_once()
       # break
        if i % 10 == 0 and i != 0:
            time.sleep(120)
        objs.append(DowloadConfig(ip=ip, serial=serial, account=serial[2:], model=random.choice(model_list)))
        objs[i].create_panel()
        my_thread = threading.Thread(target=objs[i].start_configuration_process)
        my_thread.start()
    #response = api.Unit.info(unt_id = '%!@#$%^&*')

