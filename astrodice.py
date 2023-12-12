import random

def generate_reading(prompt):
    planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Sun', 'Moon', 'North Node', 'South Node']
    houses = ['First House', 'Second House', 'Third House', 'Fourth House', 'Fifth House', 'Sixth House', 'Seventh House', 'Eighth House', 'Ninth House', 'Tenth House', 'Eleventh House', 'Twelfth House']
    signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

    random_planet = random.choice(planets)
    random_house = random.choice(houses)
    random_sign = random.choice(signs)

    return f"Your reading for '{prompt}': {random_planet} in {random_house} in {random_sign}."

# Example usage
prompt = input("Enter your query: ")
reading = generate_reading(prompt)
print(reading)
