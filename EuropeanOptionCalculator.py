# This program is to calculate European option's theoretical price
# Given the program uses Black-Scholes equation, American option cannot be calculated by it

# Necessary Packages
from scipy.stats import norm
import math

# Call Option
def Call(s, e, r, d, t, v):
    # s: stock price or the underlying asset price
    # e: strike price of the option
    # r: risk-free interest rate
    # d: dividend yield
    # t: time left to maturity (in days but annualized after)
    # v: volatility
    # Endogenous Parameters
    t = t / 242 # For A-share market
    d1 = (math.log(s/e) + (r - d + 0.5*(v**2))*t)/(v*(t**0.5))
    d2 = d1 - v*(t**0.5)
    # Calculating
    c = s*math.exp(-d*t)*norm.cdf(d1) - e*math.exp(-r*t)*norm.cdf(d2)
    # Greeks
    delta = math.exp(-d*t)*norm.cdf(d1)
    gamma = (math.exp(-d*t)*Nprime(d1))/(v*s*math.sqrt(t))
    theta = (-((v*s*math.exp(-d*t)*Nprime(d1)))/(2*math.sqrt(t)) + d*s*norm.cdf(d1)*math.exp(-d*t) - r*e*math.exp(-r*t)*norm.cdf(d2)) / 242
    speed = -((math.exp(-d*t)*Nprime(d1))/(v**2 * s**2 * t)) * (d1 + v*math.sqrt(t))
    vega = (s*math.sqrt(t)*math.exp(-d*t)*Nprime(d1)) / 100
    rho = e*t*math.exp(-r*t)*norm.cdf(d2)
    # Print results
    print('=== === === === === === === ===')
    print('Theoretical Price:', c)
    print('Delta:', delta)
    print('Gamma:', gamma)
    print('Theta:', theta)
    print('Speed:', speed)
    print('Vega:', vega)
    print('Rho:', rho)
    print('=== === === === === === === ===')

def Put(s, e, r, d, t, v):
    t = t / 242 # For A-share market
    # Endogenous Parameters
    d1 = (math.log(s/e) + (r - d + 0.5*(v**2))*t)/(v*(t**0.5))
    d2 = d1 - v*(t**0.5)
    # Calculating
    c = -s*math.exp(-d * t)*norm.cdf(-d1) + e*math.exp(-r * t)*norm.cdf(-d2)
    # Greeks
    delta = math.exp(-d*t)*(norm.cdf(d1) - 1)
    gamma = ((math.exp(-d*t)*Nprime(d1))/(v*s*math.sqrt(t)))
    theta = ((-((v*s*math.exp(-d*t)*Nprime(-d1))/(2*math.sqrt(t)))) - d*s*norm.cdf(-d1)*math.exp(-d*t) + r*e*math.exp(-r*t)*norm.cdf(-d2)) / 242
    speed = -((math.exp(-d*t)*Nprime(d1))/(v**2 * s**2 * t)) * (d1 + v*math.sqrt(t))
    vega = (s*math.sqrt(t)*math.exp(-d*t)*Nprime(d1)) / 100
    rho = -e*t*math.exp(-r*t)*norm.cdf(-d2)
    # Print results
    print('=== === === === === === === ===')
    print('Theoretical Price:', c)
    print('Delta:', delta)
    print('Gamma:', gamma)
    print('Theta:', theta)
    print('Speed:', speed)
    print('Vega:', vega)
    print('Rho:', rho)
    print('=== === === === === === === ===')

def BinaryCall(s, e, r, d, t, v):
    t = t / 242 # For A-share market
    # Endogenous Parameters
    d1 = (math.log(s/e) + (r - d + 0.5*(v**2))*t)/(v*(t**0.5))
    d2 = d1 - v*(t**0.5)
    # Calculating
    c = math.exp(-r*t)*norm.cdf(d2)
    # Greeks
    delta = (math.exp(-r*t)*Nprime(d2))/(v*s*math.sqrt(t))
    gamma = (-((math.exp(-r*t)*d1*Nprime(d2))/(v**2 * s**2 * t)))
    theta = (r*math.exp(-r*t)*norm.cdf(d2) + math.exp(-r*t)*Nprime(d2)*(d1/(2*t) - (r-d)/(v*math.sqrt(t)))) / 242
    speed = -((math.exp(-r*t)*Nprime(d2))/(v**2 * s**3 * t)) * (-2*d1 + (1 - d1*d2)/(v*math.sqrt(t)))
    vega = (-math.exp(-r*t)*Nprime(d2)*(d1/v)) / 100
    rho = -t*math.exp(-r*t)*norm.cdf(d2) + (t/v)*math.exp(-r*t)*Nprime(d2)
    # Print results
    print('=== === === === === === === ===')
    print('Theoretical Price:', c)
    print('Delta:', delta)
    print('Gamma:', gamma)
    print('Theta:', theta)
    print('Speed:', speed)
    print('Vega:', vega)
    print('Rho:', rho)
    print('=== === === === === === === ===')

def BinaryPut(s, e, r, d, t, v):
    t = t / 242 # For A-share market
    # Endogenous Parameters
    d1 = (math.log(s/e) + (r - d + 0.5*(v**2))*t)/(v*(t**0.5))
    d2 = d1 - v*(t**0.5)
    # Calculating
    c = math.exp(-r*t)*(1 - norm.cdf(d2))
    # Greeks
    delta = -((math.exp(-r*t)*Nprime(d2))/(v*s*math.sqrt(t)))
    gamma = ((math.exp(-r*t)*d1*Nprime(d2))/(v**2 * s**2 * t))
    theta = (r*math.exp(-r*t)*(1 - 2*norm.cdf(d2)) - math.exp(-r*t)*Nprime(d2)*(d1/(2*t) - (r-d)/(v*math.sqrt(t)))) / 242
    speed = (math.exp(-r*t)*Nprime(d2))/(v**2 * s**3 * t) * (-2*d1 + (1 - d1*d2)/(v*math.sqrt(t)))
    vega = (math.exp(-r*t)*Nprime(d2)*(d1/v)) / 100
    rho = -t*math.exp(-r*t)*(1-norm.cdf(d2)) - (t/v)*math.exp(-r*t)*Nprime(d2)
    # Print results
    print('=== === === === === === === ===')
    print('Theoretical Price:', c)
    print('Delta:', delta)
    print('Gamma:', gamma)
    print('Theta:', theta)
    print('Speed:', speed)
    print('Vega:', vega)
    print('Rho:', rho)
    print('=== === === === === === === ===')

# Main Program
# Select what type of option is to be priced
selection = input('What type of option do you want to price? Choose 1 for call, 2 for put, 3 for binary call, 4 for binary put:')
selection = int(selection)

# Exdogenous Parameters
s = input('How much is the stock or underlying asset right now:')
e = input('How much is your strike price:')
r = input('How large is the risk-free interest rate:')
d = input('How large is the dividend yield of the underlying asset:')
t = input('How long will your option mature (in days):')
v = input('How large is the volatility of the underlying asset:')

# Convert them to float
s = float(s)
e = float(e)
r = float(r)
d = float(d)
t = float(t)
v = float(v)

# Define N' function
def Nprime(x):
    Nprime = 1/(math.sqrt(2*math.pi))*math.exp(-0.5*(x**2))
    return Nprime

# Calculate
if selection == 1:
    Call(s, e, r, d, t, v)
elif selection == 2:
    Put(s, e, r, d, t, v)
elif selection == 3:
    BinaryCall(s, e, r, d, t, v)
elif selection == 4:
    BinaryPut(s, e, r, d, t, v)
else:
    print('Oops! It seems that you went wrong with the selection of type of option, just try again!')
