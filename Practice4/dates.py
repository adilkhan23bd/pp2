from datetime import datetime, timedelta


now = datetime.now()


print("1.", now - timedelta(days=5))


print("2.")
print("Вчера:", now - timedelta(days=1))
print("Сегодня:", now)
print("Завтра:", now + timedelta(days=1))


print("3.", now.replace(microsecond=0))


date1 = datetime(2024, 2, 27, 10, 0, 0)
date2 = datetime(2024, 2, 28, 12, 30, 0)
diff = (date2 - date1).total_seconds()
print("4.", diff, "секунд")