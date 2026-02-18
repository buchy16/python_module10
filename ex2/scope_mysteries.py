from typing import Dict, Any


initial_powers = [46, 30, 66]
power_additions = [8, 15, 19, 17, 15]
enchantment_types = ['Flaming', 'Earthen', 'Radiant']
items_to_enchant = ['Shield', 'Sword', 'Wand', 'Armor']


def mage_counter() -> callable:
    call_count = 0

    def counter() -> str:
        nonlocal call_count
        call_count += 1
        return f"Call {call_count}: {call_count}"

    return counter


def spell_accumulator(initial_power: int) -> callable:
    def accumulator(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(name: int) -> str:
        nonlocal enchantment_type
        return f"{enchantment_type} {name}"

    return enchant


def memory_vault() -> Dict[str, callable]:
    securised_dict = {}

    def store(key: Any, value: Any) -> None:
        nonlocal securised_dict
        securised_dict[key] = value

    def recall(key: Any) -> Any:
        nonlocal securised_dict
        value = securised_dict.get(key)
        if (value is None):
            return "Memory not found"
        return value

    return {"recall": recall, "store": store}


# =============================================================================
# =============================================================================
# =============================================================================


if (__name__ == "__main__"):
    print("Testing mage counter...")
    count_function = mage_counter()
    for k in range(9):
        print(count_function())
    print()

    print("Testing spell acumulator...")
    accumulator = spell_accumulator(initial_powers[0])
    for k in range(10):
        print(accumulator(2))
    print()

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    for name in ["Sword", "Shield"]:
        print(flaming(name))
        print(frozen(name))
    print()

    print("Testing memory vault")
    f = memory_vault()

    print("adding 'song1': 'Virtual Insanity' to the securised dict")
    f["store"]("song1", "Virtual Insanity")
    print("Accessing 'song1' from securised dict")
    print(f["recall"]("song1"))
    print("Accessing 'song2' from securised dict")
    print(f["recall"]("song2"))
