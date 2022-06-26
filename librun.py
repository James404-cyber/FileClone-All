import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Fil32")._site_view_()
elif 'aarch' in arc:
	__import__("Fil")._site_view_()
else:
	exit(f' Unknow device machine {arc}')
