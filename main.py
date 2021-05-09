from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import pymysql
from Layout import screen_helper
from kivymd.uix.dialog import MDDialog
import cv2 as cv
from datetime import datetime
import numpy as np
from kivy.properties import StringProperty
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from threading import Timer




conn = pymysql.connect(host="ID191774_6itn1project7.db.webhosting.be", user="ID191774_6itn1project7", password="Project7", db="ID191774_6itn1project7")
mycursor = conn.cursor()
mycursor.execute("SELECT Username from ID191774_6itn1project7.Users")
MySqlNames = mycursor.fetchall()
mycursor.execute("SELECT Password from ID191774_6itn1project7.Users")
MySqlPasswords = mycursor.fetchall()


class LoginScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class Change(Screen):
    pass


class ShowObj(Screen):
    pass

class account(Screen):
    pass


class GipApp(MDApp):
    username = StringProperty('')
    password = StringProperty('')
    TimeOfReg = StringProperty('')
    strID =  StringProperty('')

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_string(screen_helper)
        self.username = "unknown"
        self.password = "Unknown"
        self.usernameKV = "unknown"
        self.TimeOfReg = "unknown"
        self.strID = "unknown"
        self.UserData = "unknown"
        return screen

    def open_table(self):
        self.data_tables.open()



    def verify(self, username, password):
        if username != "" and password != "":
            for row in MySqlNames:
                if row[0].strip() == username:
                    sql = "SELECT Password from ID191774_6itn1project7.Users where Username = %s "
                    mycursor.execute(sql, (username))
                    TestPassword = mycursor.fetchall()
                    for row3 in TestPassword:
                        if row3[0].strip() == password:
                            dialog = MDDialog(title="Login successful")
                            dialog.open()
                            self.username = username
                            self.password = password
                            GipApp.get_running_app().root.current = 'main'


                            sql = "SELECT DateOfRegistration from ID191774_6itn1project7.Users where Username = %s "
                            mycursor.execute(sql, (username))
                            TimeOfRe = mycursor.fetchall()
                            for row4 in TimeOfRe:
                                if row4[0].strip() != "":
                                    self.TimeOfReg = row4[0].strip()

                            sql = "SELECT idUsers from ID191774_6itn1project7.Users where Username = %s "
                            mycursor.execute(sql, (username))
                            ID = mycursor.fetchall()
                            for row5 in ID:
                                if row5[0] != "":
                                    self.ID = row5[0]
                                    self.strID = str(self.ID)




                        if row3[0] != password:
                            dialog = MDDialog(title="Passwords is not correct.")
                            dialog.open()
        else:
            dialog = MDDialog(title="Fill in the empty text boxes")
            dialog.open()

    def build(self):
        screen = Builder.load_string(screen_helper)
        sql = "SELECT LoggedInUser from ID191774_6itn1project7.DetectedObjects   "
        mycursor.execute(sql)
        self.User = mycursor.fetchall()
        sql = "SELECT ObjectName from ID191774_6itn1project7.DetectedObjects  "
        mycursor.execute(sql)
        self.Object = mycursor.fetchall()
        sql = "SELECT Certainty from ID191774_6itn1project7.DetectedObjects  "
        mycursor.execute(sql)
        self.Certainty = mycursor.fetchall()
        sql = "SELECT TimeOfDetection from ID191774_6itn1project7.DetectedObjects  "
        mycursor.execute(sql)
        self.Time = mycursor.fetchall()

        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("User", dp(30)),
                ("Object", dp(30)),
                ("Certainty", dp(30)),
                ("Time", dp(30)),

            ],
            row_data=[
                (self.User),
                (self.Object),
                (self.Certainty),
                (self.Time),

            ],
        )
        return screen

    def register(self, RegUsername, RegPassword, RegRepeatPassword):
        if RegPassword != "" and RegRepeatPassword != "" and RegUsername != "":
            if RegPassword == RegRepeatPassword:
                current_datetime = datetime.now()
                insert = "INSERT INTO Users(Username, Password, DateOfRegistration) VALUES (%s,%s,%s)"
                mycursor.execute(insert, (RegUsername, RegPassword, current_datetime))
                conn.commit()
                dialog = MDDialog(title="You are successfully registered")
                dialog.open()
            if RegRepeatPassword != RegPassword:
                dialog = MDDialog(title="Passwords are not the same. Please try again.")
                dialog.open()
                print(MySqlNames)
        else:
            dialog = MDDialog(title="Fill in the empty text boxes")
            dialog.open()

    def Yolo(self):
        cap = cv.VideoCapture(0)
        whT = 320
        confThreshold = 0.6
        nmsThreshold = 0.2

        classesFile = "coco.names"
        classNames = []
        with open(classesFile, 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n')
        print(classNames)

        modelConfiguration = "yolov3.cfg"
        modelWeights = "yolov3.weights"
        net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
        net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

        def findObjects(outputs, img):
            hT, wT, cT = img.shape
            bbox = []
            classIds = []
            confs = []
            for output in outputs:
                for det in output:
                    scores = det[5:]
                    classId = np.argmax(scores)
                    confidence = scores[classId]
                    if confidence > confThreshold:
                        w, h = int(det[2] * wT), int(det[3] * hT)
                        x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                        bbox.append([x, y, w, h])
                        classIds.append(classId)
                        confs.append(float(confidence))

            indices = cv.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

            for i in indices:
                i = i[0]
                box = bbox[i]
                x, y, w, h = box[0], box[1], box[2], box[3]
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%',
                           (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

                DetectedName = (f'{classNames[classIds[i]].upper()}')
                DetectedProcent = (f'{int(confs[i] * 100)}%')
                print(DetectedName)
                print(DetectedProcent)
                current_datetime = datetime.now()
                print(current_datetime)
                insert = "INSERT INTO DetectedObjects (WayOfDetection, ObjectName, Certainty, TimeOfDetection, LoggedInUser) VALUES (%s,%s,%s,%s,%s)"
                mycursor.execute(insert, ("webcam", DetectedName, DetectedProcent, current_datetime, self.username))
                conn.commit()


        while True:
            success, img = cap.read()

            blob = cv.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
            net.setInput(blob)
            layersNames = net.getLayerNames()
            outputNames = [(layersNames[i[0] - 1]) for i in net.getUnconnectedOutLayers()]
            outputs = net.forward(outputNames)
            findObjects(outputs, img)


            cv.imshow('Image', img)
            key = cv.waitKey(1)
            if key == 27:
                break



    def Change(self, Password, PasswordReg):
        if Password != "" and PasswordReg != "":
            if Password == PasswordReg:
                insert = "UPDATE `Users` SET `Password`= %s where Username = %s "
                mycursor.execute(insert, (PasswordReg, self.username))
                print(self.username)
                conn.commit()
                dialog = MDDialog(title="The password has been changed.")
                dialog.open()
            if Password != PasswordReg: 
                dialog = MDDialog(title="New passwords are not the same. Please try again.")
                dialog.open()
                print(MySqlNames)
        else:
            dialog = MDDialog(title="Fill in the empty text boxes")
            dialog.open()






if __name__ == '__main__':
    GipApp().run()
