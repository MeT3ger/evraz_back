import requests
import json

class LLM_Connector:

    def __init__(self):
        self.prompt = {}
    
    async def create_prompt(self, user_content, database_content, instruct_content):
        sysyem_text_prompt = '''Ты говорящий на русском языке помощник программиста, 
                            который отвечает за проверку структуры отправляемых тебе проектов,
                            данных тебе ввиде объекта json.
                            '''

        user_text_prompt = '''Ниже дан проект в виде структуры json. 
                                Проверь его на соответствие требованиям по оформлению.
                                Используй данную инструкцию и подробно опиши все несоответствия, которые найдешь.
                        '''
        self.prompt = {'model': 'mistral-nemo-instruct-2407',
                       'messages' : [ 
                           {
                                'role': 'system',
                                #'content': sysyem_text_prompt + '\n\n' + instruct_content
                                'content': instruct_content
                            },
                            {
                                'role': 'user',
                                'content': user_text_prompt + '\n\n' + str(user_content)
                            },
                           
                        ],
                        'max_tokens': 1000,
                        'temperature': 0.3
                    }
        return self.prompt
    
    def send_request_to_mistral(self, headers = {}, http_addr = ''):
        if headers == {}:
            headers = {
                'Authorization': 'ue6XtSyH0I3G7abILEL0sk6NKG5GhzIw',
                'Content-Type': 'application/json',
            }
        
        if http_addr == '':
            http_addr = 'http://84.201.152.196:8020/v1/completions'

        response = requests.post(http_addr, headers=headers, json=self.prompt)
        answer = response.json()

        return answer