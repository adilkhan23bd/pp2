import json


file_path = r'C:\Users\Адильхан\Desktop\pp2\work\Practice4\sample-data.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Speed':<8} {'MTU':<6}")
print("-" * 80)

for item in data['imdata'][:3]:
    a = item['l1PhysIf']['attributes']
    print(f"{a['dn']:<50} {a['speed']:<8} {a['mtu']:<6}")