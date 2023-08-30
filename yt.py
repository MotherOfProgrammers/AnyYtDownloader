# Created By Anon
import os
from pytube import YouTube
import sys
import platform


def sysint():
	try:
		print("""
     		==================================
     		=  YT VIDEO DOWNLOADER  => ANON  =
        	==================================
		""")
		link = str(input("[ENTER] Enter Your Link: "))
		lnk = YouTube(link)
		title = lnk.title
		print(f"[INFO] Video Title: {title}")
		stream = lnk.streams.get_highest_resolution()
		print("[+] Downloading...")
		stream.download()
		print("[INFO] Download Success!")
	except:
		print("[ERROR] Download Error!")


print("[+] Checking Updates...")
print("[+] Upgrading...")
sysi = platform.system()
os.system("pip3 install pytube")

if sysi == 'Linux':
        os.system('clear')
        sysint()
elif sysi == 'Windows':
        os.system('cls')
        sysint()
else:
        print(f"{sysi} Is Not Supportable For This")
        sys.exit()
