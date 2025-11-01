class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str = "NotVaccinatedError") -> None:
        super().__init__(name)


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(name)
