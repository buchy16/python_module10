from functools import reduce, partial, lru_cache, singledispatch
from typing import Dict, List, Any
from operator import add, mul


spell_powers = [15, 21, 21, 44, 27, 11]
operations = ['add', 'multiply', 'max', 'min']


def spell_reducer(spells: List[int], operation: str) -> int:
    if operation == "add":
        return reduce(lambda a, b: add(a, b), spells)
    if operation == "multiply":
        return reduce(lambda a, b: mul(a, b), spells)
    if operation == "max":
        return reduce(lambda a, b: max(a, b), spells)
    if operation == "min":
        return reduce(lambda a, b: min(a, b), spells)


def partial_enchanter(base_enchantment: callable) -> Dict[str, callable]:
    return {
        "fire_enchant":
        partial(base_enchantment, 50, "fire"),
        "ice_enchant":
        partial(base_enchantment, 50, "ice"),
        "lightning_enchant":
        partial(base_enchantment, 50, "lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> callable:
    @singledispatch
    def spell_system(args: Any) -> str:
        return f"{args}Unknown manipulation, \
please refer to the ancestral magaique book"

    @spell_system.register(int)
    def _(args: int) -> str:
        return f"spell deal {args} damages"

    @spell_system.register(str)
    def _(args: str) -> str:
        return f"spell enchante object with {args}"

    @spell_system.register(list)
    def _(args: List[str]) -> str:
        result = ""
        for spell in args:
            result += f"casted {spell}, "
        return result
    return spell_system


# =============================================================================
# =============================================================================
# =============================================================================


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"enchantment {element} applied to {target} with a power of {power}"


if (__name__ == "__main__"):
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, operations[0])}")
    print(f"Product: {spell_reducer(spell_powers, operations[1])}")
    print(f"Max: {spell_reducer(spell_powers, operations[2])}")
    print(f"Min: {spell_reducer(spell_powers, operations[3])}\n")

    print("Testing partial enchanter...")
    enchanter = partial_enchanter(base_enchantment)
    print(f"1. {enchanter['fire_enchant']('Homonculus Lust')}")
    print(f"1. {enchanter['ice_enchant']('Goblin')}")
    print(f"1. {enchanter['lightning_enchant']('Dragon')}\n")

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    # print(f"debug --- {memoized_fibonacci.cache_info()}")
    print(f"Fib(15): {memoized_fibonacci(15)}\n")

    print("Testing spell_dispatcher...")
    caster = spell_dispatcher()
    print(f"Fireball damage: {caster(10)}")
    print(f"Enchanting sword: {caster('unbreakingIII')}")
    print(f"Casting multiple spell: \
{caster(['Fireball', 'poison', 'lightning'])}")
