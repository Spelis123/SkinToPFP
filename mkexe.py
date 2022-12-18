import os
curdir = os.getcwd()
command = 'cmd /k "cd ' + curdir + ' & pip install -r constraints.txt & pyinstaller -w -F -n'+ "SkinStealer.exe" + ' Run.pyw"'
os.system(command)