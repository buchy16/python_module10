from typing import List


test_values = [23, 24, 23]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def speel_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(target: str) -> tuple:
        return (spell1(target), spell2(target))

    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def multiplicate(og_power) -> tuple:
        return (og_power, base_spell(og_power) * multiplier)

    return multiplicate


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast(mana: int) -> str:
        return spell(mana) if condition(mana) is True else "Spell fizzled"

    return cast


def spell_sequence(spells: List[callable]) -> callable:
    def cast_multiple(mana: int) -> List[str]:
        return [(spell(mana)) for spell in spells]

    return cast_multiple

# =============================================================================
# =============================================================================
# =============================================================================


def cast_earthquake(mana: int) -> str:
    return (f"earthquake casted with {mana} mana")


def cast_earthquake_condition(mana: int) -> bool:
    return (True if mana >= 3 else False)


def cast_fireball(mana: int) -> str:
    return (f"fireball casted with {mana} mana")


def cast_tornado(mana: int) -> str:
    return (f"tornado casted with {mana} mana")


def tornado(og_power) -> int:
    return og_power


def fireball(target: str):
    return f"Fireball hits {target}"


def heal(target: str):
    return f"Heals {target}"


if (__name__ == "__main__"):
    print("Testing spell combiner...")
    combined = speel_combiner(fireball, heal)
    speel_combined = combined(test_targets[0])
    print(f"Combined spell result: {speel_combined[0]}, {speel_combined[1]}\n")

    print("Testing power amplifier...")
    amplificator = power_amplifier(tornado, 3)
    amplified_result = amplificator(10)
    print(f"Original: {amplified_result[0]}, Amplified: {amplified_result[1]}")
    print()

    print("Testing conditional caster")
    caster = conditional_caster(cast_earthquake_condition, cast_earthquake)
    cast_result = caster(4)
    print(cast_result, "\n")

    print("Testing  spell sequence...")
    ultimate_caster = spell_sequence([cast_earthquake, cast_fireball,
                                      cast_tornado])
    cast_result = ultimate_caster(5)
    for result in cast_result:
        print(result)
