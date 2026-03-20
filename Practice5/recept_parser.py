import re


prices = re.findall(r'Стоимость\n(\d[\d ]*,\d{2})', text)

products = re.findall(r'\d+\.\n([^\n]+)', text)

total = re.search(r'ИТОГО:\n([\d\s,]+)', text)
total_amount = total.group(1) if total else "Not found"

datetime = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s*\d{2}:\d{2}:\d{2})', text)
datetime_value = datetime.group(1) if datetime else "Not found"

payment = re.search(r'(Банковская карта|Наличные)', text)
payment_method = payment.group(1) if payment else "Not found"

print("Products:")
for p in products:
    print("-", p)

print("\nPrices:")
for pr in prices:
    print(pr)

print("\nTotal:", total_amount)
print("Date and Time:", datetime_value)
print("Payment method:", payment_method)