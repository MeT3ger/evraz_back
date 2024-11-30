class Instructions:
    project_struct = '''
    Требования по оформлению Python-проекта:
    demo_project
        components
            demo_project_backend
                demo_project
                tests
                    __init__.py
                    pyproject.toml
                    README.md
                    setup.py
        deployment
        docs
        .editorconfig
        .gitignore
        .gitattributes
        
    в deployment лежат файлы для CI/CD
    в dock тех документация
        схема преценденты
        схема базы данных
        схема развертывания
        схема компонетов
        swagger
        документация к бизнес процессам
    каталог components для отделения backend и frontend
    demo_project_backend - корень
    
    Используется гексагональная архитектура:
    demo_project_backend
                demo_project
                    adapters
                    application
                    composites
                tests
                    __init__.py
                    pyproject.toml
                    README.md
                    setup.py
    
    бизнес логика.
    
    application
        etl
            __init__.py
            constants.py
            dataclasses.py
            interfaces.py
            services.py
        mills_planner
            services
            __init__.py
            constants.py
            dataclasses.py
            events.py
            interfaces.py
        model
            __init__.py
            errors.py
    
    Используются dto, константы, ds модели, сервисы и т.д.
    В этом слое описываются всевозможные ошибки!
    
    
    Слой адаптеров
    В адаптерах лежат интеграции со внешними сервисами.
    
    adapters
        api
        app_database
        cli
        kafka_consumer
        logger
        message_bus
        source_database
        source_excel_parser
        
    таблицы описаны в виде sqlalchemy моделей.
    
    adapters
        api
        app_database
            alembic
                migrations
                __init__.py
                env.py
                scipt.py.mako
            repositories
                __init__.py
                mapping.py
                settings.py
                tables.py
    
    используется snake case
    
    Слой композитов
    composites
        __init__.py
        alembic_runner.py
        api.py
        cli.py
        etl.py
        model.py
        realtime_data.py
    '''
    
    file_struct = '''
        Для базы данных применяется как можно меньше диалекто-зависимых
        конструкций, а если применятся то оставляется #TODO: dialect dependent
        
        указывать naming_convention в Metadata обязательно
        
        названия таблиц в snake_case
        
        В БД вся дана храниться в UTC и в приложении в UTC
        
        print не использовать!
        
        Неверно
        id = 1
        self.logger.info(f"User with id [{id}] was created")
        
        верно
        id = 1
        self.logger.info(f"User with id [%s] was created", id)
        
        Не используется асинхронный код!
        
        pandas numpy используются только в DS
        
        Websockets только для уведомлений!
        
        Код пишется по Pep8 докстринги по PEP256 257
        
        строки переносим по 80 символов
    '''