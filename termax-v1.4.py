import os

#STOP LOOKING AT MY CODE YOU CREEP qwq

os.system("clear")

print('''
 TERMAX v1.4 by Max-0800
''')

hostdir = "/sys/devices/system/cpu/cpufreq/policy"
cluster1 = "/sys/devices/system/cpu/cpufreq/policy0"
for cnum in range(1,9):
	if os.path.isdir(f"{hostdir}{cnum}") == True:
		cluster2 = f"{hostdir}{cnum}"
		break

def main():
	global hostdir
	global cluster1
	global cluster2
	tmx = input("/Admin/:> ")
	xvar = tmx[8:]
	
	#CPU Changing statements
	if "cpu -cm1" in tmx:
		os.system(f"echo '{xvar}' > {cluster1}/scaling_max_freq")
		print("Operation success.")
	elif "cpu -cm2" in tmx:
		os.system(f"echo '{xvar}' > {cluster2}/scaling_max_freq")
		print("Operation success.")
		
	#GPU Changing statements
	if "cpu -gm1" in tmx:
		os.system(f"echo '{xvar}' > {cluster1}/scaling_governor")
		print("Operation succes.")
	elif "cpu -gm2" in tmx:
		os.system(f"echo '{xvar}' > {cluster2}/scaling_governor")
		print("Operationg success.")
	
	#Informational statements
	if tmx == "cpu -C":
		print()
		print("Cluster 1")
		os.system(f"cat {cluster1}/scaling_available_frequencies")
		os.system(f"cat {cluster1}/scaling_available_governors")
		print()
		print("Cluster 2")
		os.system(f"cat {cluster2}/scaling_available_frequencies")
		os.system(f"cat {cluster2}/scaling_available_governors")
		print()
	elif tmx == "cpu -si":
		print()
		print("Cluster 1 current state")
		os.system(f"cat {cluster1}/scaling_max_freq")
		os.system(f"cat {cluster1}/scaling_governor")
		print()
		print("Cluster 2 current state")
		os.system(f"cat {cluster2}/scaling_max_freq")
		os.system(f"cat {cluster2}/scaling_governor")
		print()
	
	if tmx == "adb -RB":
		os.system("sudo reboot")
	
	if tmx == "help":
		print("Commands")
		print('''
cpu -cm1 <num>       sets desired clock speed to cluster 1
cpu -cm2 <num>       sets desired clock speed to cluster 2
cpu -gm1 <gov>       sets desired governor to cluster 1
cpu -gm2 <gov>       sets desired governor to cluster 2
cpu -si              shows current CPU clock speed and CPU governor
cpu -C               shows available CPU clock speeds
adb -RB              reboots device''')
	elif tmx == "cls":
		os.system("clear")

#Loopback
while True:
	main()