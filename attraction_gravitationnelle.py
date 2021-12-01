#from test_class_planètes import *

G = 6.7e10-11 #[m^3/(kg^-1*s^-2)]

def Fg(mass_planète, x_Asteroid_crash_test, y_Asteroid_crash_test, x_planéte, y_planète):
    r_carre = (x_Asteroid_crash_test-x_planéte)**2 + (y_Asteroid_crash_test-y_planète)**2
    Force_gravita = (G * Asteroid_crash_test.mass * mass_planète) / r_carre
    return Force_gravita


