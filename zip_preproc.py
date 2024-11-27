from zipfile import ZipFile
import os
import json
import pprint

def create_dict(archv, dict, list_path, indx = 0):
    if indx < len(list_path) - 1:
        if not(list_path[indx] in dict.keys()):
            dict[list_path[indx]] = {}
        return create_dict(archv, dict[list_path[indx]], list_path, indx+1)
    else:
        names = archv.namelist()
        for name in names:
            if name.endswith(list_path[indx]) and not('MACOSX' in name):
                print()
                with archv.open(name, 'r') as file:
                    dict[list_path[indx]] = file.read().decode('utf8') # Переделать
        return dict

    

filename = '2020.2-Anunbis-develop.zip'
archieve = ZipFile(filename, mode='r')
filelist = []
Dict_path = {}

for item in archieve.infolist():
    fname = item.filename

    if fname[-1] != '/' and not('MACOSX' in fname) :

        if fname.endswith('py'):
            with archieve.open(fname, 'r') as file:
                #print(str(file.read()))
                pass


        filelist.append(list(fname.split('/')))

for item in filelist:
    create_dict(archieve, Dict_path, item)

st = set()
for item in filelist:
    end_s = list(item[-1].split('.'))[-1]
    st.add(end_s)

#'json', 'lock', 'png'
print(st)
pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(Dict_path)


with open('PreprocData.json', 'w') as file:
    json.dump(Dict_path, file)


archieve.close()

'''
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(Dict_path)
st = set()
for item in filelist:
    end_s = list(item[-1].split('.'))[-1]
    st.add(end_s)
'''
