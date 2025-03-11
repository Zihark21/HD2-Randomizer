import subprocess, shutil, sys, os

if os.path.exists('HD2'):
    shutil.rmtree('HD2')

if os.path.exists('HD2.zip'):
    os.remove('HD2.zip')

subprocess.run([sys.executable, 'cx_setup.py', 'build'])
shutil.make_archive("HD2", 'zip', "HD2")