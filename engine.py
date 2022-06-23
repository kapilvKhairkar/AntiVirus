import hashlib
import os
def sha_hash(file_name):
    try:
        f = open(file_name,"rb")
        bytes = f.read()
        shahashes = hashlib.sha256(bytes).hexdigest()
        f.close()
        return shahashes
    except Exception as e:
        return e

def malware_checker(pathofFile):
    hash_malware_check =sha_hash(pathofFile)
    malware_hashes = open("virusHash.unibit", "r").read().split("\n")
    #malware_hashes = open("virusHash.unibit","r").readlines() ALSO APPEND \N AT END
    virus_Info = open("virusinfo.unibit", "r").read().split("\n")

    for i in malware_hashes:
        if i == hash_malware_check:
            return virus_Info[malware_hashes.index(i)]
    return 0
virusName = list()
virusPath = list()
def virusScanner(path):
    dir_list = list()
    for (dirpath,dirname,filename) in os.walk(path):
        dir_list += [os.path.join(dirpath,file) for file in filename]

    for i in dir_list:
        print(i)
        if malware_checker(i) != 0:
            virusName.append(malware_checker(i) + " ::FILE:: " + i)
            virusPath.append(i)

def virusRemover(path):
    virusScanner(path)
    if virusPath:
        for i in virusPath:
            os.remove(i)
    else:
        return 0


def junkRemover():
    username = os.environ.get('USERNAME').upper().split(" ")
    temp_list = list()
    for (dirpath, dirname, filename) in os.walk("C:\\Windows\\Temp"):
        temp_list += [os.path.join(dirpath, file) for file in filename]
        temp_list += [os.path.join(dirpath, file) for file in dirname]
    for (dirpath, dirname, filename) in os.walk(f"C:\\User\\{username}\\AppData\\Local\\Temp"):
        temp_list += [os.path.join(dirpath, file) for file in filename]
        temp_list += [os.path.join(dirpath, file) for file in dirname]
    for (dirpath, dirname, filename) in os.walk("C:\\Windows\\Prefetch"):
        temp_list += [os.path.join(dirpath, file) for file in filename]
        temp_list += [os.path.join(dirpath, file) for file in dirname]

    if temp_list:
        for i in temp_list:
            try:
                os.remove(i)
            except Exception as e:
                return e
            try:
                os.rmdir(i)
            except Exception as e:
                return e
    else:
        return 0
"""
def ramBooster():
    task = list()# should be in exe format
    for i in task:
        try:
            os.system(f"taskkill /f /in {i}")
        except Exception as e:
            return e
            
"""
#junkRemover()


