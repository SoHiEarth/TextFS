class World:
    def Gravity(Strength,State="Calc"):
        if State == "Init":
            print("Gravity is set to",Strength,"m/s.")
    def Speed(W,Cd,EP,Area,AD):
        import math
        velocity = math.sqrt((2 * EP) / (AD * Area * Cd))
        return velocity
    def AirResistance(A,Cd,spd,p):
        data = (p*Cd*A)/2*spd*spd
        return data
    