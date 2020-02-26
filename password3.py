# password3
# password3
# Password重試程式
# 先在程式碼中 設定好passwoed='a123456'
# 讓使用者最多輸入3次密碼
# 不對的話就印出'密碼失敗'
# 對的話就印出'登入成功'
# 三次時顯示'帳號已經鎖定'
p = 'a123456'
c = 0
while True:
	pa = input ('請輸入密碼')
	if pa == p :
		print ('登入成功')
		break
	else:
		print ('登入失敗 請重新輸入')
		c = c + 1
		if c == 3:
			print ('帳號已經鎖定')
			break


    

c = c + 1
