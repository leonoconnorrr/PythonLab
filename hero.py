class Battle:

    def __init__(self, throw, receive, weapon):
        self.throw = throw
        self.receive = receive
        self.weapon = weapon

    def action(self):
        print(f"{self.throw} throws {self.weapon} and {self.receive} catches it.")

battle1 = Battle("Thor", "Captain America", "Mjolnir")

battle1.action()





