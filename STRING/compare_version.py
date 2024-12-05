def compareVersion(version1, version2):
        
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]

        vv_1 = 0
        vv_2 = 0

        for x in range(max(len(v1),len(v2))):

            if x < len(v1):
                vv_1 = v1[x]
            else:
                vv_1 = 0

            if x < len(v2):
                vv_2 = v2[x]
            else:
                vv_2 = 0

            if vv_1 > vv_2:
                return 1
            elif vv_1 < vv_2:
                return -1

        return 0        

version1 = "1.2"
version2 = "1.10"
res = compareVersion(version1,version2)
print(res)