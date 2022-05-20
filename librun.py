import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("file32").mn()
elif 'aarch' in arc:
	__import__("Filegood").mn()
else:
	exit(f' Unknow device machine {arc}')
