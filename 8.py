def schet (user_choice,number):
	k = ''	
	if (user_choice == 2) or (user_choice == 8):
		while number>0:
			k = str(number%user_choice) + k
			number//=user_choice
		print (k)
	else:
		print("Ошибка!")
print ("Вы можете выбрать двоичную или восьмеричную систему счисления")
try:
	schet ((int(input("Введите систему счисления: "))),(int(input("Введите число: "))))	
except:
	print ("Ошибка!")