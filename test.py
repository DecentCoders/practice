class person:
    name = "Hridoy"
    occupation = "Developer"
    net_worth = 10
    def test(self):
        print(f"{self.name} is a {self.occupation}")
a = person()
a.test()