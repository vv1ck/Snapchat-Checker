try:
	from requests import post,get
	import random,requests,sys,time
	from threading import Thread,Lock
except Exception as Joker:exit(input(Joker))
def slow(M):
	for c in M + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1. / 60)
def SeveUSERS(Target):
	with open('New-SnapUser.txt', 'a') as J:
		J.write(Target+'\n')
def SeveUSERSD(Target):
	with open('DELETED-SnapUser.txt', 'a') as J:
		J.write(f'[DELETED Or available :@{Target}]\n')
class RUN_Checker:
	def __init__(self):
		self.proxylist=[]
		self.TOKEN=''
		self.IDS=''
		self.runs=True;self.prnt=Lock()
		self.Ymth,self.Nmth,self.Err,self.Dl=0,0,0,0
		self.Modes=input("""Mdoe:
1) Checked through the usernames file
2) Random check (create random usernames and check them) 
Enter : """)
		if self.Modes=='1':
			try:
				self.file=open(input('\n[$] ->> Enter name file (Username) : '),'r')
			except FileNotFoundError:input('\n[!!] Invalid filename, please try again ..\n');return RUN_Checker()
		elif self.Modes=='2':
			try:
				self.let=int(input('[+] Enter the number of characters for the username [ 3 / 4 / 5 ] : '))
			except ValueError:input('[!] Please enter a number, not a letter ..');return RUN_Checker()
		try:self.proxy =  open(input('\n[$] ->> Enter name file (Proxy) : '),'r').read().splitlines()
		except FileNotFoundError:input('\n[!!] Invalid filename, please try again ..\n');return RUN_Checker()
		try:self.trt=int(input('[+] Enter Thread : '))
		except ValueError:input('[!] Please enter a number, not a letter ..');return RUN_Checker()
		tele=input('\n[?] Sent To Telegram ? [ y / n ]')
		if tele=='y':
			try:
				Users=open('IDS_TELEGRAM.txt', 'r').read().splitlines()
				self.TOKEN=Users[0]
				self.IDS=Users[1]
			except IndexError:pass
			except FileNotFoundError:
				self.TOKEN=input('[+] Enter TokenBot: ')
				self.IDS = input('[+] Enter Your ID: ')
				with open('IDS_TELEGRAM.txt', 'a') as J:J.write(f'{self.TOKEN}\n{self.IDS}\n')
		slow('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		Thread(target=self.PRNT).start()
		self.TRET()
	def PRNT(self):
		while self.prnt:
			print(f'\r available :{self.Ymth} ,DELETED Or available:{self.Dl} , Not available:{self.Nmth} , Bad Proxy:{self.Err} | Users: \r',end="")
	def CheckSnap2(self,Target):
		run = str(random.choice(self.proxylist))
		try:
			PROXY =  {
					"http": f"http://{run}",
					"https": f"http://{run}"}
			Checks=post("https://app.snapchat.com/loq/suggest_username_v3",headers={"User-Agent": "Snapchat/10.25.0.0 (Agile_Client_Error; Android 6.2.0#503792501#11; gzip)","allow-recycled-username": "true","allow-recycled-username": "True"},data={"requested_username": Target},proxies=PROXY,timeout=3)
			if ('"status_code":"TAKEN"' in Checks.text):
				self.Nmth+=1
			elif ('"status_code":"INVALID_BEGIN"' in Checks.text):self.Nmth+=1
			elif ('"status_code":"DELETED"' in Checks.text):
				self.Dl+=1
				SeveUSERSD(Target)
			elif ('"status_code":"OK"'in Checks.text):
				self.Ymth+=1
				SeveUSERS(Target)
				get(f'https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={self.IDS}&text=[+] user Snap >> [ @{Target} ]')
			elif (Checks.status_code==403):
				self.Err+=1
			elif (Checks.status_code==429):
				self.Err+=1
				self.CheckSnap2(Target)
			else:self.Nmth+=1
		except KeyboardInterrupt:
			self.runs=False
		except KeyError:self.Err+=1
		except UnicodeEncodeError:self.Err+=1
		except IndexError:self.Err+=1
		except requests.exceptions.ConnectionError:
			self.Err+=1
			self.CheckSnap2(Target)
		except requests.exceptions.ReadTimeout:
			self.Err+=1
			self.CheckSnap2(Target)
		except requests.exceptions.ChunkedEncodingError:
			self.Err+=1
			self.CheckSnap2(Target)
	
	def CheckSnap(self):
		while self.runs:
			run = str(random.choice(self.proxylist))
			if self.Modes=='1':
				Target =self.file.readline().split('\n')[0]
				if Target=='':
					self.runs=False
					#self.prnt=False
					sys.exit()
			elif self.Modes=='2':
				Target = str(''.join((random.choice('qazwsxedcrfv_tgbyhnujmn-ujmiklop6asf9bro7vwo4nqp3ngoebb0nepf5pfbsli8pqnfpgapz') for i in range(self.let))))
			try:
				PROXY =  {
						"http": f"http://{run}",
						"https": f"http://{run}"}
				Checks=post("https://app.snapchat.com/loq/suggest_username_v3",headers={"User-Agent": "Snapchat/10.25.0.0 (Agile_Client_Error; Android 6.2.0#503792501#11; gzip)"},data={"requested_username": Target},proxies=PROXY,timeout=3)
				if ('"status_code":"TAKEN"' in Checks.text):
					self.Nmth+=1
				elif ('"status_code":"INVALID_BEGIN"' in Checks.text):self.Nmth+=1
				elif ('"status_code":"DELETED"' in Checks.text):
					self.Dl+=1
					SeveUSERSD(Target)
				elif ('"status_code":"OK"'in Checks.text):
					self.Ymth+=1
					SeveUSERS(Target)
					get(f'https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={self.IDS}&text=[+] user Snap >> [ @{Target} ]')
				elif (Checks.status_code==403):
					self.Err+=1
				elif (Checks.status_code==429):
					self.Err+=1
					self.CheckSnap2(Target)
				else:self.Nmth+=1
			except KeyboardInterrupt:
				self.runs=False
			except KeyError:self.Err+=1
			except UnicodeEncodeError:self.Err+=1
			except IndexError:self.Err+=1
			except requests.exceptions.ConnectionError:
				self.Err+=1
				self.CheckSnap2(Target)
			except requests.exceptions.ReadTimeout:
				self.Err+=1
				self.CheckSnap2(Target)
			except requests.exceptions.ChunkedEncodingError:
				self.Err+=1
				self.CheckSnap2(Target)
			
	def TRET(self):
		theards =[]
		for pro in self.proxy:
			self.proxylist.append(pro)
		for i in range(self.trt):
			trts = Thread(target=self.CheckSnap)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
		self.prnt=False
		input('\n->> Mission finished, press Enter to exit ...')
print("""
┈┈┈┈╱▔▔╲
┈┈┈┈▏┈┈▕ SnapChat Checker V3
┈┈┈┈╲┈┈╱▂▂▂▂
╱▔▔╲╱┈┈┈╱▔╲▏╲
▏┈┈┈┈┈▂▂▏╭╮╭╮▏╭╮
╲▂▂╱▏╱╭╮╲┊▋┊▋╱╰╯
┈┈┈┈╲▏▕▏┈┈┈┈▔┈▕  By Joker *_*
┈┈┈┈┈╲┈╲▂▂▂▂▂▂╱   IG: @221298
┈┈┈┈┈┈▔╲╰━╯╱
┈┈┈┈┈┈┈┈▔""")
RUN_Checker()
