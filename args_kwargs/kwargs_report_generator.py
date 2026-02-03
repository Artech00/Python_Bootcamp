def generate_report(**kwargs):
    print("Report info")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

    print(kwargs.items())


generate_report(sales=1500, expenses=500, profit=1000, region="Europe")
