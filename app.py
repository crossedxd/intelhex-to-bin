#!/usr/bin/env python3
from controllers import PIC32MX340F512H
from utils import parse_record

# INHX8M HEX-record format
# https://www.lucidtechnologies.info/inhx8m.htm

# INHX32 extended linear address example
# https://www.lucidtechnologies.info/inhx32.htm

# PIC32 documentation (for memory map)
# http://ww1.microchip.com/downloads/en/devicedoc/61143h.pdf


# TODO add args parser
fn = r"H:\workspace\tns\PIC32_SPI_Plib_Level0_4.X.production.hex"
# fn = r"H:\workspace\tns\PIC32_SPI_Plib_Level5.X.production.hex"
# fn = r"H:\workspace\tns\blinky.hex"

pic32 = PIC32MX340F512H()

current_address = 0
with open(fn) as f:
    for row in f:
        current_address = parse_record(row, current_address, pic32)

pic32.generate_memory_regions()

print(f"[+] Inferred memory type: {pic32.get_map_type().name}")
print(f"[+] Minimum address: 0x{min(pic32.memory_map.keys()):08x}")
print(f"[+] Maximum address: 0x{max(pic32.memory_map.keys()):08x}")
print(f"[+] Total bytes collected: {len(pic32.memory_map.values())}")
