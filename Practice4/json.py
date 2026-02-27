import json

data = {
    "imdata": [
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/34]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/35]",
                    "descr": "",
                    "speed": "inherit",
                    "mtu": "9150"
                }
            }
        }
    ]
}


print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)

for item in data['imdata']:
    attr = item['l1PhysIf']['attributes']
    print(f"{attr['dn']:<50} {attr['descr']:<20} {attr['speed']:<8} {attr['mtu']:<6}")