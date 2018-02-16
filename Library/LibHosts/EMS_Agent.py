#Coded by LeeJunHwan
import urllib
import os
import sys


class EMS_Agent():
	ROBOT_LIBRARY_DOC_FORMAT = 'rest'
	
	def __init__(self):
		self.hosts_instance = Hosts_Inspect()

				
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


	def hosts_vuln(self):
		return self.hosts_instance.hosts_vuln_write()

	def hosts_safe(self):
		return self.hosts_instance.hosts_safe_write()
	def hosts_test(self):
		return self.hosts_instance.hosts_test()
				

class Hosts_Inspect():
	def hosts_vuln_write(self):
		with open("C:\\windows\\system32\\drivers\\etc\\hosts", "w") as f:
			f.write("127.0.0.3 naver.com")
			return f

	def hosts_safe_write(self):
		with open("C:\\windows\\system32\\drivers\\etc\\hosts", "w") as f:
			f.write("")
			return f
	def hosts_test(self):
		with open("c:\\hosts","w") as f:
			f.write("hosts test")
			return f
				


if __name__ == "__main__":
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



