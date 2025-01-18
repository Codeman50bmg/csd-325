# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a string in the form 'City, Country - population xxx, Language' if both population and language are provided,
    or 'City, Country - population xxx' if only population is provided, or 'City, Country - Language' if only language is provided,
    or 'City, Country' if neither are provided."""
    
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    elif language:
        return f"{city}, {country} - {language}"
    else:
        return f"{city}, {country}"

# Call the function with city, country, and optionally population
print(city_country('Santiago', 'Chile', '5000000', 'Spanish'))  # With population
print(city_country('Paris', 'France', '2148000','French'))    # With population
print(city_country('Tokyo', 'Japan', '13929286','Japanese'))    # With population

