#//DIRECTORY\\#
filename = "life-expectancy.csv" #(make sure the path is right)

year_of_interest = input("Enter the year of interest: ").strip()
country_of_interest = input("Enter a country of interest (or press Enter to skip): ").strip().lower()

#//CALC\\# overall
overall_min = float('inf')
overall_max = float('-inf')
overall_min_country = ""
overall_min_year = 0
overall_max_country = ""
overall_max_year = 0
#year\
year_total = 0
year_count = 0
year_min = float('inf')
year_max = float('-inf')
year_min_country = ""
year_max_country = ""
# country
country_total = 0
country_count = 0
country_min = float('inf')
country_max = float('-inf')
country_min_year = 0
country_max_year = 0
life_exp_that_year = None

#//FUNCTION\\# -------------------------------------------------------------------------------------------------
with open(filename, "r") as file:
    next(file)  # skips the header
    for line in file:
        parts = line.strip().split(",")
        entity = parts[0]
        year = parts[2]
        try:
            life_exp = float(parts[3])
        except ValueError:
            continue
        #overall
        if life_exp < overall_min:
            overall_min = life_exp
            overall_min_country = entity
            overall_min_year = year
        if life_exp > overall_max:
            overall_max = life_exp
            overall_max_country = entity
            overall_max_year = year
        #year
        if year == year_of_interest:
            year_total += life_exp
            year_count += 1
            if life_exp < year_min:
                year_min = life_exp
                year_min_country = entity
            if life_exp > year_max:
                year_max = life_exp
                year_max_country = entity
        #country
        if entity.lower() == country_of_interest:
            country_total += life_exp
            country_count += 1
            if life_exp < country_min:
                country_min = life_exp
                country_min_year = year
            if life_exp > country_max:
                country_max = life_exp
                country_max_year = year
            if year == year_of_interest:
                life_exp_that_year = life_exp
#//PRINT\\# ------------------------------------------------------------------------------------------------------
print()
print(f"Overall max life expectancy: {overall_max} from {overall_max_country} in {overall_max_year}")
print(f"Overall min life expectancy: {overall_min} from {overall_min_country} in {overall_min_year}")
#year results
if year_count > 0:
    year_avg = year_total / year_count
    print(f"\nFor the year {year_of_interest}:")
    print(f"Average life expectancy: {year_avg:.2f}")
    print(f"Max life expectancy: {year_max} in {year_max_country}")
    print(f"Min life expectancy: {year_min} in {year_min_country}")
else:
    print(f"\nNo data found for year {year_of_interest}.")
#country results
if country_of_interest:
    print(f"\nFor the country {country_of_interest.title()}:")
    if country_count > 0:
        country_avg = country_total / country_count
        print(f"Average life expectancy across all years: {country_avg:.2f}")
        print(f"Min life expectancy: {country_min} in {country_min_year}")
        print(f"Max life expectancy: {country_max} in {country_max_year}")
        if life_exp_that_year is not None:
            print(f"Life expectancy in {year_of_interest}: {life_exp_that_year}")
        else:
            print(f"No data for {country_of_interest.title()} in {year_of_interest}")
    else:
        print("No data found for that country.")