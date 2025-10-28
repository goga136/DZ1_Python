from smartphone import Smartphone

smartphone = Smartphone("Nokia", "Nokia1", "+79211234567")

catalog = [
    Smartphone("Nokia", "Nokia 8800", "+79212223333"),
    Smartphone("Nokia", "Nokia 6600", "+79213334444"),
    Smartphone("Nokia", "Nokia 2025", "+79214445555"),
    Smartphone("Nokia", "Nokia 3310", "+79215556666"),
    Smartphone("Nokia", "Nokia 7610", "+79216667777")
]

for smartphone in catalog:
    print(f"{smartphone.brand}, {smartphone.model},{smartphone.number_tlf}")
