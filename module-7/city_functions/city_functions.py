def citystring(city_name , country_name, population=None, language=None):
    syntaxReturn = f"{city_name}, {country_name}"
    if population is not None:
        syntaxReturn += f" - Population - {population}"
    if language is not None:
        syntaxReturn += f", {language}"
    return syntaxReturn


def main():
    print(citystring("Boston" , "United States"))
    print(citystring("London" , "England" , 500000))
    print(citystring("Tokyo" , "Japan" , 600000 , "Japanese"))


main()
