from breezypythongui import EasyFrame
import random


class LottoNumbers(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Lotto Number Generator")

        self.addLabel(text="Lotto Number Generator", sticky="S", column=0, row=0).config(font="Arial")

        self.addLabel(text="Your Lotto Numbers Are:", sticky="W", column=0, row=1)

        self.num1 = self.addIntegerField(value="", row=2, column=0, sticky="W", state="readonly", width=3)
        self.num2 = self.addIntegerField(value="", row=3, column=0, sticky="W", state="readonly", width=3)
        self.num3 = self.addIntegerField(value="", row=4, column=0, sticky="W", state="readonly", width=3)
        self.num4 = self.addIntegerField(value="", row=5, column=0, sticky="W", state="readonly", width=3)
        self.num5 = self.addIntegerField(value="", row=6, column=0, sticky="W", state="readonly", width=3)

        self.addLabel(text="And your powerball number is:", row=7, column=0)

        self.powerball = self.addIntegerField(value="", row=8, column=0, sticky="W", width=3)

        self.addButton(text="Click to generate numbers", row=9, column=0, command=self.generate)

    def generate(self):
        nums = random.sample(range(1, 69), 5)
        powerball = random.randint(1, 26)
        self.num1.setNumber(nums[0])
        self.num2.setNumber(nums[1])
        self.num3.setNumber(nums[2])
        self.num4.setNumber(nums[3])
        self.num5.setNumber(nums[4])
        self.powerball.setNumber(powerball)
        self.powerball["background"] = "Red"


def main():
    LottoNumbers().mainloop()


if __name__ == "__main__":
    main()