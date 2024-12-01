from data.consts.instruct import Instructions
from data.consts.languague import Language


class LLM_Params:

    __project = {
        'system_text_prompt' : '''
            Пиши на русском языке. Проверь, Правильно ли оформлен проект. 
        ''',
        'user_text_prompt': '''
            Ниже дан проект в виде списка, состоящего из имен файлов проекта с путями к ним. 
            Проверь его на соответствие требованиям по оформлению.
            Используй данную тебе  инструкцию и подробно опиши все несоответствия, которые найдешь.
        '''
    }

    __file = {
        'system_text_prompt' : '''
            Пиши на русском языке. Проверь, Правильно ли оформлен програмный код. 
        ''',
        'user_text_prompt': '''
            Ниже дан текст программы. 
            Проверь его на соответствие требованиям по оформлению.
            Используй данную тебе  инструкцию и подробно опиши все несоответствия, которые найдешь.
        '''
    }
        
    headers= {
        'Authorization': 'ue6XtSyH0I3G7abILEL0sk6NKG5GhzIw',
        'Content-Type': 'application/json',
    }

    http_addr = 'http://84.201.152.196:8020/v1/completions'
    
    def body(user_file: str, instruction, most_similary: str, is_this_project):
        #print(user_file)
        message = {}

        if is_this_project:
            message = {
            'model': 'mistral-nemo-instruct-2407',
            'messages' : [ 
                {
                    'role': 'system',
                    # TODO: добавить связь с most_similary
                    'content': LLM_Params.__project['system_text_prompt'] + '\n\n' + str(instruction)
                },
                
                {
                    'role': 'user',
                    'content': LLM_Params.__project['user_text_prompt'] + '\n\n' + str(user_file)
                },
                
            ],
            'max_tokens': 1000,
            'temperature': 0.4
        }
        else:
            message = {
            'model': 'mistral-nemo-instruct-2407',
            'messages' : [ 
                {
                    'role': 'system',
                    # TODO: добавить связь с most_similary
                    'content': LLM_Params.__file['system_text_prompt'] + '\n\n' + str(instruction)
                },
                
                {
                    'role': 'user',
                    'content': LLM_Params.__file['user_text_prompt'] + '\n\n' + str(user_file)
                },
                
            ],
            'max_tokens': 1000,
            'temperature': 0.4
        }

        return message