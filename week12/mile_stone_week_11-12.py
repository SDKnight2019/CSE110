import csv

# Loading Data
file_path = "life-expectancy.csv"

# Overall min/max life expectancy variables
overall_min_life = float("inf")
overall_max_life = float("-inf")
min_country = ""
max_country = ""
min_year = 0
max_year = 0

# Store data for year-specific calculations
year_data = {}

# Prompt the user for a year
user_year = int(input("\nEnter the year of interest: "))

# Read the dataset
with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        country = row[0]
        year = int(row[2])
        life_expectancy = float(row[3])

        # Check for overall min/max
        if life_expectancy < overall_min_life:
            overall_min_life = life_expectancy
            min_country = country
            min_year = year

        if life_expectancy > overall_max_life:
            overall_max_life = life_expectancy
            max_country = country
            max_year = year

        # Store data per year
        if year not in year_data:
            year_data[year] = []
        year_data[year].append((country, life_expectancy))

# Display overall statistics
print(f"\nThe overall max life expectancy is: {overall_max_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {overall_min_life} from {min_country} in {min_year}")

# Check if the user-specified year exists in the dataset
if user_year in year_data:
    life_expectancies = [data[1] for data in year_data[user_year]]
    avg_life = sum(life_expectancies) / len(life_expectancies)

    min_country, min_life = min(year_data[user_year], key=lambda x: x[1])
    max_country, max_life = max(year_data[user_year], key=lambda x: x[1])

    # Display results for the selected year
    print(f"\nFor the year {user_year}:")
    print(f"The average life expectancy across all countries was {avg_life:.2f}")
    print(f"The max life expectancy was in {max_country} with {max_life:.2f}")
    print(f"The min life expectancy was in {min_country} with {min_life:.2f}")

else:
    print("Year not found in the dataset.")
    