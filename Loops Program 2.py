for hour in range(24):
    if hour == 0:
        print(f"{hour}:00 - Midnight")
    elif hour == 12:
        print(f"{hour}:00 - Noon")
    elif hour < 12:
        print(f"{hour}:00 AM")
    else:
        print(f"{hour - 12}:00 PM")
