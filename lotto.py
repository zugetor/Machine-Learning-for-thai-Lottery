from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.read_csv('thLotto_49-59.csv')
day = list(zip(data['day'],data['month'],data['year']))
first = data['first']
digit3 = data['3digit']
last_2digit_top = data['last_2digit_top']
first_3digit_1 = data['first_3digit_1']
first_3digit_2 = data['first_3digit_2']
last_3digit_1 = data['last_3digit_1']
last_3digit_2 = data['last_3digit_2']
last_2digit_down = data['last_2digit_down']
iD = int(input("Day: "))
iM = int(input("Month: "))
iY = int(input("Year: "))

def perdictLotto(d,m,y,data1,data2):
	model = LinearRegression()
	model.fit(data1,data2)
	predict = model.predict([[d,m,y]])
	return predict[0]
	
print("\nFirst: %06d"%perdictLotto(iD,iM,iY,day,first))
print("Three digit: %03d"%perdictLotto(iD,iM,iY,day,digit3))
print("The first three digits: %03d"%perdictLotto(iD,iM,iY,day,first_3digit_1))
print("                        %03d"%perdictLotto(iD,iM,iY,day,first_3digit_2))
print("The last three digits:  %03d"%perdictLotto(iD,iM,iY,day,last_3digit_1))
print("                        %03d"%perdictLotto(iD,iM,iY,day,last_3digit_2))
print("Two digits:    %02d"%perdictLotto(iD,iM,iY,day,last_2digit_top))
print("               %02d"%perdictLotto(iD,iM,iY,day,last_2digit_down))