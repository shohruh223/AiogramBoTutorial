import random
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.default.level_keyboard import stop_button, level_button
from loader import dp
from states.level import LevelState


@dp.message_handler(state=LevelState.level)
async def lvl_handler(msg: types.Message, state: FSMContext):
    if msg.text == "LEVEL 1️⃣":
        question = f"{random.randrange(1, 11)} {random.choice(['+', '-', '*'])} {random.randrange(1, 11)}"
        answer = eval(question)
    elif msg.text == "LEVEL 2️⃣":
        question = f"{random.randrange(1, 51)} {random.choice(['+', '-', '*'])} {random.randrange(1, 51)}"
        answer = eval(question)
    elif msg.text == "LEVEL 3️⃣":
        question = f"{random.randrange(1, 101)} {random.choice(['+', '-', '*'])} {random.randrange(1, 101)}"
        answer = eval(question)
    elif msg.text == "LEVEL 4️⃣":
        question = f"{random.randrange(1, 101)} {random.choice(['+', '-', '*', '/'])} {random.randrange(1, 101)}"
        answer = eval(question)

    async with state.proxy() as data:
        data["answer"] = answer
        data['level'] = msg.text
        data['true'] = 0
        data['false'] = 0
    await LevelState.next()
    await msg.answer(f"SAVOL : {question}  = ?", reply_markup=stop_button())


@dp.message_handler(Text("🛑 Stop"), state=LevelState.answer)
async def stop_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        true_answer = data.get("true")
        false_answer = data.get("false")

    text = f"""{data.get("level")}
Savolarning soni : {int(true_answer) + int(false_answer)}:
✅ : {true_answer}
❌ : {false_answer}"""
    await state.finish()
    await msg.answer(text,
                     reply_markup=level_button())


@dp.message_handler(state=LevelState.answer)
async def start_test(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if data.get("answer") == int(msg.text):
            data["true"] += 1
            await msg.answer("✅")
        else:
            data["false"] += 1
            await msg.answer("❌")

        if data.get('level') == "LEVEL 1️⃣":
            question = f"{random.randrange(1, 11)} {random.choice(['+', '-', '*'])} {random.randrange(1, 11)}"
            answer = eval(question)
        elif data.get('level') == "LEVEL 2️⃣":
            question = f"{random.randrange(1, 51)} {random.choice(['+', '-', '*'])} {random.randrange(1, 51)}"
            answer = eval(question)
        elif data.get('level') == "LEVEL 3️⃣":
            question = f"{random.randrange(1, 101)} {random.choice(['+', '-', '*'])} {random.randrange(1, 101)}"
            answer = eval(question)
        elif data.get('level') == "LEVEL 4️⃣":
            question = f"{random.randrange(1, 101)} {random.choice(['+', '-', '*', '/'])} {random.randrange(1, 101)}"
            answer = eval(question)

        data["answer"] = answer

    await LevelState.answer.set()
    await msg.answer(f"SAVOL : {question}  = ?", reply_markup=stop_button())

