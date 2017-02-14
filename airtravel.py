
class Flight:

    def __init__(self, number, aircraft):
        self._number=number
        self._aircraft=aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.registration()

class Aircraft:

    def __init__(self, registration):
        self._registration=registration

    def registration(self):
        return self._registration

    print("hi")
    print("hi again")
