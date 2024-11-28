from zipfile import ZipFile
import json
import pprint

#Класс для работы с запакованным архивом
#Атрибуты класса:
#   filename - имя зип архива
#   archieve - обьект ZipFile (архив)
#   filelist - список с путями до файлов
#   Dict_path - словарь со структурой архива
class ZipPreproc:

    #Инициализация класса
    #   filename - имя архива
    def __init__(self, filename):
        self.filename = filename    #Имя файла
        self.archieve = ZipFile(filename) #Архив
        self.filelist = []  #Список всез файлов
        self.Dict_path = {}

        for item in self.archieve.infolist():    #Создание списка со всеми файлами, кроме тех, что находятся в директории 'MACOSX'
            fname = item.filename

            if fname[-1] != '/' and not('MACOSX' in fname) :
                self.filelist.append(list(fname.split('/')))

    #Функция для полного заполнения словаря
    async def fill_dict(self):
        for item in self.filelist:   #Заполнение словаря
            await self.__create_dict(list_path=item)

    #Функция для красивого вывода многоуровневого словаря
    #   data_json - словарь
    async def display_json(self):

        if self.Dict_path == {}:
            await self.fill_dict()

        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(self.Dict_path)

    #Функция для поиска всевозможных расширений в списке с файлами
    #   filelist - список, содержащий имена файлов
    #Вывод:
    #   множество всевозможных расширений
    async def find_file_types(self):

        if self.Dict_path == {}:
            await self.fill_dict()

        st = set() #возвращаемое множество

        for item in self.filelist:
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
    async def __create_dict(self, list_path, indx = 0):

        if indx < len(list_path) - 1:   #Если не дошли до самого файла, то углубляемся в следующую директорию
            if not(list_path[indx] in self.Dict_path.keys()):
                self.Dict_path[list_path[indx]] = {}
            return await self.__create_dict(list_path, indx+1)
        else:                           #Если дошли, то считываем файл в string. Игнорируем картинки png и все файлы из директории MAKOSX
            names = self.archieve.namelist()
            for name in names:
                if name.endswith(list_path[indx]) and not('MACOSX' in name):
                    with self.archieve.open(name, 'r') as file:
                        if not name.endswith('png'):
                            self.Dict_path[list_path[indx]] = file.read().decode('utf-8', errors='ignore')
                        else:
                            self.Dict_path[list_path[indx]] ='some image'
            return self.Dict_path

    #Функция создания json непосредственно из архива zip
    #   filename - имя архива
    #   jsonname - имя json, в который будет сохраняться инфорация (если существует, то старая информация на нем будет стерта). По умолчанию 'PreprocData.json'
    #Результат работы:
    #   файл json, повторяющий структуру архива
    async def create_json(self, jsonname = 'PreprocData.json'):

        if self.Dict_path == {}:
            await self.fill_dict()

        with open(jsonname, 'w') as file: #Запись словаря в файл json
            json.dump(self.Dict_path, file)
        
        return True


    def __del__(self):
        self.archieve.close()