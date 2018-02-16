#Coded by LeeJunHwan
import urllib
import os
import sys


class EMS_Agent():
	ROBOT_LIBRARY_DOC_FORMAT = 'rest'
	def agent_download(self, host_ip, agent_name):
		"""
		*EMS AGENT DOWNLOADER* by *LeeJunHwan.*
		--------   
		
		def agent_download(self, host_ip, agent_name)  
		--------						
		Just Download to EMS Agent for MyPC Auto.
		
		URL Example: http://192.168.4.11/apc/AgentInstall/mypcautoSetup.exe
		"""
		agent_download_url = "http://" + host_ip + "/apc/AgentInstall/" + agent_name + "Setup.exe"
		agent_download_path = "D:\\" + agent_name + "Setup.exe"
		agent_full_path = urllib.urlretrieve(agent_download_url, agent_download_path)	
		agent_file_size = os.path.getsize(agent_full_path[0])
		print("[+] " + agent_download_url)
		print("[*] " + str(int(agent_file_size)) + "Byte")			
		
		if (agent_file_size > 10000): # 1KB
			return True
		else:
			return False

	def apcconsole_force_terminate(self):
		"""
		APCConsole.exe Enforce Terminate .
		"""
		for i in xrange(5):
			os.system("taskkill /f /im apcconsole.exe")


class Years_Manipulate():		  
	ROBOT_LIBRARY_DOC_FORMAT = 'rest'
	def years_manipulate(self, period):
		"""
		----------
		def years_manipulate(self, period):
		----------
		Windows local years manipulate with powershell commands.
		Example:
			   years_manipulate(-3)
			   years_manipulate(5)
		"""
		period = str(period)
		years_manipulate_cmd = "powershell -c set-date (get-date).addyears(" + period + ")"		
		years_manipulate_cmd_result = os.system(years_manipulate_cmd)
		print(years_manipulate_cmd)
		if (years_manipulate_cmd_result):
			return False
		else:
			return True


if __name__ == "__main__":
	ll = Years_Manipulate()
	inst = ll.years_manipulate(-9)
	print(inst)
	inst = ll.years_manipulate(27)
	print(inst)
	
	  
	"""
	  print("[+] Hello, this is EMS agent Library By LeeJunHwan.")
	if (len(sys.argv) >= 2):
		host_ip = sys.argv[1]
	else:
		host_ip = "192.168.4.11"
	agent_name = "mypcauto"

	lollol = EMS_Agent()
	if (lollol.agent_download(host_ip, agent_name)):
		print("[+] Download Success.")
	else:
		print("[-] Download Fail.")

	  """

