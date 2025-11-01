import datetime


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name


    def visit_cafe(self, visitor: dict) :
        if not visitor["vaccine"]:
            raise NotVaccinatedError

        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError

        elif not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        else:
            return f"Welcome to {self.name}"


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    without_mask = False
    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except NotVaccinatedError:
            return "All friends should be vaccinated"

        except NotWearingMaskError:
            masks_to_buy += 1
            without_mask = True

    if without_mask:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"

kfc = Cafe("KFC")

friends = [
    {
        "name": "Alisa",
        "wearing_a_mask": True
    },
    {
        "name": "Bob",
        "vaccine": {
            "expiration_date": datetime.date.today()
        },
        "wearing_a_mask": True
    },
]
print(go_to_cafe(friends=friends, cafe=Cafe("KFC")))