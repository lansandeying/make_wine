#coding = utf-8

from airtest.core.android.recorder import *
from airtest.core.android.adb import *

class Recoding():
    def __init__(self,device):
        self.device = device
        adb = ADB(serialno=self.device)
        self.recorder = Recorder(adb)

    def star_recoding(self):
        # ¿ªÆô
        self.recorder.start_recording()

    def end_recoding(self,recoding_path):
        #¹Ø±Õ
        self.recorder.stop_recording(output=recoding_path + r"\wine.mp4")