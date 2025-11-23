from serial.tools import list_ports
import serial
import time
import csv
import threading
import numpy as np
import pandas as pds
import matplotlib.pyplot as plt


ports = list_ports.comports()
for port in ports: print(port)

CSVFile = open("data.csv","w",newline='')
CSVFile.truncate()

ArduinoData = serial.Serial('/dev/cu.DSDTECHHC-05',9600)

#reset the arduino serial
ArduinoData.setDTR(False)
time.sleep(1)
ArduinoData.flushInput()
ArduinoData.setDTR(True)


row = 0
ProgramOn = True
TimeStamps = []

def ListenForStop():
    global ProgramOn
    input("Press enter to stop program")
    ProgramOn = False


def RecordData():
    StartTime = time.time()
    while ProgramOn == True:
        global row
        global TimeStamps
        try:
            s_bytes = ArduinoData.readline()
            decode_bytes = s_bytes.decode('utf-8').strip('\r\n')
           
            
            if row == 0:
                values = [str('Temp 1'),str('Temp 2'), str('Temp 3'), str('Temp 4')]
            else:
                values = [float(x) for x in decode_bytes.split(",")]
                ElapsedTime = time.time() - StartTime
                ElapsedTimeFormatted = float(f"{ElapsedTime:.2f}")
                TimeStamps.append(ElapsedTimeFormatted)
        
            print(values)
        
            writer = csv.writer(CSVFile,delimiter=",")
            writer.writerow(values)
        except:
            print("ERROR, Line was not recorded.")
        
        
        
        row = row + 1

def CreateGraph():
    global TimeStamps
    data = pds.read_csv("data.csv")
    print(data)
    D = data.to_numpy()
    temp1 = D[ :,0]
    temp2 = D[ :,1]
    temp3 = D[ :,2]
    temp4 = D[ :,3]

    plt.plot(TimeStamps,temp1, label = "Temp 1")
    plt.plot(TimeStamps,temp2, label = "Temp 2")
    plt.plot(TimeStamps,temp3, label = "Temp 3")
    plt.plot(TimeStamps,temp4, label = "Temp 4")
    plt.legend()
    plt.title("Thermocouple Temperature")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (C)")
    plt.style.use('fivethirtyeight')
    plt.savefig('basic.png')
    plt.show()
    





StopThread = threading.Thread(target=ListenForStop)
StopThread.start()

RecordData()

StopThread.join()

if ProgramOn == False:
    CSVFile.close()
    CreateGraph()
