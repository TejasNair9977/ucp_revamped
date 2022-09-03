import sys
import os
import json
import sched, time
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile,QTimer
from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer=QTimer()
        self.ui.pinger.clicked.connect(self.ping)
        self.ui.gasdispenser.clicked.connect(self.gas)
        self.ui.hrclothdispenser.clicked.connect(self.hrcloth)
        self.ui.kidispenser.clicked.connect(self.ki)
        self.ui.pbdispenser.clicked.connect(self.pb)
        self.ui.dtpadispenser.clicked.connect(self.dtpa)
        self.ui.radioButton_2.setChecked(True)
        self.ui.dial.setValue(67)
        self.ui.verticalSlider.setValue(23)
        self.timer.start(2000)
        self.timer.timeout.connect(self.ping)
        # os.system("arduino-cli upload -p COM3 --fqbn arduino:avr:uno ucp")
        # os.system("arduino-cli compile --fqbn arduino:avr:uno ucp")
        # os.system("cls")
    def gas(self):
        self.ui.label_26.setText("Dispensed Gas Masks")
        self.timeout=QTimer()
        self.timeout.singleShot(2000,self.resetdis)
    def hrcloth(self):
        self.ui.label_26.setText("Dispensed HR Cloth")
        self.timeout=QTimer()
        self.timeout.singleShot(2000,self.resetdis)
    def ki(self):
        self.ui.label_26.setText("Dispensed KI")
        self.timeout=QTimer()
        self.timeout.singleShot(2000,self.resetdis)
    def pb(self):
        self.ui.label_26.setText("Dispensed PB")
        self.timeout=QTimer()
        self.timeout.singleShot(2000,self.resetdis)
    def dtpa(self):
        self.ui.label_26.setText("Dispensed DTPA")
        self.timeout=QTimer()
        self.timeout.singleShot(2000,self.resetdis)
    def resetdis(self):
        self.ui.label_26.setText("Idle")
    def ping(self):
        self.ui.pinger.setEnabled(False)
        try:
            os.system("copy sdcard_image.ima backup.ima")
        except:
            print("file in use, will try next time")
        with open(r"backup.ima", "rb") as file:
            offset=file.read().find(b'label_2')-2
            file.seek(offset)
            byte = file.read(400)
        jsonstring=byte.decode('utf-8').rstrip('\x00')
        bjson = json.loads(jsonstring)
        bjson["radiobutton"]=self.ui.radioButton.isChecked()
        bjson["horizontalSlider"]=self.ui.horizontalSlider.value()
        bjson["dial"]=self.ui.dial.value()
        bjson["verticalSlider"]=self.ui.verticalSlider.value()
        rbyte = bytes(json.dumps(bjson),'utf-8')
        empty=b'\x00'*(400-len(rbyte))
        print(rbyte+empty)
        with open(r"backup.ima", "r+b") as file:
            file.seek(offset)
            file.write(rbyte+empty)
        print("done!")
        os.system("del backup.ima")
        self.ui.label_2.setText(str(bjson["label_2"])+" rads")
        self.ui.label_14.setText(str(bjson["label_14"])+" rads")
        self.ui.label_17.setText(str(bjson["label_17"])+" rads")
        self.ui.label_18.setText(str(bjson["label_18"])+" rads")
        extrapower=0
        reduction1=0
        reduction2=0
        if(self.ui.radioButton.isChecked()):
            extrapower=int(20+self.ui.horizontalSlider.value()/3)
            reduction1=int(bjson["label_6"]*self.ui.horizontalSlider.value()/100)
            reduction2=int(bjson["label_20"]*self.ui.horizontalSlider.value()/100)
        self.ui.label_6.setText(str(bjson["label_6"]-reduction1)+"ppm")
        self.ui.label_20.setText(str(bjson["label_20"]-reduction2)+"ppm")
        waterpressure=self.ui.dial.value()
        extrapressure=int(waterpressure/5)
        self.ui.label_22.setText("NORMAL")
        if(waterpressure>70):
            self.ui.label_22.setText("LOW")
        elif(waterpressure<40):
            self.ui.label_22.setText("HIGH")
        self.ui.label_10.setText(str(bjson["label_10"]+extrapressure)+" psi")
        self.ui.progressBar.setValue(waterpressure)
        
        self.ui.label_29.setText(str(bjson["label_29"]+extrapower)+" MW")

        
        
        self.ui.pinger.setEnabled(True)
        
if __name__ == "__main__":
    os.system("echo off")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
