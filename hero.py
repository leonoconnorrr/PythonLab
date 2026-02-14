class Battle:

    def __init__(self, throw, receive, weapon):
        self.throw = throw
        self.receive = receive
        self.weapon = weapon

    def action(self):
        print(f"{self.throw} throws {self.weapon} and {self.receive} catches it.")

    def start(self, action):
        action()

battle1 = Battle("Thor", "Captain America", "Mjolnir")

battle1.start(battle1.action)
