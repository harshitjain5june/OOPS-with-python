class Fraction:

    def __init__(self, n , d) -> None:
        self.den = d
        self.num = n



    # This magic method tells the compiler whenever someone whats to prints the value of Object of this class then run this method and show the value we mention inside this method.
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    

    # This magic method will run if someone tries to add two objects for example x = 5/6 and y = 7/8 , then if someone prints x+y then logic inside this method will run.
    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num,temp_den)