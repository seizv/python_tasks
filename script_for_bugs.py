import logging, time
from ipmp.emu.neo import NeoPanel
from ipmp.pages.rest.api import GuiApi
import threading

class DowloadConfig(object):
    def __init__(self, ip='0.0.0.0', serial='1245ABCDEF90', account='0234567890'):
        self.ip = ip
        self.serial = serial
        self.account = account
        self.api = GuiApi(self.ip, logger=logger, formt='json')
        self.api.Login.login(usr_email='admin@tycomonitor.com', usr_password='Admin123')


    def create_panel(self):
        self.panel = NeoPanel(serial=self.serial, account=self.account, media='IP', model='HS3248', logger=logger)
        self.panel.config.host = self.ip
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
        len_resp = len(response_list[0])
        return False if len_resp < 15 else True

    def start_configuration_process(self):
        while not self.panel_is_discovered():
            time.sleep(10)
            print('waiting for discovery finished {}'.format(self.serial))
        self.api.Configuration.refresh(unt_id=self.unt_id)
        pr_id = self.api.Processes.getFirstAppearedWithNeededStatusProcessId('start')
        while self.api.Processes.getProcessStatus(pr_id) != 'succeeded':
            time.sleep(15)
            print('waiting for process succeeded {}'.format(self.serial))
        self.api.Units.removeUnit(id=self.serial)



if __name__ == '__main__':
    #logging.basicConfig(level='DEBUG')
    logger = logging.getLogger()
    ip = '94.125.123.68'
    n = 10
    serials = ['%X' % (i + 0xC00000080000) for i in range(n)]
    objs = []
    tasks = []
    for i, serial in enumerate(serials):
        objs.append(DowloadConfig(ip=ip, serial=serial))
        my_thread = threading.Thread(target=objs[i].create_panel)
        my_thread.start()
        my_thread = threading.Thread(target=objs[i].start_configuration_process)
        my_thread.start()
        time.sleep(10)
    print(objs)
    #response = api.Unit.info(unt_id = '%!@#$%^&*')

