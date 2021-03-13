from tkinter import *
import random
import time
import webbrowser as wb
import tkinter.messagebox as mb
#ВНИМАНИЕ!!! Игра НЕ является доработанной,
#все баги будут исправлятся В БУДУЕЩЕМ!!!

#Делал Mikro, Mikro#5986
import tkinter.simpledialog as s
#Настройки окна

window = Tk()
window.geometry('700x700')
window.title('Деньги и экономия')
window.resizable(True, True)
window.iconphoto(True, PhotoImage(file='../buildMirus/icons.iconset/icon.png'))
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
print('добро пожаловать в "деньги и экономия"! ваша цель - заработать 1 миллиард за 30 лет.')
textOil = 'Цена нефти 60 РублеКоинов за литр'
textCotton = 'Цена хлопка 200 РублеКоинов за килограмм'
textGold = 'Цена золота 30000 РублеКоинов за слиток'
howMoney = 'У вас есть 10000 РублеКоинов'
howManyOilHave = 'У вас есть 0 литров нефти'
howManyCottonHave = 'У вас есть 0 килограмм хлопка'
howManyGoldHave = 'У вас есть 0 слитков золота'
positions = ['Интерн', 'Секретарь', 'Новичок', 'Джуниор', 'Опытный', 'Сениор', 'Специалист', 'Начальник', 'Владелец компании']
engPositions = ['Intern', 'Secretary', 'Newbie', 'Junior', 'Experienced', 'Senior', 'Specialist', 'Chief', 'Owner of company']
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
    global money, buyOil, price, notEnoughMoneyOil, oilPrice, oilHave, howMoney, howManyMoney, howManyOilHave
    howMany = int(buyOil.get())
    price = howMany * oilPrice
    price = int(price)
    money = int(money)
    if (price <= money and howMany >= 1):
        oilHave += howMany
        money -= price
        if (isRussian):
            howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
            howManyOil.config(text = 'У вас есть ' + str(oilHave) + ' литров нефти') 
            notEnoughMoneyOil.config(text = 'Куплено!', fg = '#007011')
        if (isEnglish):
            howMoney = 'You have ' + str(money) + ' RubleCoins'
            howManyOil.config(text = 'You have ' + str(oilHave) + ' liters of oil') 
            notEnoughMoneyOil.config(text = 'Bought!', fg = '#007011')
        howManyMoney.config(text = howMoney)
    else:
        if (isRussian):
            notEnoughMoneyOil.config(text = 'Недостаточно РублеКоинов!', fg = '#ff0000')
        if (isEnglish):
            notEnoughMoneyOil.config(text = 'Not enough RubleCoins!', fg = '#ff0000')

def fSellOil():
    global money, sellOil, price, notEnoughMoneyOil, oilPrice, oilHave, howMoney, howManyMoney, howManyOilHave
    howMany = int(sellOil.get())
    price = howMany * oilPrice
    price = int(price)
    money = int(money)
    if (howMany <= oilHave and howMany > 0):
        oilHave -= howMany
        money += price
        if (isRussian):
            howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
            howManyOil.config(text = 'У вас есть ' + str(oilHave) + ' литров нефти') 
            notEnoughMoneyOil1.config(text = 'Продано!', fg = '#007011')
        if (isEnglish):
            howMoney = 'You have ' + str(money) + ' RubleCoins'
            howManyOil.config(text = 'You have ' + str(oilHave) + ' liters of oil') 
            notEnoughMoneyOil1.config(text = 'Sold!', fg = '#007011')
        howManyMoney.config(text = howMoney)
    else:
        if (isRussian):
            notEnoughMoneyOil1.config(text = 'Недостаточно нефти!', fg = '#ff0000')
        if (isEnglish):
            notEnoughMoneyOil1.config(text = 'Not enough oil!', fg = '#ff0000')
        
def fBuyCotton():
    global money, buyCotton, price, notEnoughMoneyCotton, cottonPrice, cottonHave, howMoney, howManyMoney, howManyCottonHave
    howMany = int(buyCotton.get())
    price = howMany * cottonPrice
    price = int(price)
    money = int(money)
    if (price <= money and howMany >= 1):
        cottonHave += howMany
        money -= price
        if (isRussian):
            howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
            howManyCotton.config(text = 'У вас есть ' + str(cottonHave) + ' килограммов хлопка') 
            notEnoughMoneyCotton.config(text = 'Куплено!', fg = '#007011')
        if (isEnglish):
            howMoney = 'You have ' + str(money) + ' RubleCoins'
            howManyCotton.config(text = 'You have ' + str(cottonHave) + ' kilograms of cotton') 
            notEnoughMoneyCotton.config(text = 'Bought!', fg = '#007011')
        howManyMoney.config(text = howMoney)
    else:
        if (isRussian):
            notEnoughMoneyCotton.config(text = 'Недостаточно РублеКоинов!', fg = '#ff0000')
        if (isEnglish):
            notEnoughMoneyCotton.config(text = 'Not enough RubleCoins!', fg = '#ff0000')

def fSellCotton():
    global money, sellCotton, price, notEnoughMoneyCotton, cottonPrice, cottonHave, howMoney, howManyMoney, howManyCottonHave
    howMany = int(sellCotton.get())
    price = howMany * cottonPrice
    price = int(price)
    money = int(money)
    if (howMany <= cottonHave and howMany > 0):
        cottonHave -= howMany
        money += price
        if (isRussian):
            howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
            howManyCotton.config(text = 'У вас есть ' + str(cottonHave) + ' килограммов хлопка') 
            notEnoughMoneyCotton1.config(text = 'Продано!', fg = '#007011')
        if (isEnglish):
            howMoney = 'You have ' + str(money) + ' RubleCoins'
            howManyCotton.config(text = 'You have ' + str(cottonHave) + ' kilograms of cotton') 
            notEnoughMoneyCotton1.config(text = 'Sold!', fg = '#007011')
        howManyMoney.config(text = howMoney)
    else:
        if (isRussian):
            notEnoughMoneyCotton1.config(text = 'Недостаточно хлопка!', fg = '#ff0000')
        if (isEnglish):
            notEnoughMoneyCotton1.config(text = 'Not enough cotton!', fg = '#ff0000')


def fBuyGold():
    global money, buyGold, price, notEnoughMoneyGold, goldPrice, goldHave, howMoney, howManyMoney, howManyGoldHave
    howMany = int(buyGold.get())
    price = howMany * goldPrice
    price = int(price)
    money = int(money)
    if (price <= money and howMany >= 1):
        goldHave += howMany
        money -= price
        if (isRussian):
            howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
            howManyGold.config(text = 'У вас есть ' + str(goldHave) + ' слитков золота') 
            notEnoughMoneyGold.config(text = 'Куплено!', fg = '#007011')
        if (isEnglish):
            howMoney = 'You have ' + str(money) + ' RubleCoins'
            howManyGold.config(text = 'You have ' + str(goldHave) + ' ingots of gold') 
            notEnoughMoneyGold.config(text = 'Bought!', fg = '#007011')
        howManyMoney.config(text = howMoney)
    else:
        if (isRussian):
            notEnoughMoneyGold.config(text = 'Недостаточно РублеКоинов!', fg = '#ff0000')
        if (isEnglish):
            notEnoughMoneyGold.config(text = 'Not enough RubleCoins!', fg = '#ff0000')

def fSellGold():
    global money, sellGold, price, notEnoughMoneyGold, goldPrice, goldHave, howMoney, howManyMoney, howManyGoldHave
    howMany = int(sellGold.get())
    price = howMany * goldPrice
    price = int(price)
    money = int(money)
    if (howMany <= goldHave and howMany > 0):
        goldHave -= howMany
        money += price
        if (isRussian):
            howMoney = 'У вас есть ' + str(money) + ' РублеКоинов'
            howManyGold.config(text = 'У вас есть ' + str(goldHave) + ' слитков золота') 
            notEnoughMoneyGold1.config(text = 'Продано!', fg = '#007011')
        if (isEnglish):
            howMoney = 'You have ' + str(money) + ' RubleCoins'
            howManyGold.config(text = 'You have ' + str(goldHave) + ' ingots of gold') 
            notEnoughMoneyGold1.config(text = 'Sold!', fg = '#007011')
        howManyMoney.config(text = howMoney)
    else:
        if (isRussian):
            notEnoughMoneyGold1.config(text = 'Недостаточно золота!', fg = '#ff0000')
        if (isEnglish):
            notEnoughMoneyGold1.config(text = 'Not enough gold!', fg = '#ff0000')

def endThisMonth():
    global canDie, isRussian, isEnglish, canGetRice, timeUntilDeath, timeLeft, goldPrice, cottonPrice, oilPrice, whatGoldPrice, whatCottonPrice, whatOilPrice, textOil, textCotton, textGold, money, happiness, aboutHappiness, happinessPerMonth, aboutFit, fitPerMonth, whatToBuyHappiness, whatToBuyFit, whatToBuyHappiness, notEnoughMoneyOil, notEnoughMoneyOil1, notEnoughMoneyCotton, notEnoughMoneyCotton1, notEnoughMoneyGold, notEnoughMoneyGold1
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
    if (isEnglish):
        timeUntilDeathText = str(timeUntilDeath) + ' months left until the end of this game'
        textOil = 'Oil price is ' + str(oilPrice) + ' RubleCoins per liter'
        textCotton = 'Cotton price is ' + str(cottonPrice) + ' RubleCoins per kilogram'
        textGold = 'Gold price is ' + str(goldPrice) + ' RubleCoins per ingot'
        howMoney = 'You have ' + str(money) + ' RubleCoins'
    howManyTimeLive.config(text = timeUntilDeathText)
    whatOilPrice.config(text = textOil)
    whatCottonPrice.config(text = textCotton)
    whatGoldPrice.config(text = textGold)
    howManyMoney.config(text = howMoney)
    canGetRice = 3
    notEnoughMoneyOil.config(text = '')
    notEnoughMoneyOil1.config(text = '')
    notEnoughMoneyCotton.config(text = '')
    notEnoughMoneyCotton1.config(text = '')
    notEnoughMoneyGold.config(text = '')
    notEnoughMoneyGold1.config(text = '')
    buyOil.delete(0, END)
    sellOil.delete(0, END)
    buyCotton.delete(0, END)
    sellCotton.delete(0, END)
    buyGold.delete(0, END)
    sellGold.delete(0, END)
    if timeUntilDeath == 0:
        if canDie == True:
            if (isRussian):
                print('Конец игры! Ваш персонаж умер от старости!')
            if (isEnglish):
                print('Game over! Your character died of old age!')
            endMonth.destroy()
    if money >= 1000000000:
        if (isRussian):
            print('Поздравляем вас! Вы заработали 1 миллиард РублеКоинов менее чем за 30 лет! Вы получили бессмертие!')
        if (isEnglish):
            print('Congratulations! You got 1 billion RubleCoins in less than 30 years! You got immortality!')
        canDie = False

def openMyProfile():
    global whatAboutRice, yourPosition, yourPositionProfit, scaleHappiness, happiness, scaleFit, fit
    profile = Toplevel()
    profile.geometry('300x575')
    profile.resizable(False, False)
    if (isRussian):
        profile.title('Ваш профиль')
        position = 'Вы ' + positions[positionNum]
        positionProfit = 'Вы зарабатываете ' + str(positionsProfit[positionNum]) + ' РублеКоинов в месяц'
        #Профиль
        #Работа
        work = LabelFrame(profile, text = 'Работа')
        yourPosition = Label(work, text = position)
        yourPositionProfit = Label(work, text = positionProfit)
        positionRice = Button(work, text = 'Запросить повышение', command = iNeedRice)
        whatAboutRice = Label(work, text = whatAboutMe)
    if (isEnglish):
        profile.title('Your profile')
        position = 'You are ' + engPositions[positionNum]
        positionProfit = 'You earn ' + str(positionsProfit[positionNum]) + ' RubleCoins per month'
        #Profile
        #Work
        work = LabelFrame(profile, text = 'Work')
        yourPosition = Label(work, text = position)
        yourPositionProfit = Label(work, text = positionProfit)
        positionRice = Button(work, text = 'Require rasing', command = iNeedRice)
        whatAboutRice = Label(work, text = 'You do not require rasing')

    work.grid(column = 0, row = 0, padx = 5, pady = 5)
    yourPosition.grid(column = 0, row = 0, padx = 5, pady = 5)
    yourPositionProfit.grid(column = 0, row = 1, padx = 5, pady = 5)
    positionRice.grid(column = 0, row = 2, padx = 5, pady = 5)
    whatAboutRice.grid(column = 0, row = 3, padx = 5, pady = 5)

def iNeedRice():
    global positionNum, canGetRice
    whatWithMe = random.randint(0, 100)
    if canGetRice == 0:
        if (isRussian):
            whatAboutRice.config(text = 'Вы не можете запросить повышение!', fg = '#ff0000')
        if (isEnglish):
            whatAboutRice.config(text = 'You can not require raising!', fg = '#ff0000')
    if canGetRice > 0:
        canGetRice -= 1
        if whatWithMe < 11:
            if (isRussian):
                whatAboutRice.config(text = 'Вас повысили!', fg = '#00ff48')
            if (isEnglish):
                whatAboutRice.config(text = 'You increased!', fg = '#00ff48')
            if positionNum != 8:
                positionNum += 1
                if (isRussian):
                    position = 'Вы ' + positions[positionNum]
                    positionProfit = 'Вы зарабатываете ' + str(positionsProfit[positionNum]) + ' РублеКоинов в месяц'
                if (isEnglish):
                    position = 'You are ' + engPositions[positionNum]
                    positionProfit = 'You earn ' + str(positionsProfit[positionNum]) + ' RubleCoins per month'
                yourPosition.config(text = position)
                yourPositionProfit.config(text = positionProfit)
        if whatWithMe > 10 and whatWithMe < 76:
            if (isRussian):
                whatAboutRice.config(text = 'Вам отказали!', fg = '#9e9e9e')
            if (isEnglish):
                whatAboutRice.config(text = 'You were denied!', fg = '#9e9e9e')
        if whatWithMe > 75:
            if (isRussian):
                whatAboutRice.config(text = 'Вас понизили!', fg = '#ff0000')
            if (isEnglish):
                whatAboutRice.config(text = 'You got demoted!', fg = '#ff0000')
            if positionNum != 0:
                positionNum -= 1
                if (isRussian):
                    position = 'Вы ' + positions[positionNum]
                    positionProfit = 'Вы зарабатываете ' + str(positionsProfit[positionNum]) + ' РублеКоинов в месяц'
                if (isEnglish):
                    position = 'You are ' + engPositions[positionNum]
                    positionProfit = 'You earn ' + str(positionsProfit[positionNum]) + ' RubleCoins per month'
                yourPosition.config(text = position)
                yourPositionProfit.config(text = positionProfit)

def helpCreator():
    wb.open('https://www.donationalerts.com/r/playman_bs')

def changeMyLanguage():
    changingLanguage = Toplevel()
    changingLanguage.geometry('300x575')
    changingLanguage.resizable(False, False)
    if (isRussian):
        changingLanguage.title('Смена языка')
        chooseNewLanguage = Label(changingLanguage, text = 'Выберите язык', width = 40)
    if (isEnglish):
        changingLanguage.title('Change language')
        chooseNewLanguage = Label(changingLanguage, text = 'Choose language', width = 40)
    changeLanguageRussian = Button(changingLanguage, text = 'Русский', command = changeMyLanguageRussian)
    changeLanguageEnglish = Button(changingLanguage, text = 'English', command = changeMyLanguageEnglish)

    chooseNewLanguage.grid(column = 0, row = 0, padx = 5, pady = 5, columnspan = 2)
    changeLanguageRussian.grid(column = 0, row = 1, padx = 5, pady = 5)
    changeLanguageEnglish.grid(column = 1, row = 1, padx = 5, pady = 5)

def changeMyLanguageRussian():
    global isRussian, isEnglish, changingLanguage
    window.title('Деньги и экономия')
    mainLobby.config(text = 'Главное меню')
    gameLobby.config(text = 'Меню игры')
    gameProcess.config(text = 'Игровой процесс')
    otherThings.config(text = 'Прочее')
    oil.config(text = 'Нефть')
    buyOilText.config(text = 'Купить нефть')
    buyOilButton.config(text = 'Купить')
    sellOilText.config(text = 'Продать нефть')
    sellOilButton.config(text = 'Продать')
    cotton.config(text = 'Хлопок')
    buyCottonText.config(text = 'Купить хлопок')
    buyCottonButton.config(text = 'Купить')
    sellCottonText.config(text = 'Продать хлопок')
    sellCottonButton.config(text = 'Продать')
    gold.config(text = 'Золото')
    buyGoldText.config(text = 'Купить золото')
    buyGoldButton.config(text = 'Купить')
    sellGoldText.config(text = 'Продать золото')
    sellGoldButton.config(text = 'Продать')
    endMonth.config(text = 'Закончить месяц')
    openProfile.config(text = 'Открыть профиль')
    helpTheCreator.config(text = 'Помочь автору')
    changeLanguage.config(text = 'Сменить язык')
    howManyMoney.config(text = 'У вас есть ' + str(money) + ' РублеКоинов')
    whatOilPrice.config(text = 'Цена нефти ' + str(oilPrice) + ' РублеКоинов за литр')
    whatCottonPrice.config(text = 'Цена хлопка ' + str(cottonPrice) + ' РублеКоинов за килограмм')
    whatGoldPrice.config(text = 'Цена золота ' + str(goldPrice) + ' РублеКоинов за слиток')
    howManyOil.config(text = 'У вас есть ' + str(oilHave) + ' литров нефти')
    howManyCotton.config(text = 'У вас есть ' + str(cottonHave) + ' килограмм хлопка')
    howManyGold.config(text = 'У вас есть ' + str(goldHave) + ' слитков золота')
    howManyTimeLive.config(text = 'До конца игры осталось ' + str(timeUntilDeath) + ' месяцев')
    isRussian = True
    isEnglish = False

def changeMyLanguageEnglish():
    global isRussian, isEnglish, changingLanguage
    window.title('Money and economy')
    mainLobby.config(text = 'Main menu')
    gameLobby.config(text = 'Game menu')
    gameProcess.config(text = 'Game process')
    otherThings.config(text = 'Other')
    oil.config(text = 'Oil')
    buyOilText.config(text = 'Buy oil')
    buyOilButton.config(text = 'Buy')
    sellOilText.config(text = 'Sell oil')
    sellOilButton.config(text = 'Sell')
    cotton.config(text = 'Cotton')
    buyCottonText.config(text = 'Buy cotton')
    buyCottonButton.config(text = 'Buy')
    sellCottonText.config(text = 'Sell cotton')
    sellCottonButton.config(text = 'Sell')
    gold.config(text = 'Gold')
    buyGoldText.config(text = 'Buy gold')
    buyGoldButton.config(text = 'Buy')
    sellGoldText.config(text = 'Sell gold')
    sellGoldButton.config(text = 'Sell')
    endMonth.config(text = 'End this month')
    openProfile.config(text = 'Open profile')
    helpTheCreator.config(text = 'Help the creator')
    changeLanguage.config(text = 'Change language')
    howManyMoney.config(text = 'You have ' + str(money) + ' RubleCoins')
    whatOilPrice.config(text = 'Oil price is ' + str(oilPrice) + ' RubleCoins per liter')
    whatCottonPrice.config(text = 'Cotton price is ' + str(cottonPrice) + ' RubleCoins per kilogram')
    whatGoldPrice.config(text = 'Gold price is ' + str(goldPrice) + ' RubleCoins per ingot')
    howManyOil.config(text = 'You have ' + str(oilHave) + ' liters of oil')
    howManyCotton.config(text = 'You have ' + str(cottonHave) + ' kilograms of cotton')
    howManyGold.config(text = 'You have ' + str(goldHave) + ' ingots of gold')
    howManyTimeLive.config(text = str(timeUntilDeath) + ' months left until the end of this game')
    isEnglish = True
    isRussian = False
    
#Виджеты
mainLobby = LabelFrame(text = 'Главное меню', width = 100, height = 100)
gameLobby = LabelFrame(mainLobby, text = 'Меню игры', width = 50, height = 100)
gameProcess = LabelFrame(mainLobby, text = 'Игровой процесс', width = 50, height = 50)
otherThings = LabelFrame(mainLobby, text = 'Прочее', width = 50, height = 50)
#Нефть
oil = LabelFrame(gameLobby, text = 'Нефть')
buyOilText = Label(oil, text = 'Купить нефть')
buyOil = Entry(oil)
buyOilButton = Button(oil, text = 'Купить', command = fBuyOil)
notEnoughMoneyOil = Label(oil, text = '')
sellOilText = Label(oil, text = 'Продать нефть')
sellOil = Entry(oil)
sellOilButton = Button(oil, text = 'Продать', command = fSellOil)
notEnoughMoneyOil1 = Label(oil, text = '')
#Хлопок
cotton = LabelFrame(gameLobby, text = 'Хлопок')
buyCottonText = Label(cotton, text = 'Купить хлопок')
buyCotton = Entry(cotton)
buyCottonButton = Button(cotton, text = 'Купить', command = fBuyCotton)
notEnoughMoneyCotton = Label(cotton, text = '')
sellCottonText = Label(cotton, text = 'Продать хлопок')
sellCotton = Entry(cotton)
sellCottonButton = Button(cotton, text = 'Продать', command = fSellCotton)
notEnoughMoneyCotton1 = Label(cotton, text = '')
#Золото
gold = LabelFrame(gameLobby, text = 'Золото')
buyGoldText = Label(gold, text = 'Купить золото')
buyGold = Entry(gold)
buyGoldButton = Button(gold, text = 'Купить', command = fBuyGold)
notEnoughMoneyGold = Label(gold, text = '')
sellGoldText = Label(gold, text = 'Продать золото')
sellGold = Entry(gold)
sellGoldButton = Button(gold, text = 'Продать', command = fSellGold)
notEnoughMoneyGold1 = Label(gold, text = '')
#Игровой процесс
endMonth = Button(gameProcess, text = 'Закончить месяц', command = endThisMonth)
howManyMoney = Label(gameProcess, text = howMoney)
whatOilPrice = Label(gameProcess, text = textOil, fg = '#ff002b')
whatCottonPrice = Label(gameProcess, text = textCotton, fg = '#ff002b')
whatGoldPrice = Label(gameProcess, text = textGold, fg = '#ff002b')
howManyOil = Label(gameProcess, text = howManyOilHave, fg = '#4d9e62')
howManyCotton = Label(gameProcess, text = howManyCottonHave, fg = '#4d9e62')
howManyGold = Label(gameProcess, text = howManyGoldHave, fg = '#4d9e62')
howManyTimeLive = Label(gameProcess, text = timeUntilDeathText, fg = '#8480ff')
openProfile = Button(gameProcess, text = 'Открыть профиль', command = openMyProfile)
#Прочее
helpTheCreator = Button(otherThings, text = 'Помочь автору', command = helpCreator)
changeLanguage = Button(otherThings, text = 'Сменить язык', command = changeMyLanguage)

mainLobby.pack()
gameLobby.grid(column = 1, row = 0, padx = 10, pady = 10, rowspan = 2)
gameProcess.grid(column = 0, row = 0, padx = 10, pady = 10)
otherThings.grid(column = 0, row = 1, padx = 10, pady = 10)
oil.grid(column = 0, row = 0, padx = 10, pady = 10)
buyOilText.grid(column = 0, row = 0, padx = 5, pady = 5)
buyOil.grid(column = 1, row = 0, padx = 5, pady = 5)
buyOilButton.grid(column = 1, row = 1, padx = 5, pady = 5)
notEnoughMoneyOil.grid(column = 0, row = 1, padx = 5, pady = 5)
sellOilText.grid(column = 0, row = 2, padx = 5, pady = 5)
sellOil.grid(column = 1, row = 2, padx = 5, pady = 5)
sellOilButton.grid(column = 1, row = 4, padx = 5, pady = 5)
notEnoughMoneyOil1.grid(column = 0, row = 4, padx = 5, pady = 5)
cotton.grid(column = 0, row = 1, padx = 10, pady = 10)
buyCottonText.grid(column = 0, row = 0, padx = 5, pady = 5)
buyCotton.grid(column = 1, row = 0, padx = 5, pady = 5)
buyCottonButton.grid(column = 1, row = 1, padx = 5, pady = 5)
notEnoughMoneyCotton.grid(column = 0, row = 1, padx = 5, pady = 5)
sellCottonText.grid(column = 0, row = 2, padx = 5, pady = 5)
sellCotton.grid(column = 1, row = 2, padx = 5, pady = 5)
sellCottonButton.grid(column = 1, row = 4, padx = 5, pady = 5)
notEnoughMoneyCotton1.grid(column = 0, row = 4, padx = 5, pady = 5)
gold.grid(column = 0, row = 2, padx = 10, pady = 10)
buyGoldText.grid(column = 0, row = 0, padx = 5, pady = 5)
buyGold.grid(column = 1, row = 0, padx = 5, pady = 5)
buyGoldButton.grid(column = 1, row = 1, padx = 5, pady = 5)
notEnoughMoneyGold.grid(column = 0, row = 1, padx = 5, pady = 5)
sellGoldText.grid(column = 0, row = 2, padx = 5, pady = 5)
sellGold.grid(column = 1, row = 2, padx = 5, pady = 5)
sellGoldButton.grid(column = 1, row = 4, padx = 5, pady = 5)
notEnoughMoneyGold1.grid(column = 0, row = 4, padx = 5, pady = 5)
endMonth.grid(column = 0, row = 0, padx = 5, pady = 5)
howManyMoney.grid(column = 0, row = 1, padx = 5, pady = 5)
whatOilPrice.grid(column = 0, row = 2, padx = 5, pady = 5)
whatCottonPrice.grid(column = 0, row = 3, padx = 5, pady = 5)
whatGoldPrice.grid(column = 0, row = 4, padx = 5, pady = 5)
howManyOil.grid(column = 0, row = 5, padx = 5, pady = 5)
howManyCotton.grid(column = 0, row = 6, padx = 5, pady = 5)
howManyGold.grid(column = 0, row = 7, padx = 5, pady = 5)
howManyTimeLive.grid(column = 0, row = 8, padx = 5, pady = 5)
openProfile.grid(column = 0, row = 9, padx = 5, pady = 5)
helpTheCreator.grid(column = 0, row = 0, padx = 5, pady = 5)
changeLanguage.grid(column = 0, row = 1, padx = 5, pady = 5)

#Конец программы

window.mainloop()
