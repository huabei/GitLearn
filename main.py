import os
import subprocess

if __name__ == "__main__":  
    os.chdir(r"E:\Python_Project\GitLearn")
    subprocess.call([r"D:\Program Files\SmartGit\git\bin\git.exe", 'commit', '-a', '-m', '"today update"'])    
    subprocess.call([r'D:\Program Files\SmartGit\git\bin\git.exe', 'push'])
    