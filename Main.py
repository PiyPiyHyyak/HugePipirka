from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

keyboard_callback = CallbackData("menu", "choice")
ege_bt = InlineKeyboardButton("ЕГЭ", callback_data=keyboard_callback.new(choice="ЕГЭ"))
oge_bt = InlineKeyboardButton("ОГЭ", callback_data=keyboard_callback.new(choice="ОГЭ"))
keyboard = InlineKeyboardMarkup(row_width=2)
keyboard.add(ege_bt)
keyboard.add(oge_bt)

from config import TOKEN

bot = Bot(token=TOKEN)  # Создание объекта бота с использованием токена
dp = Dispatcher(bot=bot, storage=MemoryStorage())

dictionary_list = [
    ["Ability (способность)", "Inability (неспособность)", "Disability (нетрудоспособность)", "Able (способный)",
     "Unable (неспособный)", "Disabled (инвалид)", "Enable (дать возможность)", "Disable (делать неспособным)",
     "Ably (умело)"],
    ["Absurdity (абсурдность)", "Absurd (абсурдный)"],
    ["Acceptability (приемлемость)", "Acceptable (приемлемый)", "Unacceptable (неприемлемый)", "Accept (принимать)"],
    ["Access (доступ)", "Accessibility (доступность)", "Accessible (доступный)", "Accessibly (доступно)"],
    ["Accident (случай)", "Accidental (случайный)", "Accidentally (случайно)"],
    ["Adventure (приключение)", "Adventurous (приключенческий)"],
    ["America (Америка)", "American (американский)"],
    ["Amazement (изумление)", "Amaze (изумлять)", "Amazing (изумительный)"],
    ["Archaeology (археология)", "Archaeological (археологический)", "Archaeologist (археолог)"],
    ["Association (ассоциация)", "Associate (ассоциировать)", "Associated (ассоциируемый)"],
    ["Beauty (красота)", "Beautify (украсить)", "Beautiful (красивый)"],
    ["Belief (убеждение)", "Believe (верить)", "Believable (правдоподобный)", "Unbelievable (неправдоподобный)"],
    ["Beginning (начало)", "Begin (начинать)"],
    ["Building (здание)", "Build (строить)"],
    ["Calculation (вычисление)", "Calculate (вычислять)", "Calculated (вычисленный)"],
    ["Celebration (празднование)", "Celebrate (праздновать)"],
    ["Chemistry (химия)", "Chemist (химик)", "Chemical (химический)"],
    ["Choice (выбор)", "Choose (выбирать)", "Chosen (выбранный)"],
    ["Commerce (коммерция)", "Commercial (коммерческий)"],
    ["Communication (коммуникация)", "Communicate (общаться)"],
    ["Competition (соревнование)", "Compete (соревноваться)", "Competitive (соревновательный)"],
    ["Consideration (рассмотрение)", "Consider (рассматривать)"],
    ["Conservatism (консерватизм)", "Conservation (консервация)", "Conserve (сохранять)",
     "Conservative (консервативный)"],
    ["Construction (конструкция)", "Construct (сооружать)", "Constructive (конструктивный)"],
    ["Convenience (удобство)", "Convenient (удобный)", "Inconvenient (неудобный)", "Conveniently (удобно)"],
    ["Convention (соглашение)", "Conventional (традиционный)", "Unconventional (нетрадиционный)"],
    ["Correction (исправление)", "Correct (точный)", "Incorrect (неточный)", "Correctly (точно)"],
    ["Day (день)", "Daily (дневной)"],
    ["Defense (оборона)", "Defend (защищать)", "Defensive (оборонительный)", "Defenseless (беззащитный)"],
    ["Discovery (открытие)", "Discover (открывать)"],
    ["Digit (цифра)", "Digital (цифровой)"],
    ["Drawing (рисование)", "Draw (рисовать)"],
    ["Education (обучение)", "Educate (обучать)", "Educated (обученный)", "Educational (образовательный)"],
    ["Employee (сотрудник)", "Employer (работодатель)", "Employment (трудоустройство)", "Employ (нанимать)",
     "Employed (трудоустроенный)"],
    ["Energy (энергия)", "Energize (заряжать энергией)", "Energetic (энергичный)"],
    ["Entertainment (развлечение)", "Entertain (развлекать)", "Entertaining (развлекательный)"],
    ["Environment (окружающая среда)", "Environmental (экологический)"],
    ["Essence (сущность)", "Essential (существенный)"],
    ["Europe (Европа)", "European (европейский)"],
    ["Extent (степень)", "Extend (расширять)", "Extended (обширный / расширенный)",
     "Extensive (обширный / расширенный)"],
    ["Face (лицо)", "Facial (лицевой)"],
    ["Fairness (справедливость)", "Unfairness (несправедливость)", "Fair (честный)", "Unfair (нечестный)"],
    ["Family (семья)", "Familiarity (знакомство)", "Familiar (знакомый)", "Unfamiliar (незнакомый)"],
    ["Foreigner (иностранец)", "Foreign (иностранный)"],
    ["Formality (формальность)", "Formal (формальный)", "Informal (неформальный)"],
    ["France (Франция)", "French (французский)"],
    ["Freedom (свобода)", "Free (свободный)", "Free (освобождать)"],
    ["Globe (мир)", "Global (глобальный)"],
    ["Honesty (честность)", "Dishonesty (нечестность)", "Honest (честный)", "Dishonest (нечестный)"],
    ["History (история)", "Historic (исторический - важный в истории)",
     "Historical (исторический - о событиях в прошлом)"],
    ["Impression (впечатление)", "Impress (впечатлять)", "Impressive (впечатляющий)", "Unimpressive (невпечатляющий)"],
    ["Importance (важность)", "Important (важный)"],
    ["Inclusion (включение)", "Include (включать)", "Inclusive (включающий)"],
    ["Introduction (введение)", "Introduce (вводить)", "Introductory (вводный)"],
    ["Isolation (изоляция)", "Isolate (изолировать)", "Isolated (изолированный)"],
    ["Journal (журнал)", "Journalist (журналист)", "Journalistic (журналистский)"],
    ["Laughter (смех)", "Laugh (смеяться)", "Laughable (смешной)"],
    ["Leader (лидер)", "Lead (вести)", "Mislead (вводить в заблуждение)", "Leading (ведущий)"],
    ["Marvel (чудо)", "Marvelous (Чудесный)"],
    ["Mass (масса)", "Massive (огромный)"],
    ["Memory (память)", "Memorize (запоминать)", "Memorable (запоминающийся)"],
    ["Mountain (гора)", "Mountainous (гористый)"],
    ["Necessity (необходимость)", "Necessary (необходимый)", "Unnecessary (ненужный)"],
    ["Nerves (нервы)", "Nervous (нервный)"],
    ["Notice (уведомление)", "Notice (уведомлять)", "Noticed (замеченный)", "Unnoticed (незамеченный)"],
    ["Openness (открытость)", "Open (открытый)", "Openly (открыто)"],
    ["Operation (операция)", "Operator (оператор)", "Operate (оперировать)"],
    ["Originality (оригинальность)", "Origin (происхождение)", "Originate (происходить)", "Unoriginal (неоригинальный)",
     "Original (оригинальный)"],
    ["Paint (краска)", "Painting (картина)", "Paint (красить)"],
    ["Population (население)", "Populate (населять)"],
    ["Possession (владение)", "Possess (владеть)"],
    ["Practice (практика)", "Practise (практиковать)", "Practical (практиковать)", "Impractical (непрактичный)"],
    ["Preparation (подготовка)", "Prepare (готовиться)", "Preparatory (подготовительный)"],
    ["Prevention (предотвращение)", "Prevent (предотвращать)", "Preventive (превевнтивный)"],
    ["Profession (профессия)", "Professional (профессиональный)", "Unprofessional (непрофессиональный)"],
    ["Psychology (психология)", "Psychological (психологический)"],
    ["Punishment (наказание)", "Punish (наказывать)"],
    ["Quickness (скорость)", "Quicken (ускорять)", "Quick (быстрый)"],
    ["Relation (связь)", "Relate (связывать)", "Related (связанный)", "Unrelated (несвязанный)",
     "Relationship (отнощения)"],
    ["Religion (религия)", "Religious (религиозный)"],
    ["Reservation (бронирование)", "Reserve (забронировать)"],
    ["Rome (Рим)", "Roman (римский)"],
    ["Selection (выбор)", "Select (выбирать)"],
    ["Servant (слуга)", "Serve (служить)"],
    ["Shock (шок)", "Shock (шокировать)", "Shocking (шокирующий)"],
    ["Sail (плавать)", "Sailor (моряк)", "Sail (парус)"],
    ["Speaker (говорящий)", "Speech (речь)", "Speak (говорить)", "Spoken (разговорный)"],
    ["Specialty (специализация)", "Specialize (специализировать)", "Special (специальный)"],
    ["Strength (сила)", "Strong (сильный)"],
    ["Symbol (символ)", "Symbolize (символизировать)", "Symbolic (символический)"],
    ["Swimmer (пловец)", "Swim (плавать)"],
    ["Tropics (тропики)", "Tropical (тропический)"],
    ["Truth (правда)", "True (истинный)", "Truthful (верный)", "Untruthful (неверный)", "Truly (правдиво)"],
    ["Volcano (вулкан)", "Volcanic (вулканический)"],
    ["Width (широта)", "Wide (широкий)", "Widely (широко)"],
    ["Wood (дерево)", "Wooden (деревянный)"],
]


@dp.message_handler(commands=["start"], state="*")
# команда /start будет работать из любом состояния
# Обработчик команды /start для любого состояния

async def start_handler(message: types.Message):
    await message.answer(
        text="Hello, My Name is Alex! I Will Help You to Prepare for Your English Examinations. What exam will you take this year?",
        reply_markup=keyboard
    )

    # Функция для получения меню с кнопками


@dp.callback_query_handler(keyboard_callback.filter(), state="*")
async def button_handler(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    choice = callback_data["choice"]
    await call.message.answer(
        f"You Have Chosen {choice}! Tell Me a Word Whose Cognates (one-root words) You Would Like to Know... (example: Biology)")
    await bot.answer_callback_query(call.id)  # убирает часики с кнопки (завершает callback)

    await state.set_state("wait_for_key")


@dp.message_handler(state="wait_for_key")
async def _(message: types.Message, state: FSMContext):
    to_find = message.text
    found = None

    for lst in dictionary_list:
        for elem in lst:
            if to_find in elem.split():
                found = lst.copy()
                found.remove(elem)
                break
    if found is not None:
        await message.answer(f"{' '.join(found)}")
        await state.reset_state()
    else:
        await message.answer("The word was not found. Try again. \n(The word must start with a capital letter)")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dispatcher=dp, skip_updates=True)
