#Coded by LeeJunHwan
import urllib
import os
import sys
import unittest


class EMS_Agent():
	def agent_download(self, host_ip, agent_name):
		#url_ex; http://192.168.4.11 /apc/AgentInstall/mypcautoSetup.exe
		agent_download_url = "http://" + host_ip + "/apc/AgentInstall/" + agent_name + "Setup.exe"
		agent_download_path = "D:\\" + agent_name + "Setup.exe"
		try:
			agent_full_path = urllib.urlretrieve(agent_download_url, agent_download_path)
		except IOError:
			return False

		agent_file_size = os.path.getsize(agent_full_path[0])
		print("\n[+] " + agent_download_url)
		print("[*] " + str(int(agent_file_size)) + "Byte")
		if (agent_file_size > 10000): # 1KB
			return True
		else:
			return False


class EMS_Agent_Testunit(unittest.TestCase):
    def test001(self):
        test001 = EMS_Agent()
        c = test001.agent_download("192.168.4.11", "mypcauto")
        self.assertTrue(c)
    def test002(self):
        test002 = EMS_Agent()
        c = test002.agent_download("192.168.123.123", "mypcauto")
        self.assertFalse(c)
    def test003(self):
        test003 = EMS_Agent()
        c = test003.agent_download("192.168.4.11", "mypcauto123")
        self.assertFalse(c)





if __name__ == '__main__':
    print("[+] EMS agent Library By LeeJunHwan.")
    suite = unittest.TestLoader().loadTestsFromTestCase(EMS_Agent_Testunit)
    unittest.TextTestRunner(verbosity=2).run(suite)



"""

#Coded by LeeJunHwan
import urllib
import os
import sys
import unittest
import EMS_Agent


class EMS_Agent_Testunit(unittest.TestCase):
    def test001(self):
        test001 = EMS_Agent.EMS_Agent()
        self.assertTrue(test001.agent_download("192.168.4.11", "mypcauto"))



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(EMS_Agent_Testunit)
    unittest.TextTestRunner(verbosity=2).run(suite)



import EMS_Agent
import sys


print("[+] Hello, this is EMS agent Library By LeeJunHwan.")
print("[+] Test Cases Start")
agent_name = "mypcauto"
host_ip = "192.168.4.12"
lollol = EMS_Agent.EMS_Agent()

print("\n[+] Test Case1")
if (lollol.agent_download(host_ip, agent_name)):
	print("[+] Download Success.\n[+] Test Case1 Pass")
else:
	print("[-] Download Fail.\n[+] Test Case1 Fail")

print("\n[+] Test Case2")
if (len(sys.argv) >= 2):
	host_ip = sys.argv[1]
else:
	host_ip = "192.168.4.11"
if (lollol.agent_download(host_ip, agent_name)):
	print("[+] Download Success.\n[+] Test Case2 Pass")
else:
	print("[-] Download Fail.\n[+] Test Case2 Fail")

print
"""