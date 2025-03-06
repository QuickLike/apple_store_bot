from aiogram.fsm.state import State, StatesGroup


class CartStates(StatesGroup):
    waiting_for_quantity = State()


class CheckoutStates(StatesGroup):
    waiting_for_address = State()
