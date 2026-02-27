import re
with open(r'C:\Users\Адильхан\Desktop\pp2\work\Practice5\raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()
print("ЧЕК:")
print("--" * 40)

print("\nТОВАРЫ:")
tovars = re.findall(r'\d+\.\s+(.+?)\s+\d', text)
for i, item in enumerate(tovars, 1):
    print(f"{i}. {item}")

print("\nЦЕНЫ:")
ceny = re.findall(r'\d+(?:\s\d+)?,\d{2}', text)
print(ceny)

# 3. ИТОГО
itog = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', text)
if itog:
    print(f"\nИТОГО: {itog.group(1)} руб.")

# 4. Дата
date = re.search(r'(\d{2}\.\d{2}\.\d{4})', text)
if date:
    print(f"\nДАТА: {date.group(1)}")

# 5. Оплата
if 'Банковская карта' in text:
    print("ОПЛАТА: Карта")
elif 'Наличные' in text:
    print("ОПЛАТА: Наличные")