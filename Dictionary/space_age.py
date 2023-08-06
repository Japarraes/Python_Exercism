class SpaceAge:
    
    def __init__(self, seconds):
        self.seconds = seconds
    
    def on_mercury(self):
        return round(self.seconds / 31557600 / 0.2408467, 2)
    
    def on_venus(self):
        return round(self.seconds / 31557600 / 0.61519726, 2)
    
    def on_earth(self):
        return round(self.seconds / 31557600, 2)
    
    def on_mars(self):
        return round(self.seconds / 31557600 / 1.8808158, 2)
    
    def on_jupiter(self):
        return round(self.seconds / 31557600 / 11.862615, 2)
    
    def on_saturn(self):
        return round(self.seconds / 31557600 / 29.447498, 2)
    
    def on_uranus(self):
        return round(self.seconds / 31557600 / 84.016846, 2)
    
    def on_neptune(self):
        return round(self.seconds / 31557600 / 164.79132, 2)

print(SpaceAge(1000000000).on_earth())      # 31.69
print(SpaceAge(2134835688).on_mercury())    # 280.88
print(SpaceAge(189839836).on_venus())       # 9.78
print(SpaceAge(2129871239).on_mars())       # 35.88
print(SpaceAge(901876382).on_jupiter())     # 2.41
print(SpaceAge(2000000000).on_saturn())     # 2.15
print(SpaceAge(1210123456).on_uranus())     # 0.46
print(SpaceAge(1821023456).on_neptune())    # 0.35