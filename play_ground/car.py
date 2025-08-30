class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def describe(self) -> str:
        return f"{self.year} {self.color} {self.model} (for sale: {self.for_sale})"

    def drive(self):
        print(f"The {self.year} {self.color} {self.model} is Driving")

    def stop(self):
        print(f"The {self.year} {self.color} {self.model} is Stopped")
