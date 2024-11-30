from data.consts.instruct import Instructions


class LLM_Params:
    __system_text_prompt = '''
        Ты говорящий на русском языке помощник программиста, 
        который отвечает за проверку структуры отправляемых тебе проектов,
        данных тебе ввиде объекта json. Требования представлены ниже.
    '''

    __user_text_prompt = '''
        Ниже дан проект в виде структуры json, повторяющий структуру проекта. Он может быть вложенный. 
        Проверь его на соответствие требованиям по оформлению.
        Используй данную тебе  инструкцию и подробно опиши все несоответствия, которые найдешь.
    '''
        
    headers= {
        'Authorization': 'ue6XtSyH0I3G7abILEL0sk6NKG5GhzIw',
        'Content-Type': 'application/json',
    }

    http_addr = 'http://84.201.152.196:8020/v1/completions'
    
    def body(user_file: str, instruction: Instructions, most_similary: str):
        return {
            'model': 'mistral-nemo-instruct-2407',
            'messages' : [ 
                {
                    'role': 'system',
                    # TODO: добавить связь с most_similary
                    'content': LLM_Params.__system_text_prompt + '\n\n' + str(instruction)
                },
                
                {
                    'role': 'user',
                    'content': LLM_Params.__user_text_prompt + '\n\n' + str(user_file)
                },
                
            ],
            'max_tokens': 1000,
            'temperature': 0.3
        }