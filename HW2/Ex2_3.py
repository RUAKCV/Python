months = {
    "01": "winter",
    "02": "winter",
    "03": "spring",
    "04": "spring",
    "05": "spring",
    "06": "summer",
    "07": "summer",
    "08": "summer",
    "09": "fall",
    "10": "fall",
    "11": "fall",
    "12": "winter"
}
key = input("Input month number in 2 digits = ")

if key in months:
    month = months[key]
    print(month)
