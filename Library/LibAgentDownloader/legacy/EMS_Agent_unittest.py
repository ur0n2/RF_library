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







