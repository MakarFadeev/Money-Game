from tkinter import *
import random
import time,sys
import webbrowser as wb
import tkinter.messagebox as mb
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QMessageBox,QDialog
# ВНИМАНИЕ!!! Игра НЕ является доработанной,
# все баги будут исправлятся В БУДУЕЩЕМ!!!
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLobby = QtWidgets.QGroupBox(self.centralwidget)
        self.mainLobby.setGeometry(QtCore.QRect(0, 0, 541, 561))
        self.mainLobby.setObjectName("mainLobby")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainLobby)
        self.verticalLayout.setObjectName("verticalLayout")
        self.coins = QtWidgets.QLabel(self.mainLobby)
        self.coins.setAlignment(QtCore.Qt.AlignCenter)
        self.coins.setObjectName("coins")
        self.verticalLayout.addWidget(self.coins)
        self.profile = QtWidgets.QPushButton(self.mainLobby)
        self.profile.setAutoDefault(False)
        self.profile.setDefault(False)
        self.profile.setFlat(False)
        self.profile.setObjectName("profile")
        self.verticalLayout.addWidget(self.profile)
        self.priceOil = QtWidgets.QLabel(self.mainLobby)
        self.priceOil.setAlignment(QtCore.Qt.AlignCenter)
        self.priceOil.setObjectName("priceOil")
        self.verticalLayout.addWidget(self.priceOil)
        self.priceCotton = QtWidgets.QLabel(self.mainLobby)
        self.priceCotton.setAlignment(QtCore.Qt.AlignCenter)
        self.priceCotton.setObjectName("priceCotton")
        self.verticalLayout.addWidget(self.priceCotton)
        self.priceGold = QtWidgets.QLabel(self.mainLobby)
        self.priceGold.setAlignment(QtCore.Qt.AlignCenter)
        self.priceGold.setObjectName("priceGold")
        self.verticalLayout.addWidget(self.priceGold)
        self.oil = QtWidgets.QLabel(self.mainLobby)
        self.oil.setAlignment(QtCore.Qt.AlignCenter)
        self.oil.setObjectName("oil")
        self.verticalLayout.addWidget(self.oil)
        self.cotton = QtWidgets.QLabel(self.mainLobby)
        self.cotton.setAlignment(QtCore.Qt.AlignCenter)
        self.cotton.setObjectName("cotton")
        self.verticalLayout.addWidget(self.cotton)
        self.gold = QtWidgets.QLabel(self.mainLobby)
        self.gold.setAlignment(QtCore.Qt.AlignCenter)
        self.gold.setObjectName("gold")
        self.verticalLayout.addWidget(self.gold)
        self.deathTime = QtWidgets.QLabel(self.mainLobby)
        self.deathTime.setAlignment(QtCore.Qt.AlignCenter)
        self.deathTime.setObjectName("deathTime")
        self.verticalLayout.addWidget(self.deathTime)
        self.end_month = QtWidgets.QPushButton(self.mainLobby)
        self.end_month.setEnabled(True)
        self.end_month.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.end_month.setStyleSheet("#end_month{\n"
"padding-left:0;\n"
"padding-right:0;\n"
"}")
        self.end_month.setObjectName("end_month")
        self.verticalLayout.addWidget(self.end_month)
        self.Buy = QtWidgets.QGroupBox(self.centralwidget)
        self.Buy.setGeometry(QtCore.QRect(540, 0, 311, 171))
        self.Buy.setObjectName("Buy")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Buy)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self._10__100__1000_ = QtWidgets.QHBoxLayout()
        self._10__100__1000_.setObjectName("_10__100__1000_")
        self._10_ = QtWidgets.QPushButton(self.Buy)
        self._10_.setObjectName("_10_")
        self._10__100__1000_.addWidget(self._10_)
        self._100_ = QtWidgets.QPushButton(self.Buy)
        self._100_.setObjectName("_100_")
        self._10__100__1000_.addWidget(self._100_)
        self._1000_ = QtWidgets.QPushButton(self.Buy)
        self._1000_.setObjectName("_1000_")
        self._10__100__1000_.addWidget(self._1000_)
        self.verticalLayout_3.addLayout(self._10__100__1000_)
        self.countType = QtWidgets.QHBoxLayout()
        self.countType.setObjectName("countType")
        self.typeLabel = QtWidgets.QLabel(self.Buy)
        self.typeLabel.setObjectName("typeLabel")
        self.countType.addWidget(self.typeLabel)
        self.type = QtWidgets.QComboBox(self.Buy)
        self.type.setEditable(False)
        self.type.setMaxVisibleItems(0)
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.countType.addWidget(self.type)
        self.countLabel = QtWidgets.QLabel(self.Buy)
        self.countLabel.setObjectName("countLabel")
        self.countType.addWidget(self.countLabel)
        self.count = QtWidgets.QSpinBox(self.Buy)
        self.count.setObjectName("count")
        self.count.setMaximum(10000000)
        self.countType.addWidget(self.count)
        self.verticalLayout_3.addLayout(self.countType)
        self._10_100_1000 = QtWidgets.QHBoxLayout()
        self._10_100_1000.setObjectName("_10_100_1000")
        self._10 = QtWidgets.QPushButton(self.Buy)
        self._10.setObjectName("_10")
        self._10_100_1000.addWidget(self._10)
        self._100 = QtWidgets.QPushButton(self.Buy)
        self._100.setObjectName("_100")
        self._10_100_1000.addWidget(self._100)
        self._1000 = QtWidgets.QPushButton(self.Buy)
        self._1000.setObjectName("_1000")
        self._10_100_1000.addWidget(self._1000)
        self.verticalLayout_3.addLayout(self._10_100_1000)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buy = QtWidgets.QPushButton(self.Buy)
        self.buy.setObjectName("buy")
        self.horizontalLayout.addWidget(self.buy)
        self.sell = QtWidgets.QPushButton(self.Buy)
        self.sell.setObjectName("sell")
        self.horizontalLayout.addWidget(self.sell)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.Other = QtWidgets.QGroupBox(self.centralwidget)
        self.Other.setGeometry(QtCore.QRect(540, 170, 311, 391))
        self.Other.setObjectName("Other")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Other)
        self.verticalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.helpTeam = QtWidgets.QPushButton(self.Other)
        self.helpTeam.setObjectName("helpTeam")
        self.verticalLayout_2.addWidget(self.helpTeam)
        self.discord = QtWidgets.QPushButton(self.Other)
        self.discord.setObjectName("discord")
        self.verticalLayout_2.addWidget(self.discord)
        self.site = QtWidgets.QPushButton(self.Other)
        self.site.setObjectName("site")
        self.verticalLayout_2.addWidget(self.site)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainLobby.setTitle(_translate("MainWindow", "Профиль"))
        self.coins.setText(_translate("MainWindow", "У вас есть 10000 РублеКоинов"))
        self.profile.setText(_translate("MainWindow", "Профиль"))
        self.priceOil.setText(_translate("MainWindow", "Цена нефти 60 РублеКоинов за литр"))
        self.priceCotton.setText(_translate("MainWindow", "Цена хлопка 200 РублеКоинов за килограмм"))
        self.priceGold.setText(_translate("MainWindow", "Цена золота 30000 РублеКоинов за слиток"))
        self.oil.setText(_translate("MainWindow", "У вас есть 0 литров нефти"))
        self.cotton.setText(_translate("MainWindow", "У вас есть 0 килограмм хлопка"))
        self.gold.setText(_translate("MainWindow", "У вас есть 0 слитков золота"))
        self.deathTime.setText(_translate("MainWindow", "До конца игры осталось 360 месяцев"))
        self.end_month.setText(_translate("MainWindow", "Закончить месяц"))
        self.Buy.setTitle(_translate("MainWindow", "Покупка"))
        self._10_.setText(_translate("MainWindow", "+10"))
        self._100_.setText(_translate("MainWindow", "+100"))
        self._1000_.setText(_translate("MainWindow", "+1000"))
        self.typeLabel.setText(_translate("MainWindow", "тип:"))
        self.type.setCurrentText(_translate("MainWindow", "нефть"))
        self.type.setItemText(0, _translate("MainWindow", "нефть"))
        self.type.setItemText(1, _translate("MainWindow", "хлопок"))
        self.type.setItemText(2, _translate("MainWindow", "золото"))
        self.countLabel.setText(_translate("MainWindow", "количество:"))
        self._10.setText(_translate("MainWindow", "-10"))
        self._100.setText(_translate("MainWindow", "-100"))
        self._1000.setText(_translate("MainWindow", "-1000"))
        self.buy.setText(_translate("MainWindow", "Купить"))
        self.sell.setText(_translate("MainWindow", "Продать"))
        self.Other.setTitle(_translate("MainWindow", "Другое"))
        self.helpTeam.setText(_translate("MainWindow", "Поддержать Команду"))
        self.discord.setText(_translate("MainWindow", "Дискорд сервер игры"))
        self.site.setText(_translate("MainWindow", "Сайт игры"))
class Ui_Profile(object):
    def setupUi(self, Profile):
        Profile.setObjectName("Profile")
        Profile.resize(200, 100)
        Profile.setToolTipDuration(-9)
        Profile.setSizeGripEnabled(False)
        Profile.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Profile)
        self.verticalLayout.setObjectName("verticalLayout")
        self.profile = QtWidgets.QLabel(Profile)
        self.profile.setAlignment(QtCore.Qt.AlignCenter)
        self.profile.setObjectName("profile")
        self.verticalLayout.addWidget(self.profile)
        self.label = QtWidgets.QLabel(Profile)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.profile1 = QtWidgets.QPushButton(Profile)
        self.profile1.setObjectName("profile1")
        self.verticalLayout.addWidget(self.profile1)

        self.retranslateUi(Profile)
        QtCore.QMetaObject.connectSlotsByName(Profile)

    def retranslateUi(self, Profile):
        _translate = QtCore.QCoreApplication.translate
        Profile.setWindowTitle(_translate("Profile", "Profile"))
        self.profile.setText(_translate("Profile", "Вы Интерн"))
        self.label.setText(_translate("Profile", "Вы зарабатаваете 15000"))
        self.profile1.setText(_translate("Profile", "Запросить повышение"))
# Делал Mikro, Mikro#5986

# Настройки окна

app = QApplication(sys.argv)
window=QMainWindow()
profileD=QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)
profile=Ui_Profile()
profile.setupUi(profileD)
money = 10000
oilPrice = 60
cottonPrice = 200
goldPrice = 30000
oilHave = 0
cottonHave = 0
goldHave = 0
timeUntilDeath = 360
timeLeft = 0
whatAboutMe = 'Вы не запрашивали повышения'
QMessageBox.information(window,'деньги и экономия','добро пожаловать в "деньги и экономия"! ваша цель - заработать 1 миллиард за 30 лет.',QMessageBox.Ok,QMessageBox.Ok)
textOil = 'Цена нефти 60 РублеКоинов за литр'
textCotton = 'Цена хлопка 200 РублеКоинов за килограмм'
textGold = 'Цена золота 30000 РублеКоинов за слиток'
howMoney = 'У вас есть 10000 РублеКоинов'
howManyOilHave = 'У вас есть 0 литров нефти'
howManyCottonHave = 'У вас есть 0 килограмм хлопка'
howManyGoldHave = 'У вас есть 0 слитков золота'
positions = ['Интерн', 'Секретарь', 'Новичок', 'Джуниор', 'Опытный', 'Сениор', 'Специалист', 'Начальник',
             'Владелец компании']
engPositions = ['Intern', 'Secretary', 'Newbie', 'Junior', 'Experienced', 'Senior', 'Specialist', 'Chief',
                'Owner of company']
positionsProfit = [15000, 22500, 30000, 47500, 55000, 62500, 70000, 77500, 85000, 90000]
positionNum = 0
yourPosition = 'Вы Интерн'
positionProfit = 'Вы зарабатываете 15000'
timeUntilDeathText = 'До конца игры осталось 360 месяцев'
canGetRice = 3
canDie = True
isRussian = True
isEnglish = False


def fBuyOil():
    global ui
    global money, oilPrice, oilHave
    howMany = int(ui.count.value())
    price = howMany * oilPrice
    price = int(price)
    money = int(money)
    if (price <= money and howMany >= 1):
        oilHave += howMany
        money -= price
        howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
        ui.oil.setText('У вас есть ' + str(oilHave) + ' литров нефти')
        ui.coins.setText(howMoney)
    else:
            QMessageBox.information(window,'РублеКоины','Недостаточно РублеКоинов!',QMessageBox.Ok,QMessageBox.Ok)


def fSellOil():
    global ui
    global money, oilPrice, oilHave
    howMany = int(ui.count.value())
    price = howMany * oilPrice
    price = int(price)
    money = int(money)
    if (howMany <= oilHave and howMany > 0):
        oilHave -= howMany
        money += price
        ui.oil.setText('У вас есть ' + str(oilHave) + ' литров нефти')
        ui.coins.setText('У вас есть ' + str(money) + ' РублеКоинов')
    else:
        QMessageBox.information(window, 'нефть', 'Недостаточно нефти', QMessageBox.Ok, QMessageBox.Ok)


def fBuyCotton():
    global ui
    global money, cottonPrice, cottonHave
    howMany = int(ui.count.value())
    price = howMany * cottonPrice
    price = int(price)
    money = int(money)
    if (price <= money and howMany >= 1):
        cottonHave += howMany
        money -= price
        howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
        ui.cotton.setText('У вас есть ' + str(cottonHave) + ' литров нефти')
        ui.coins.setText(howMoney)
    else:
        QMessageBox.information(window, 'РублеКоины', 'Недостаточно РублеКоинов!', QMessageBox.Ok, QMessageBox.Ok)


def fSellCotton():
    global ui
    global money, cottonPrice, cottonHave
    howMany = int(ui.count.value())
    price = howMany * cottonPrice
    price = int(price)
    money = int(money)
    if (howMany <= cottonHave and howMany > 0):
        cottonHave -= howMany
        money += price
        ui.cotton.setText('У вас есть ' + str(cottonHave) + ' литров нефти')
        ui.coins.setText('У вас есть ' + str(money) + ' РублеКоинов')
    else:
        QMessageBox.information(window, 'нефть', 'Недостаточно нефти', QMessageBox.Ok, QMessageBox.Ok)


def fBuyGold():
    global ui
    global money, goldPrice, goldHave
    howMany = int(ui.count.value())
    price = howMany * goldPrice
    price = int(price)
    money = int(money)
    if (price <= money and howMany >= 1):
        goldHave += howMany
        money -= price
        howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
        ui.gold.setText('У вас есть ' + str(goldHave) + ' литров нефти')
        ui.coins.setText(howMoney)
    else:
        QMessageBox.information(window, 'РублеКоины', 'Недостаточно РублеКоинов!', QMessageBox.Ok, QMessageBox.Ok)


def fSellGold():
    global ui
    global money, goldPrice, goldHave
    howMany = int(ui.count.value())
    price = howMany * goldPrice
    price = int(price)
    money = int(money)
    if (howMany <= goldHave and howMany > 0):
        goldHave -= howMany
        money += price
        ui.gold.setText('У вас есть ' + str(goldHave) + ' литров нефти')
        ui.coins.setText('У вас есть ' + str(money) + ' РублеКоинов')
    else:
        QMessageBox.information(window, 'нефть', 'Недостаточно нефти', QMessageBox.Ok, QMessageBox.Ok)


def endThisMonth():
    global canDie, canGetRice, timeUntilDeath, timeLeft, goldPrice, cottonPrice, oilPrice,  textOil, textCotton, textGold, money,ui
    timeUntilDeath -= 1
    goldPrice += random.randint(-2000, 2000)
    cottonPrice += random.randint(-500, 500)
    oilPrice += random.randint(-100, 100)
    if (goldPrice < 15000):
        goldPrice += 2500
    if (cottonPrice < 70):
        cottonPrice += 400
    if (oilPrice < 20):
        oilPrice += 300
    if (oilPrice > 1000):
        oilPrice -= 300
    if (goldPrice > 75000):
        goldPrice -= 2500
    if (cottonPrice > 2000):
        cottonPrice -= 400
    money += positionsProfit[positionNum]
    if (isRussian):
        timeUntilDeathText = 'До конца игры осталось ' + str(timeUntilDeath) + ' месяцев'
        textOil = 'Цена нефти ' + str(oilPrice) + ' РублеКоинов за литр'
        textCotton = 'Цена хлопка ' + str(cottonPrice) + ' РублеКоинов за килограмм'
        textGold = 'Цена золота ' + str(goldPrice) + ' РублеКоинов за слиток'
        howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'

    ui.deathTime.setText(timeUntilDeathText)
    ui.priceOil.setText(textOil)
    ui.priceCotton.setText(textCotton)
    ui.priceGold.setText(textGold)
    ui.coins.setText(howMoney)
    canGetRice = 3

    ui.count.clear()
    if timeUntilDeath == 0:
        if canDie == True:
            ui.end_month.setText('You lose')
            ui.end_month.clicked.connect(lambda :None)
    if money >= 1000000000:

        print('Поздравляем вас! Вы заработали 1 миллиард РублеКоинов менее чем за 30 лет! Вы получили бессмертие!')
        canDie = False


def openMyProfile():
    global yourPosition,profile,positionsProfit,positionNum,positionProfit,positions,isRussian,isEnglish

    if (isRussian):

        position = 'Вы ' + positions[positionNum]
        positionProfit = 'Вы зарабатываете ' + str(positionsProfit[positionNum]) + ' РублеКоинов в месяц'
        # Профиль
        # Работа
        profile.profile.setText(position)
        profile.label.setText(positionProfit)
        profile.profile1.clicked.connect(iNeedRice)
        profileD.open()


    if (isEnglish):

        position = 'You are ' + engPositions[positionNum]
        positionProfit = 'You earn ' + str(positionsProfit[positionNum]) + ' RubleCoins per month'




def iNeedRice():
    global positionNum, canGetRice,profile
    whatWithMe = random.randint(0, 100)
    if canGetRice == 0:
        if (isRussian):
            QMessageBox.information(window,"должность",'Вы не можете запросить повышение!',QMessageBox.Ok,QMessageBox.Ok)
        if (isEnglish):
            QMessageBox.information(window,"должность",'You can not require raising!',QMessageBox.Ok,QMessageBox.Ok)
    if canGetRice > 0:
        canGetRice -= 1
        if whatWithMe < 11:
            if (isRussian):
                QMessageBox.information(window,"должность",'Вас повысили!',QMessageBox.Ok,QMessageBox.Ok)
            if (isEnglish):
                QMessageBox.information(window,"должность",'You increased!',QMessageBox.Ok,QMessageBox.Ok)
            if positionNum != 8:
                positionNum += 1
                if (isRussian):
                    position = 'Вы ' + positions[positionNum]
                    positionProfit = 'Вы зарабатываете ' + str(positionsProfit[positionNum]) + ' РублеКоинов в месяц'
                if (isEnglish):
                    position = 'You are ' + engPositions[positionNum]
                    positionProfit = 'You earn ' + str(positionsProfit[positionNum]) + ' RubleCoins per month'
                profile.profile.setText(position)
                profile.label.setText(positionProfit)
        if whatWithMe > 10 and whatWithMe < 76:
            if (isRussian):
                QMessageBox.information(window,"должность",'Вам отказали!',QMessageBox.Ok,QMessageBox.Ok)
            if (isEnglish):
                QMessageBox.information(window,"должность",'You were denied!',QMessageBox.Ok,QMessageBox.Ok)
        if whatWithMe > 75:
            if (isRussian):
                QMessageBox.information(window,"должность",'Вас понизили!',QMessageBox.Ok,QMessageBox.Ok)
            if (isEnglish):
                QMessageBox.information(window,"должность",'You got demoted!',QMessageBox.Ok,QMessageBox.Ok)
            if positionNum != 0:
                positionNum -= 1
                if (isRussian):
                    position = 'Вы ' + positions[positionNum]
                    positionProfit = 'Вы зарабатываете ' + str(positionsProfit[positionNum]) + ' РублеКоинов в месяц'
                if (isEnglish):
                    position = 'You are ' + engPositions[positionNum]
                    positionProfit = 'You earn ' + str(positionsProfit[positionNum]) + ' RubleCoins per month'
                profile.profile.setText(position)
                profile.label.setText(positionProfit)


def helpCreator():
    wb.open('https://www.donationalerts.com/r/playman_bs')


def changeMyLanguage():
    changingLanguage = Toplevel()
    changingLanguage.geometry('300x575')
    changingLanguage.resizable(False, False)
    if (isRussian):
        changingLanguage.title('Смена языка')
        chooseNewLanguage = Label(changingLanguage, text='Выберите язык', width=40)
    if (isEnglish):
        changingLanguage.title('Change language')
        chooseNewLanguage = Label(changingLanguage, text='Choose language', width=40)
    changeLanguageRussian = Button(changingLanguage, text='Русский', command=changeMyLanguageRussian)
    changeLanguageEnglish = Button(changingLanguage, text='English', command=changeMyLanguageEnglish)

    chooseNewLanguage.grid(column=0, row=0, padx=5, pady=5, columnspan=2)
    changeLanguageRussian.grid(column=0, row=1, padx=5, pady=5)
    changeLanguageEnglish.grid(column=1, row=1, padx=5, pady=5)

def buySell(buyOrSell):
    global ui
    a=ui.type.currentText()
    if buyOrSell==0:
        if a=='нефть':
            fBuyOil()
        elif a=='хлопок':
            fBuyCotton()
        elif a=='золото':
            fBuyCotton()
    elif buyOrSell==1:
        if a=='нефть':
            fSellOil()
        elif a=='хлопок':
            fSellCotton()
        elif a=='золото':
            fSellCotton()



# Виджеты
ui.end_month.clicked.connect(endThisMonth)
ui.profile.clicked.connect(openMyProfile)
ui.buy.clicked.connect(lambda :buySell(0))
ui.sell.clicked.connect(lambda :buySell(1))
ui.helpTeam.clicked.connect(lambda :helpCreator())
for i in 10,100,1000:
    exec(f'ui._{i}.clicked.connect(lambda :ui.count.setValue(ui.count.value()-{i}))\nui._{i}_.clicked.connect(lambda :ui.count.setValue(ui.count.value()+{i}))')
# Конец программы

window.show()
sys.exit(app.exec_())
