import os

#STOP LOOKING AT MY CODE YOU CREEP qwq
#update started on 02/20/2022

os.system("clear")

print('''
 Termax Optical
 v1.52
 by Max-0800
''')

hostdir = "/sys/devices/system/cpu/cpufreq/policy"
cluster1 = "/sys/devices/system/cpu/cpufreq/policy0"
for cnum in range(1,9):
	if os.path.isdir(f"{hostdir}{cnum}") == True:
		cluster2 = f"{hostdir}{cnum}"
		break

igpu = "/sys/kernel/gpu"

def main():
	global hostdir
	global cluster1
	global cluster2
	global igpu
	tmx = input("/Admin/:> ")
	xvar = tmx[9:]
	
	#CPU changing statements
	if "cpu -cm1 " in tmx:
		os.system(f"echo '{xvar}' > {cluster1}/scaling_max_freq")
		print("Operation success.")
	elif "cpu -cm2 " in tmx:
		os.system(f"echo '{xvar}' > {cluster2}/scaling_max_freq")
		print("Operation success.")
		
	#CPU governor changing statements
	if "cpu -gm1 " in tmx:
		os.system(f"echo '{xvar}' > {cluster1}/scaling_governor")
		print("Operation succes.")
	elif "cpu -gm2 " in tmx:
		os.system(f"echo '{xvar}' > {cluster2}/scaling_governor")
		print("Operationg success.")
	
	#iGPU changing statements
	if "gpu -clk " in tmx:
		os.system(f"echo '{xvar}' > {igpu}/gpu_max_clock")
		print(f"iGPU has been clocked to {xvar}-Mhz")
	elif "gpu -gov " in tmx:
		os.system(f"echo '{xvar}' > {igpu}/gpu_governor")
		print(f"iGPU governor has been set to {xvar}")
	
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
	if tmx == "gpu -C":
		print()
		print("iGPU available clock speeds and governors")
		os.system(f"cat {igpu}/gpu_freq_table")
		os.system(f"cat {igpu}/gpu_available_governor")
	elif tmx == "gpu -si":
		print()
		print("iGPU current state")
		os.system(f"cat {igpu}/gpu_max_clock")
		os.system(f"cat {igpu}/gpu_governor")
	
	#Miscellaneous
	if tmx == "sudo reboot":
		os.system("sudo reboot")
	elif tmx == "clear cache":
		os.system("rm -rf storage/elumated/0/Android/data/*/cache /data/data/*/cache")
		print("cache cleared")
	
	if tmx == "help":
		print("Commands")
		print('''
	≡Setting≡
gpu -clk <num>		sets desired clock speed to the integrated graphics unit
gpu -gov <gov>		sets desired governor to the graphics unit
cpu -cm1 <num>		sets desired clock speed to cluster 1
cpu -cm2 <num>		sets desired clock speed to cluster 2
cpu -gm1 <gov>		sets desired governor to cluster 1
cpu -gm2 <gov>		sets desired governor to cluster 2

	≡Informational≡
gpu -si			shows current GPU clock speed and GPU governor
gpu -C			shows available GPU clock speeds
cpu -si			shows current CPU clock speed and CPU governor
cpu -C			shows available CPU clock speeds

	≡Miscellaneous≡
sudo reboot		reboots device
clear cache		clears all cache
cls			clears the screen''')
	elif tmx == "cls":
		os.system("clear")

#Loopback
while True:
	main()