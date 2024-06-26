from faker import Faker
import random
from fantasy_examples import faction_data, region_data, house_data, warriors

faker = Faker()

def generate_unique_code(existing_codes):
    while True:
        code = ''.join(faker.random_choices(elements='ABCDEFGHIJKLMNOPQRSTUVWXYZ', length=4))
        if code not in existing_codes:
            existing_codes.add(code)
            return code

def generate_faction(existing_codes):
    code = generate_unique_code(existing_codes)
    name = faker.catch_phrase()
    description = faker.sentence(nb_words=10)
    return (code, name, description)

def generate_region(existing_codes):
    code = generate_unique_code(existing_codes)
    name = faker.city()
    description = faker.sentence(nb_words=12)
    return (code, name, description)

def generate_house(existing_codes):
    code = generate_unique_code(existing_codes)
    name = f"House {faker.last_name()}"
    description = faker.sentence(nb_words=10)
    return (code, name, description)




# Provided example data


# Track existing codes to ensure uniqueness
existing_faction_codes = {code for code, _, _ in faction_data}
existing_region_codes = {code for code, _, _ in region_data}
existing_house_codes = {code for code, _, _ in house_data}

# Generate additional entries
additional_factions = [generate_faction(existing_faction_codes) for _ in range(10)]
additional_regions = [generate_region(existing_region_codes) for _ in range(10)]
additional_houses = [generate_house(existing_house_codes) for _ in range(10)]

# Combine provided data with additional entries
all_factions = faction_data + additional_factions
all_regions = region_data + additional_regions
all_houses = house_data + additional_houses

print("All Factions:", all_factions)
print("All Regions:", all_regions)
print("All Houses:", all_houses)

