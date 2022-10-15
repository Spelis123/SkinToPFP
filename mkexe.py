import os
curdir = input("DIR:")
command = 'cmd /k "cd ' + curdir + ' & pyinstaller -w -F -n'+ "SkinStealer.exe" + ' Run.pyw"'
print(command)
os.system(command)