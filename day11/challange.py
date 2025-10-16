from datetime import datetime, timedelta

now = datetime.now()
print(f"Current date/time: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}, Hours: {now.hour}, Minutes: {now.minute}, Seconds: {now.second},Microseconds{now.microsecond}")

future = now + timedelta(days=100)
past = now - timedelta(days=100)
print(f"\n100 days in future: {future}")
print(f"\n100 days in past: {past}")

specific = datetime(2025,10,9,19,1,23,59)
with open("formatted_dates.txt", "w") as file:
    file.write("Specific Date and Time:\n")
    file.write(specific_datetime.strftime("%Y-%m-%d %H:%M:%S"))

print("\nSpecific date and time written to 'formatted_dates.txt'")
