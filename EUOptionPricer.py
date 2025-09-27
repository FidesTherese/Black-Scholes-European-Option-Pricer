# This is a new version of European option calculator that is based on Black-Scholes formulae.
# American option etc. could not be used in this program.

# Necessary Packages
from scipy.stats import norm
import math

# Exdogenous Parameters
print('--- --- --- --- ---')
print('Please input exdogenous parameters that is necessary to calculate.')
print('--- --- --- --- ---')
s = input('Underlying Asset Mkt-Price:')
e = input('Strike Price:')
r = input('Risk-Free Interest Rate (%):')
d = input('Dividend Yield (%):')
t = input('Days until Expiration:')
v = input('Volatility (%):')

# Convert them to float
s = float(s)
e = float(e)
r = float(r)
d = float(d)
t = float(t)
v = float(v)

# Convert some parameters to decimal
r = r / 100
d = d / 100
v = v / 100

# Annualize Days
t = t / 365

# Endogenous Parameters
d1 = (math.log(s/e) + (r - d + 0.5*(v**2))*t)/(v*(t**0.5))
d2 = d1 - v*(t**0.5)

# Define N' function
def Nprime(x):
    Nprime = 1/(math.sqrt(2*math.pi))*math.exp(-0.5*(x**2))
    return Nprime

# Results
print('\n')
print('\n')
print('\n')
print('===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====')
# For Call
print('European Call Option')
print('\n')
print('Theoretical Price:', s*math.exp(-d*t)*norm.cdf(d1) - e*math.exp(-r*t)*norm.cdf(d2))
print('Delta:', math.exp(-d*t)*norm.cdf(d1))
print('Gamma:', (math.exp(-d*t)*Nprime(d1))/(v*s*math.sqrt(t)))
print('Speed:', -((math.exp(-d*t)*Nprime(d1))/(v**2 * s**2 * t)) * (d1 + v*math.sqrt(t)))
print('Theta:', (-((v*s*math.exp(-d*t)*Nprime(d1))/(2*math.sqrt(t))) + d*s*norm.cdf(d1)*math.exp(-d*t) - r*e*math.exp(-r*t)*norm.cdf(d2)) / 365)
print('Vega:', (s*math.sqrt(t)*math.exp(-d*t)*Nprime(d1)) / 100)
print('Rho:', e*t*math.exp(-r*t)*norm.cdf(d2) / 100)
# For Put
print('--- --- --- --- ---')
print('European Put Option')
print('\n')
print('Theoretical Price:', -s*math.exp(-d * t)*norm.cdf(-d1) + e*math.exp(-r * t)*norm.cdf(-d2))
print('Delta:', math.exp(-d*t)*(norm.cdf(d1) - 1))
print('Gamma:', ((math.exp(-d*t)*Nprime(d1))/(v*s*math.sqrt(t))))
print('Speed:', -((math.exp(-d*t)*Nprime(d1))/(v**2 * s**2 * t)) * (d1 + v*math.sqrt(t)))
print('Theta:', ((-((v*s*math.exp(-d*t)*Nprime(-d1))/(2*math.sqrt(t)))) - d*s*norm.cdf(-d1)*math.exp(-d*t) + r*e*math.exp(-r*t)*norm.cdf(-d2)) / 365)
print('Vega:', (s*math.sqrt(t)*math.exp(-d*t)*Nprime(d1)) / 100)
print('Rho:', -e*t*math.exp(-r*t)*norm.cdf(-d2) / 100)
# For European Binary Call
print('--- --- --- --- ---')
print('European Binary Call Option')
print('\n')
print('Theoretical Price:', math.exp(-r*t)*norm.cdf(d2))
print('Delta:', (math.exp(-r*t)*Nprime(d2))/(v*s*math.sqrt(t)))
print('Gamma:', (-((math.exp(-r*t)*d1*Nprime(d2))/(v**2 * s**2 * t))))
print('Speed:', -((math.exp(-r*t)*Nprime(d2))/(v**2 * s**3 * t)) * (-2*d1 + (1 - d1*d2)/(v*math.sqrt(t))))
print('Theta:', (r*math.exp(-r*t)*norm.cdf(d2) + math.exp(-r*t)*Nprime(d2)*(d1/(2*t) - (r-d)/(v*math.sqrt(t)))) / 365)
print('Vega (Useless in Practice):', (-math.exp(-r*t)*Nprime(d2)*(d1/v)) / 100)
print('Rho (Useless in Practice):', -t*math.exp(-r*t)*norm.cdf(d2) + (t/v)*math.exp(-r*t)*Nprime(d2) / 100)
# For European Binary Put
print('--- --- --- --- ---')
print('European Binary Put Option')
print('\n')
print('Theoretical Price:', math.exp(-r*t)*(1 - norm.cdf(d2)))
print('Delta:', -((math.exp(-r*t)*Nprime(d2))/(v*s*math.sqrt(t))))
print('Gamma:', ((math.exp(-r*t)*d1*Nprime(d2))/(v**2 * s**2 * t)))
print('Speed:', (math.exp(-r*t)*Nprime(d2))/(v**2 * s**3 * t) * (-2*d1 + (1 - d1*d2)/(v*math.sqrt(t))))
print('Theta:', (r*math.exp(-r*t)*(1 - 2*norm.cdf(d2)) - math.exp(-r*t)*Nprime(d2)*(d1/(2*t) - (r-d)/(v*math.sqrt(t)))) / 365)
print('Vega (Useless in Practice):', (math.exp(-r*t)*Nprime(d2)*(d1/v)) / 100)
print('Rho (Useless in Practice):', -t*math.exp(-r*t)*(1-norm.cdf(d2)) - (t/v)*math.exp(-r*t)*Nprime(d2) / 100)
print('===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====')