class Instructions():
    project_struct_py = '''
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
    
    file_struct_py = '''
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

    project_struct_ts = '''
        Требования к структуре проекта–Обзор

        В качестве сборщика проекта используется Vite . Все работы ДОЛЖНЫ начинаться с разворачивания
        шаблона проекта. Актуальный шаблон можно получить у Pavel.Tokarenko@evraz.com.
        структура в папке src проекта
        Adapters ........ (1)
        API ............. (2)
        App ............. (3)
        Assets .......... (4)
        Components ...... (5)
        Containers ...... (6)
        Facades ......... (7)
        Mock ............ (8)
        Models .......... (9)
        Pages ........... (10)
        Shared .......... (11)
        index.css ....... (12)
        main.tsx ........ (13)
        routing.tsx ..... (14)

        Схема взаимодействия компонентов системы

        1. Adapters
        Адаптеры используются для преобразования данных из одного формата в другой. Для каждого ответа
        сервера ДОЛЖЕН использоваться свой адаптер. Для компонента, который использует массивы
        объектов, объект в качестве атрибута props, ДОЛЖЕН создаваться адаптер. Структура файлов
        адаптеров:
        ComponentName
        fromAdapter.ts
        fromAdapter.ts
        ...
        fetchAdapter.ts
        fetchAdapter.ts
        ...

        Адаптеры для компонентов помещаются в каталог с названием компонента.
        Имя адаптера ДОЛЖНО соответствовать следующей схеме:
        fetch[FetchName]Adapter.ts

        from[DataType]To[ComponentType]Adapter.ts

        Название функции адаптера ДОЛЖНО начинаться с convert... и содержать исходный тип (который
        преобразуется) конечный тип (в который преобразуется). Например:
        function convertMeltInfoOriginToMeltInfo(origin: ResponseMeltInfo): MeltInfo {
        // ...
        }

        2. API
        Содержит функции получение данных. ДОЛЖЕН содержать запросы API или подписки RabbitMQ

        3. App
        Основной компонент приложения, точка входа.

        4. Assets
        Необязательно. МОЖЕТ использоваться для хранения вспомогательных элементов приложения
        (изображения, шрифты). НЕЛЬЗЯ использовать для хранения контента не относящегося к интерфейсу.
        НЕЛЬЗЯ хранить SVG иконки, так как они реализуются, как компоненты.

        5. Components
        Содержит компоненты приложения в предметной области UI. Компоненты ДОЛЖНЫ соответствовать
        определённым требованиям.

        6. Containers
        Содержит компоненты приложения в предметной области приложения. Контейнеры ДОЛЖНЫ
        соответствовать определённым требованиям. Контейнер МОЖЕТ содержать дополнительную
        разметку. Контейнеры связывают модель приложения с компонентом.
        Контейнер НЕЛЬЗЯ использовать в качестве элемента компонента. Контейнеры МОГУТ использоваться
        внутри других контейнеров.

        7. Facades
        Содержит универсальные хуки: предоставляющие взаимодействие с одним разделом модели.

        // useUsers.ts
        import { useUnit } from 'effector';
        import { $users, $currentUser } from '../Models/Users/state';
        import { setCurrentUser } from '../Models/Users/events';
        export function useUsers() {
        const users = useUnit($users);
        const currentUser = useUnit($currentUser);
        function selectUserById(userId) {
        const user = users.find((user) => user.id === userId);
        if (user != null) setCurrentUser(user);
        }
        // ...

        }

        return {
        users,
        currentUser,
        selectUserById,
        deleteUserById,
        editUser,
        };

        Например, Модель содержит раздел users для работы с пользователями: списки пользователей,
        события взаимодействия со списком, отправка данных и т.п. Фасад предоставляет упрощённый
        доступ к этим операциям.
        const {
        users,
        currentUser,
        selectUserById,
        deleteUserById,
        editUser
        } = useUsers();

        Сам фасад включает все необходимые манипуляции и взаимодействия с моделью

        8. Mock
        Содержит файлы конфигурации Mock-сервера. В качестве Mock-сервера МОГУТ выступать: json-server
        , для него используются файлы формата *.json ; Swagger  с форматом *.yaml | *.yml .

        9. Models
        Общее состояние приложения. В качестве менеджера используется effector .
        Структура (Вариант 1)
        SideEffects
        <sideEffectGroupName>.ts
        <modelName>
        index.ts
        init.ts
        ...
        init.ts

        Структура (Вариант 2)
        <moduleName>
        events.ts
        effects.ts
        store.ts
        index.ts

        Пример
        // effects.ts
        import { createEffect } from 'effector';
        import { fetchUsers, postUser, deleteUser, putUser } from '../../API';
        export const getUsersFx = createEffect(fetchUsers);
        export const editUserFx = createEffect(putUser);
        export const createUserFx = createEffect(postUser);
        export const deleteUserFx = createEffect(deleteUser);

        // store.ts
        import { createStore } from 'effector';
        export const $users = createStore([]);
        export const $backupUser = createStore(null);
        export const $currentUser = createStore({});

        // events.ts
        import { createEvent } from 'effector';
        export const setCurrentUser = createEvent();
        export const editUser = createEvent();

        // index.ts
        import { sample } from 'effector';
        import { getUserFx } from './effects';
        import { $users, $currentUser, $backupUser } from './store';
        import { setCurrentUser, editUser } from './events';
        import {
        isNotEmpty,
        saveDataIsNotEqual,
        prepareOptimisticSave,
        prepareRestoreUserData,
        clearBackup
        } from './utils';
        $users.on(getUserFx.doneData, saveDataIsNotEqual);
        // Установить текущего пользователя
        sample({
        source: setCurrentUser,
        filter: isNotEmpty,
        target: $currentUser,
        });
        // Изменить данные о пользователе, отправить на сервер,
        // сделать бэкап изменяемых данных
        sample({
        source: $users,
        clock: editUser,
        fn: prepareOptimisticSave,
        target: [$users, $backupUser, editUserFx],
        });
        // Если сервер при сохранении ответит ошибкой,
        // восстановить данные о пользователе, очистить бэкап
        sample({
        source: [$users, $backupUser],
        clock: editUserFx.error,
        fn: prepareRestoreUserData,
        target: [$users, $backupUser],
        });
        // Если сохранение прошло успешно, очистить бэкап
        sample({
        source: $backupUser,
        clock: editUserFx.done,
        fn: clearBackup,
        target: $backupUser,
        })

        10. Pages
        Содержит компоненты представляющие один экран. Подчиняется тем же правилам разработки
        компонентов, что и обычные компоненты или контейнеры с некоторыми отступлениями.

        11. Shared
        Содержит общие типы для всего приложения. Общие утилиты.

        12. index.css
        Глобальные стили приложения

        13. main.tsx
        Точка входа в приложение

        14. routing.tsx
        Конфигурация маршрутизации
    '''

    file_struct_ts = '''
        Именования–Обзор

        Имена должны передавать намерения программиста. Имя переменной, функции, класса должно
        отвечать на все главные вопросы: почему существует, что делает и как используется.
        плохо
        let d: number; // Прошедшее время

        хорошо
        let elapsedTimeInDays: number;
        let daysSinceCreation: number;
        let daysSinceModification: number;
        let fileAgeInDays: number;

        Содержательные имена упрощают понимание и модификацию кода. Например:
        function getThem(list: List<number[]>): List<number[]> {
        const list1: List<number[]> = new List<number[]>();
        for (const x of list) {
        if (x[0] === 4) list1.add(x);
        }
        return list1;
        }

        1. Что за данные в list ?
        2. Чем важен элемент list с нулевым индексом?
        3. Какой смысл несёт значение 4?
        4. Как будет использоваться возвращаемый список?
        Но выше представлен фрагмент игры в «Сапёр», где list – это игровое поле, элемент с нулевым
        индексом – это код состояния, код 4 - означает «Флаг установлен». Итог:
        function getFlaggedCells(gameBoard: List<number[]>): List<number[]> {
        const flaggedCells: List<number[]> = new List<number[]>();
        for (const cell of gameBoard) {
        if (cell[STATUS_CODE] === FLAGGED)
        flaggedCells.add(cell);
        }
        return flaggedCells;
        }

        Базовые правила именования сущностей
        1. Избегайте дезинформации. Например: accountList – плохо, так как есть структура данных List ,
        если хранение в чём-то отличном (или вообще давно поменялось) вводит в заблуждение.
        Хорошо - accounts , accountGroup .
        2. Используйте осмысленные различия. Например: Product , PropductInfo , PropductData - с точки
        зрения смысла абсолютно одинаковые. Такие сущности не должны существовать в рамках
        проекта. UsersTable - хуже чем Users
        3. Используйте удобопроизносимые имена. genDtMs – хуже чем generatedTimestamp
        4. Избегайте схем кодирования имён. Не используйте аббревиатуры (например, венгерская запись)
        для имён без необходимости, не используйте дополнительные приставки, суффиксы, окончания,
        кроме тех случаев, когда это регламентированно библиотекой (например, эффектор
        регламентирует обозначения для юнитов: стор – приставка $ , эффект - окончание Fx ).
        // плохо
        const IDOF: number = 7 // номер дня недели
        const s_id: string = 'afe...' // тип в приставке

        // хорошо
        const dayOfWeek: number = 7;
        const $accounts: UnitStore<Account[]> = createStore();
        const fetchAccountsFx: UnitEffect<Account[], void> = createEffect();

        camelCase
        Названия функций, переменных, констант пишутся в нотации camelCase .
        // плохо
        let LastDayOfMonth: Date;
        let last_day_of_month: Date;
        // хоршо
        let lastDayOfMonth: Date;

        PascalCase
        Используется в названиях компонентов, классов, типов, интерфейсов, enum
        // плохо
        class user {}
        type listItem = {};
        interface use_fetch {};
        // хоршо
        class User {};
        type ListItem = {};
        interface AnimationProps {};
        function UserBadge(props: UserBadgeProps) { ... }

        snake_case
        Используется в типах представляющих ответ API, в адаптерах при преобразовании в структуру
        соответствующую соглашениям выше. В названиях CSS селекторов, в том числе использующихся в CSS
        Modules.
        // плохо
        let user_index: number = 0;
        <div className={styles.bodyDark} />
        // хорошо
        {
        fullName: origin.full_name,
        }
        <div className={styles.body_dark} />

        UPPER_SNAKE_CASE
        Применяется для констант, которые используются как определения. Содержат не вычисленные
        значения.
        // плохо
        const initialDurationMs: number = 5;
        const DELTA_TIME: number = lastFrameTime - currentTime;
        // хорошо
        const INITIAL_DURATION_MS: number = 5;

        Части речи
        Для того чтобы код был само-документируемым названия ДОЛЖНЫ соответствовать определённым
        частям речи.
        Существительное, прилагательное, деепричастие
        Названия переменных, констант, enum ДОЛЖНЫ отвечать на вопросы «Что?», «Какой?», «Что
        делающий?». Названия классов только на вопрос «Что?». Для прилагательных используется окончание
        ed , для деепричастий able Множественное число ДОЛЖНО использоваться для массивов, списков,
        наборов (Set), словарей (Map), stack, queue.
        // плохо
        const fetchElement = ...; // глагол
        // хорошо
        const user = ...;
        let account = ...;
        const controllers: Controller[] = [];
        const sortedUsers: User[] = []; // причастие
        const moveableTask: Task = new Task(); // деепричастие

        Глагол
        Названия функций, методов классов ДОЛЖНЫ отвечать на вопрос «Что делает?», «Что делать?».
        // плохо
        function accounts(): Account[] {} // существительное
        // хорошо
        function getAccounts(): Account[] {}
        function sort<T>(sortedItems: T[]): T{} {}
        Вопросительное предложение

        Названия переменных, констант, функций, имеющих, либо возвращающих, значение типа boolean ,
        ДОЛЖНЫ записываться как вопрос, на который можно ответить только «Да» или «Нет». Для этого
        ДОЛЖНЫ использоваться глаголы is , has , are .
        // плохо
        let mounted: boolean = false;
        // хорошо
        let isMount: boolean = false;
        function hasOvertime(): boolean {}
        let areEqualName: boolean = false;

        CSS селекторы
        Так как для компонентов ДОЛЖНЫ использоваться CSS Modules, название селектора должно
        относиться к элементу (понятие из БЭМ (bem.info) ). Для указания модификатора используется
        разделитель __ (Двойное подчеркивание).
        /* плохо */
        .card_title {}
        /* хоршо */
        .title {}
        .title__primary {}

        Custom Properties
        Согласно требованиям к разработке компонента, для стилизации сложных компонентов используются
        Custom Properties. Названия имеют следующую структуру
        --element_name_css-property[__state]

        Например:
        .root {
        }

        --title_background-color: #3eaf22;
        --title_background_color__hover: #aa21e1;

        Обязательные именования
        Обработчики событий
        Функции обработки событий ДОЛЖНЫ начинаться с глагола handle , НЕЛЬЗЯ использовать on .
        Название ДОЛЖНО относиться к предметной области проекта.
        // плохо
        function selectMine(event: SelectEvent) {}
        function handleOnSelect(event: SelectEvent) {}
        // хорошо
        function handleSelectMine(event: SelectEvent) {}
        function handleOpenPathConfigurator(event: ClickEvent) {}

        Порождение событий
        Как правило применяется к атрибутам функций, методам классов. Название атрибута ДОЛЖНО
        содержать приставку on .
        // плохо
        function Selector(change: () => {}) {}
        function createSomething(e: () => {}) {}
        // хорошо
        function Selector(onChange: () => {}) {}
        function createSomething(onCreated: () => {}) {}

        JSX / TSX
        Именования атрибутов компонента ДОЛЖНЫ быть прилагательными или существительными и
        отвечать на вопрос «Что?», «Какой?».
        <!-- Плохо -->
        <Component isDisabled />
        <Component isPrimary />
        <Component renderSlot={...} />
        <!-- Хорошо -->
        <Component disabled />
        <Component primary />
        <Component itemSlot={...} />

        Требования к разработке компонентов–Обзор

        Виды компонентов
        UI Kit — абстрактные компоненты, которые будут переиспользоваться другими модулями.
        Предметная область - UI.
        Components — абстрактные компоненты, которые специфичны для текущего модуля,
        гипотетически могут стать компонентами UI Kit. Пердметная область - UI.
        Containers — компоненты, которые взаимодействуют с данными. Как правило привязаны к
        предметной области модуля. Проектная предметная область.
        Pages — компоненты, которые используются в качестве экрана. Проектная предметная область.

        Структура компонента
        Данная структура справедлива для всех компонентов.
        <ComponentName>
        index.ts
        (1)
        <ComponentName>.tsx
        (2)
        <ComponentName>.module.css (3)
        types.ts
        (4)
        utils.ts
        (5)
        <ComponentFragmentName>.tsx (6)
        <PageContainerName>.tsx
        (7)

        1. index.ts используется для экспорта основного компонента. Позволяет убрать дублирование имён
        при импорте компонента.
        // без index.ts
        import Component from "./Components/Component/Component";
        // с index.ts
        import Component from "./Components/Component";

        Содержимое index.ts
        import Component from "./Component";
        export default Component;

        Важно! НЕЛЬЗЯ вести разработку компонента в index.ts .
        2. Основной компонент. Название должно совпадать с названием папки в которой находится
        компонент. Расширение файла обязательно должно быть .tsx
        3. Обязательно использование css modules. Название модуля должно совпадать с названием
        директории в которой находится таблица стилей. Применяется для обеспечения инкапсуляции
        компонента.
        4. Типы данных используемые с компонентом
        5. Все вспомогательные функции, используемые в компоненте, ДОЛЖНЫ выноситься в данный
        файл.
        6. Если используются вспомогательные компоненты, все выносятся в отдельный компонент,
        размещаются на том же уровне, что и основной компонент. Используют ту же таблицу стилей.
        7. Только для компонентов страниц, если необходим. Контейнер хранится в том же месте, где и
        реализация компонента.

        Имена компонентов
        Имена компонентов задаются в формате PascalCase .
        # плохо
        componentName
        component-name
        Componentname
        # хорошо
        ComponentName

        Имя функции компонента должно совпадать с именем файла.
        ComponentName.tsx

        // ...
        function ComponentName(/* props */) {
        // ...
        }

        Выбор имени
        Имя компонента зависит от вида компонента. Для абстрактных компонентов (UI Kit, Components) имя
        задаётся в отрыве от данных, полагаясь только на внешний вид компонента. Для остальных опираясь
        на назначение в проекте.
        Пример. На макете изображен элемент, который выводит данные по плавкам с фотографиями:
        Плохо
        В папке Components создаётся компонент MeltsInfoGrid . Компонент подключает данные, производит
        преобразования данных.
        Хорошо
        В папке Components или UI Kit создаётся компонент ImagesWithDescriptionsGrid . В папке Containers
        создаётся компонент MeltsInfoGrid , который получает данные, преобразует их для
        ImagesWithDescriptionsGrid затем выведет ImagesWithDescriptionsGrid

        Порядок импортов
        Данный порядок задаётся плагином к ES Lint , автоматизируется за счёт плагинов к IDE ES Lint ,

        Требования к разработке компонентов–Обзор

        Внимание! Конфигурация линтеров стандартизирована и входит в стартовый шаблон проекта.
        Использование альтернативой конфигурации возможно только после согласования с лидером
        направления.

        Типизация компонента
        Типы компонента описываются в файле types.ts и ДОЛЖНЫ экспортироваться, если используются в
        интерфейсе компонента.
        Для props компонента, как минимум, ДОЛЖЕН быть разработан интерфейс следующего содержания:
        export interface ComponentNameProps {
        className?: string;
        style?: React.CSSProperties;
        }

        Сам компонент в обязательном порядке ДОЛЖЕН использовать атрибуты указанные выше. Пример:
        function ComponentName({ className, style }: ComponentNameProps) {
        return (
        <div className={clsx(styles.root, className)} style={style}>
        {content}
        </div>
        );
        }

        Примечание. clsx модуль, отвечающий за конкатенацию имён CSS классов
        НЕЛЬЗЯ использовать стилизующие атрибуты, кроме style . Например: margin , size , height , width и
        т.п.

        Стили компонента
        В компоненте ДОЛЖНЫ применяться CSS Modules . Конечное название стиля имеет следующую
        схему:
        [ИмяКомпонента]_[локальное_имя_класса]__[хЭш]

        Для того чтобы отличать названия атрибутов объектов от названий CSS классов, для последних
        применяется snake_case нотация. Корневой элемент компонента ДОЛЖЕН содержать класс .root .
        БЭМ методология МОЖЕТ применяться частично. Не нужно указывать название блока, используется
        только название элемента. Модификатор отделяется от элемента двойным символом подчёркивания.
        Например: styles.pane , styles.pane__visibly
        НЕЛЬЗЯ использовать значения в названиях классов. Например: .margin_20 , .size_500 .

        Стилизация сложных компонентов
        Компоненты, имеющие сложную структуру, ДОЛЖНЫ быть стилизованы с использованием CSS
        Custom properties . Названия CSS Custom properties ДОЛЖНЫ задаваться следующим шаблоном:
        --<имя-элемента>-<название-стиля>-<модификатор>

        Например:

        Требования к разработке компонентов–Обзор

        function Switcher({ className, style, checked, onChange }: SwitcherProps) {
        // Логика...
        return (
        <label className={clsx(styles.root, className)} style={style}>
        <input
        type="checkbox"
        className={styles.input}
        checked={checked}
        onChange={onChange}
        />
        <div className={styles.marker} />
        </label>
        );
        }

        .root {
        --marker-background-color: #123;
        --marker-border: none;
        --marker-background-color-active: #321;
        /* Остальные стили */
        }
        .marker {
        background-color: var(--marker-background-color);
        border: var(--marker-border);
        }
        .input:checked + .marker {
        background-color: var(--marker-background-color-active);
        }

        Функции–Обзор

        В проектах ДОЛЖНЫ использоваться обычные функции вместо стрелочных. Стрелочные функции не
        являются заменой обычным, так как несут определённую функциональность и ограничения.
        Например, могут быть объявлены только как функциональные выражения, что накладывает
        ограничение на порядок объявления.
        Стрелочные функции всегда остаются стрелочными, нельзя предугадать в каком ключе будет
        использован модуль другим разработчиком, а значит, что стрелочные функции могут наложить ряд
        ограничений, либо не ожидаемые свойства в случае передачи ссылки на функцию.
        // плохо
        const useArrowFunction = () => {
        // arrow body
        ...
        }
        // хорошо
        function useClassicFunction() {
        // function body
        ...
        }

        Стрелочные функции ДОЛЖНЫ применяться только в качестве callback ов с простыми выражениями.
        Если возникла необходимость добавить фигурные скобки тела стрелочной функции, ДОЛЖНА
        использоваться классическая функция.
        // плохо
        useSomething((a, b) => {
        if (a == null && b == null) return [];
        return [...a, ...b];
        });
        // хорошо
        useSomething((a, b) => a - b);
        useSomething(combineArrays);
        function combineArrays<T>(a: T[], b: T[]): T[] {
        if (a == null, b == null) return [];
        return [...a, ...b];
        }

        Стрелочные функции НЕЛЬЗЯ использовать в качестве методов объектов. Это связано с
        возможностью использования ссылки на метод, вместо вызова. Особенно чревато подобное
        использование, если в методе используется this для доступа к другим элементам объекта, что может
        создать ситуацию, когда в этот this попадёт контекст другого объекта или функции.
        // плохо
        const myObject = {
        bestMethod = () => {
        this.anotherMethod();
        },
        anotherMethod = () => {}
        }
        useFunction(myObject.bestMethod) // опасно, this.anotherMethod() выдаст ошибку,
        // либо никогда не выплонится
    '''

    file_struct_cs = '''
        Руководство по код-ревью–Обзор

        Содержимое
        • Проверяем соответствие регламентам
        • На что обращаем внимание
        • Частые ошибки
        • Общие
        • Архитектура и дизайн методов
        • LINQ
        • Entity Framework

        Проверяем соответствие регламентам
        1. Обязательные решения при разработке
        Для всех проектов
        OpenShift
        WPF
        2. Руководство по стилю csharp

        На что обращаем внимание
        Проект
        Nuget пакеты, по возможности, должны быть обновлены до последних версий и не иметь
        уязвимостей
        Если транзитивный Nuget пакет имеет уязвимость, значит он должен быть включен в проект
        и обновлен до актуальной версии
        Проект не должен иметь лишних зависимостей или зависимостей, ссылающихся на
        локальные файлы (для таких зависимостей прописан абсолютный путь)
        Код
        В коде не должно быть неразрешенных TODO
        Не должно быть закомментированного или неиспользуемого кода
        Код с атрибутом Obsolete , по возможности, должен быть удален
        Обязательное наличие комментариев для моделей, сущностей и т.д.
        Стоит обращать внимание на неиспользуемые переменные или неиспользуемый возврат из
        методов

        Частые ошибки
        Общие
        Дублирование сообщения, при логировании исключения

        Log.Error(ex, ex.Message);
        Log.Error(ex, "");

        // Сообщение будет задублировано
        // Без дублирования

        Объединение строк с помощью оператора + , вместо Литералы необработанных строк
        await _context.Database.ExecuteSqlRawAsync("select * from uzdt.addfactorywagon("
        + "@p_wagonid, "
        + "@p_tracksectionid, "
        + "@p_netweight, "
        + "@p_grossweight; ");

        Использование прямых вычислений, вместо методов конвертации
        int netWeight = factoryWagon?.NetWeight / 1000;

        Лишняя проверка на null , для арифметический операций
        return (tons.HasValue) ? tons.Value * 1000 : null;

        Архитектура и дизайн методов
        Неправильная регистрация сервисов в IoC контейнере, когда HostedService должен быть доступен
        как Singleton
        // Неправильно
        services.AddScoped<IMnemonicStationService, MnemonicStationService>();
        services.AddSingleton<IHostedService, MnemonicStationService>();
        // Правильно
        services.AddSingleton<IMnemonicStationService, MnemonicStationService>();
        services.AddHostedService(provider => provider.GetRequiredService<IMnemonicStationService>());

        Возврат null , вместо пустой коллекции
        public IList<string>? GetHeaders()

        Возврат коллекции, c null элементами
        public IList<string?> GetHeaders()

        Проверку передаваемых аргументов стоит выполнять в методе, а не в вызове метода
        UserEntity user = await _userRepository.GetUserByIdAsync(
        command.UserId ?? throw new InvalidOperationException("Message")
        )

        Если возврат null из метода, является исключением, то исключение нужно кидать в методе, а не
        в клиентском коде

        FunctionCapabilityEntity functionCapability = await _functionCapabilityRepository.GetByIdAsync(command.Syst
        ?? throw new InvalidOperationException("Message");

        Использование внутри метода интерфейса коллекции, вместо реализации
        IList<int> list = new List<int>();

        LINQ
        Использование Skip().Take() , вместо Chunk()
        while (i < fMPCompany.CompanyTab.Length)
        {
        FMPCompanyItemDto[] items = fMPCompany.CompanyTab
        .Skip(i)
        .Take(SapErpLoadConsts.BatchSize)
        .ToArray();
        // ...
        i += SapErpLoadConsts.BatchSize;
        }

        Использование методов Union() , Except() , Intersect() , Distinct() , SequenceEqual() ,
        при работе с пользовательским типом данных,
        для которого не переопределены методы Equals() и GetHashCode() или не реализован интерфейс
        IEquatable<T>

        return ordersToro
        .Union(ordersCo)
        .ToArray();

        Использование Distinct() , после Union()
        long[] totalFunctionCapabilities = functionCapabilitiesRoles
        .Select(x => x.FunctionCapabilityId)
        .Union(functionCapabilitiesUser.Select(x => x.FunctionCapabilityId))
        .Distinct()
        .ToArray();

        Лишний ToArray() или ToList()
        EmployeesListItem[] employees = await GetEmployeesListAsync(usersByFio, positionsByTableNames, cancellation
        return new EmployeesListMessage { EmployeesList = employees.ToArray() };

        // Лишний ToArray()

        foreach(FactoryItemResponse factoryDto in dto.Where(t=> factoryNums.Contains(t.Number)).ToList())
        {
        factoryDto.CompanyId = balanceEntity.Id;
        }

        // Лиш

        Entity Framework

        Использование синхронных методов материализации, вместо асинхронных
        Удаление сущностей в цикле
        foreach (WagonMarkingPrescription item in markingForRemove)
        {
        _context.WagonMarkingPrescriptions.Remove(item);
        }

        Лишняя материализация при удалении элементов
        List<WagonMoveHistory> removingTrackMovementHistory = await _context.WagonMoveHistory
        .Where(z => z.TrackSectionId == trackSectionId)
        .ToListAsync();
        // Лишний ToListAsync()
        _context.WagonMoveHistory.RemoveRange(removingTrackMovementHistory);

        Вызов SaveChangesAsync() после каждого действия
        IQueryable<InvoiceOutFactoryWagon> wagons = _context.InvoiceOutFactoryWagons.Where(a => a.InvoiceOutId == i
        _context.InvoiceOutFactoryWagons.RemoveRange(wagons);
        await _context.SaveChangesAsync();
        // Лишний SaveChangesAsync()
        _context.InvoiceOuts.Remove(invoice);
        await _context.SaveChangesAsync();

        Выполнение фильтрации на стороне приложения, а не БД
        FactoryEntity[] allFactories = await _appDbContext.Set<FactoryEntity>()
        .AsNoTracking()
        .Include(x => x.BalanceUnitEntity)
        .ToArrayAsync(cancellationToken);
        return allFactories
        .Where(x => identificators.Any(y => y == x.Number))
        .ToArray();

        Использование AddAsync() и AddRangeAsync() , вместо Add и AddRange() , если не используется
        SqlServerValueGenerationStrategy.SequenceHiLo

        await _context.InvoiceOutDocuments.AddAsync(invoice);
    '''