from zipfile import ZipFile
import json
import pprint

#Функция для красивого вывода многоуровневого словаря
#   data_json - словарь
def display_json(data_json):
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(data_json)

#Функция для поиска всевозможных расширений в списке с файлами
#   filelist - список, содержащий имена файлов
#Вывод:
#   множество всевозможных расширений
def find_file_types(filelist):

    st = set() #возвращаемое множество

    for item in filelist:
        end_s = list(item[-1].split('.'))[-1]
        st.add(end_s)
    return st

#Функция для создания словаря из списка, повторяющего структуру копируемого пути файла.
#   archv - обьект ZipFile (архив) из которого читаются файлы
#   dict - словарь, в который записывается информация
#   list_path - список файла с путем к нему вида -['Директория1', 'Директория 2', ... 'файл']
#   indx - индекс начального элемента
#Вывод:
#   словарь со структурой, повторяющей путь файла
def create_dict(archv, dict, list_path, indx = 0):

    if indx < len(list_path) - 1:   #Если не дошли до самого файла, то углубляемся в следующую директорию
        if not(list_path[indx] in dict.keys()):
            dict[list_path[indx]] = {}
        return create_dict(archv, dict[list_path[indx]], list_path, indx+1)
    else:                           #Если дошли, то считываем файл в string. Игнорируем картинки png и все файлы из директории MAKOSX
        names = archv.namelist()
        for name in names:
            if name.endswith(list_path[indx]) and not('MACOSX' in name):
                with archv.open(name, 'r') as file:
                    if not name.endswith('png'):
                        dict[list_path[indx]] = file.read().decode('utf-8', errors='ignore')
                    else:
                        dict[list_path[indx]] ='some image'
        return dict

#Функция создания json непосредственно из архива zip
#   filename - имя архива
#   jsonname - имя json, в который будет сохраняться инфорация (если существует, то старая информация на нем будет стерта). По умолчанию 'PreprocData.json'
#Результат работы:
#   файл json, повторяющий структуру архива
def create_json(filename, jsonname = 'PreprocData.json'):

    #Чтение архива и создание всех необходимых переменных
    archieve = ZipFile(filename, mode='r')
    filelist = []
    Dict_path = {}

    for item in archieve.infolist():    #Создание списка со всеми файлами, кроме тех, что находятся в директории 'MACOSX'
        fname = item.filename

        if fname[-1] != '/' and not('MACOSX' in fname) :
            filelist.append(list(fname.split('/')))

    for item in filelist:   #Заполнение словаря
        create_dict(archieve, Dict_path, item)


    with open(jsonname, 'w') as file: #Запись словаря в файл json
        json.dump(Dict_path, file)


    archieve.close() #Закрытие чтения архива

if __name__ =='__main__':
    filename = '2020.2-Anunbis-develop.zip'
    create_json(filename)
