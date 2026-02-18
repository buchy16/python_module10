from typing import List, Dict


artifacts = [
    {'name': 'Light Prism', 'power': 96, 'type': 'armor'},
    {'name': 'Water Chalice', 'power': 104, 'type': 'accessory'},
    {'name': 'Shadow Blade', 'power': 109, 'type': 'accessory'},
    {'name': 'Shadow Blade', 'power': 65, 'type': 'armor'}
    ]

mages = [
    {'name': 'Rowan', 'power': 99, 'element': 'shadow'},
    {'name': 'River', 'power': 96, 'element': 'fire'},
    {'name': 'River', 'power': 89, 'element': 'earth'},
    {'name': 'Rowan', 'power': 98, 'element': 'earth'},
    {'name': 'Nova', 'power': 60, 'element': 'lightning'}
    ]

spells = ['tsunami', 'blizzard', 'fireball', 'freeze']


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spell: List[str]) -> List[str]:
    return list(map(lambda x: "*" + x + "*", spell))


def mage_stats(mages: List[Dict]) -> Dict:
    return {
        "max_power": max(mages, key=lambda x: x["power"])["power"],
        "min_power": min(mages, key=lambda x: x["power"])["power"],
        "avg_power": sum(map(lambda x: x["power"], mages)) / len(mages)
    }


if (__name__ == "__main__"):
    print("Testing artifact sorter...")
    sorted_artifact = artifact_sorter(artifacts)
    print(f"{sorted_artifact[0]['name']} ({sorted_artifact[0]['power']}) \
come befor {sorted_artifact[1]['name']} ({sorted_artifact[1]['power']})")
    print()

    print("Testing power filter...")
    mages_filtered = power_filter(mages, 90)
    for mage in mages_filtered:
        print(f"{mage['name']} ({mage['power']})")
    print()

    print("Testing spell transformer....")
    spell_transformed = spell_transformer(spells)
    print(f"{''.join([spell + ' ' for spell in spell_transformed])}")
    print()

    print("Testing mage stast")
    stats = mage_stats(mages)
    print(f"max power: {stats['max_power']}")
    print(f"min power: {stats['min_power']}")
    print(f"avg power: {stats['avg_power']}")
