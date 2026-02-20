from functools import wraps
from time import time


test_powers = [14, 24, 20, 25]
spell_names = ['fireball', 'flash', 'heal', 'meteor']
mage_names = ['River', 'Alex', 'Casey', 'Nova', 'Rowan', 'Storm']
invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']


class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper() -> str:
        print(f"Casing {func.__name__}...")
        start = time()
        result = func()
        end = time()
        print(f"Spell completed in {'{:.7f}'.format(end - start)} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:

    def actual_decorator(func: callable):

        @wraps(func)
        def wrapper(*args, **kwargs):
            if (args[0] >= min_power):
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return actual_decorator


def retry_spell(max_attempts: int) -> callable:

    def actual_decorator(func: callable):

        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            attempt = 1
            mana = args[0]
            while (attempt <= max_attempts):
                try:
                    mana += 1
                    return func(mana, **kwargs)
                except Exception as e:
                    print(f"{e} ,retrying... (attempt {attempt}/{max_attempts})")
                attempt += 1
            return f"Spell casting failed after {max_attempts}"

        return wrapper

    return actual_decorator


# =============================================================================
# =============================================================================
# =============================================================================

@spell_timer  # fireball() = spell(fireball)
def fireball() -> str:
    return "Fireball cast !"


@power_validator(5)
# cast_f_with_power = power_validator(5) = actual_decorator(cast_f_with_power)
def cast_f_with_power(power: int) -> str:
    return "Fireball casted successfully"


@retry_spell(5)
def cast_l_with_power(power: int):
    if power < 8:
        raise Exception("Spell failed")
    return "lightning casted successfully"


if (__name__ == "__main__"):
    print("Testing spell timer...")
    print(f"Result {fireball()}\n")

    print("Testing power validator...")
    print(f"casting fireball with 8 mana: {cast_f_with_power(8)}")
    print(f"casting fireball with 2 mana: {cast_f_with_power(2)}")

    print("Testing retry spell")
    print(f"Trying casting lightning spell: {cast_l_with_power(1)}")

# https://www.geeksforgeeks.org/python/functools-module-in-python/
# https://www.geeksforgeeks.org/python/decorators-in-python/