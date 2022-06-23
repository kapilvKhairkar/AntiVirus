f  = open("VirusDataBaseHash.bav","r").readlines()
for i in f:
    f1 = open("virusHash.unibit", "a").writelines(i[0:64] + "\n")
    f2 = open("virusinfo.unibit", "a").writelines(i[65:])

