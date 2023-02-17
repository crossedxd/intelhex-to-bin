# /usr/bin/env python3
from utils import MapType, MemoryMap


def UNKNOWN_PIC32():
    pic32 = MemoryMap()
    for offset in range(0, 0xFFFFFFFF, 0x100000):
        pic32.add_region(offset, offset + 0xFFFFF, "Unknown", MapType.MIXED)
    return pic32


"""
PIC32MX3XX/4XX FAMILY
http://ww1.microchip.com/downloads/en/devicedoc/61143h.pdf
"""


def PIC32MX320F032H():
    pic32 = MemoryMap()
    pic32.add_region(0x00000000, 0x00001FFF, "RAM", MapType.PHYSICAL)
    pic32.add_region(0x1D000000, 0x1D007FFF, "Program Flash", MapType.PHYSICAL)
    pic32.add_region(0x1F800000, 0x1F8FFFFF, "SFRs", MapType.PHYSICAL)
    pic32.add_region(0x1FC00000, 0x1FC02FEF, "Boot Flash", MapType.PHYSICAL)
    pic32.add_region(
        0x1FC02FF0, 0x1FC02FFF, "Device Configuration Registers", MapType.PHYSICAL
    )
    pic32.add_region(0x80000000, 0x80001FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0x9D000000, 0x9D007FFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0x9FC00000, 0x9FC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0x9FC02FEF, 0x9FC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    pic32.add_region(0xA0000000, 0xA0001FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0xBD000000, 0xBD007FFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0xBF800000, 0xBF8FFFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0xBFC00000, 0xBFC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0xBFC02FF0, 0xBFC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    return pic32


def PIC32MX420F032H():
    return PIC32MX320F032H()


def PIC32MX320F064H():
    pic32 = MemoryMap()
    pic32.add_region(0x00000000, 0x00003FFF, "RAM", MapType.PHYSICAL)
    pic32.add_region(0x1D000000, 0x1D00FFFF, "Program Flash", MapType.PHYSICAL)
    pic32.add_region(0x1F800000, 0x1F8FFFFF, "SFRs", MapType.PHYSICAL)
    pic32.add_region(0x1FC00000, 0x1FC02FEF, "Boot Flash", MapType.PHYSICAL)
    pic32.add_region(
        0x1FC02FF0, 0x1FC02FFF, "Device Configuration Registers", MapType.PHYSICAL
    )
    pic32.add_region(0x80000000, 0x80003FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0x9D000000, 0x9D00FFFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0x9FC00000, 0x9FC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0x9FC02FEF, 0x9FC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    pic32.add_region(0xA0000000, 0xA0003FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0xBD000000, 0xBD00FFFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0xBF800000, 0xBF8FFFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0xBFC00000, 0xBFC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0xBFC02FF0, 0xBFC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    return pic32


def PIC32MX320F128H():
    pic32 = MemoryMap()
    pic32.add_region(0x00000000, 0x00003FFF, "RAM", MapType.PHYSICAL)
    pic32.add_region(0x1D000000, 0x1D01FFFF, "Program Flash", MapType.PHYSICAL)
    pic32.add_region(0x1F800000, 0x1F8FFFFF, "SFRs", MapType.PHYSICAL)
    pic32.add_region(0x1FC00000, 0x1FC02FEF, "Boot Flash", MapType.PHYSICAL)
    pic32.add_region(
        0x1FC02FF0, 0x1FC02FFF, "Device Configuration Registers", MapType.PHYSICAL
    )
    pic32.add_region(0x80000000, 0x80003FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0x9D000000, 0x9D01FFFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0x9FC00000, 0x9FC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0x9FC02FEF, 0x9FC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    pic32.add_region(0xA0000000, 0xA0003FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0xBD000000, 0xBD01FFFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0xBF800000, 0xBF8FFFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0xBFC00000, 0xBFC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0xBFC02FF0, 0xBFC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    return pic32


def PIC32MX320F128L():
    return PIC32MX320F128H


def PIC32MX340F128H():
    pic32 = MemoryMap()
    pic32.add_region(0x00000000, 0x00007FFF, "RAM", MapType.PHYSICAL)
    pic32.add_region(0x1D000000, 0x1D01FFFF, "Program Flash", MapType.PHYSICAL)
    pic32.add_region(0x1F800000, 0x1F8FFFFF, "SFRs", MapType.PHYSICAL)
    pic32.add_region(0x1FC00000, 0x1FC02FEF, "Boot Flash", MapType.PHYSICAL)
    pic32.add_region(
        0x1FC02FF0, 0x1FC02FFF, "Device Configuration Registers", MapType.PHYSICAL
    )
    pic32.add_region(0x80000000, 0x80007FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0x9D000000, 0x9D01FFFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0x9FC00000, 0x9FC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0x9FC02FEF, 0x9FC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    pic32.add_region(0xA0000000, 0xA0007FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0xBD000000, 0xBD01FFFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0xBF800000, 0xBF8FFFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0xBFC00000, 0xBFC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0xBFC02FF0, 0xBFC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    return pic32


def PIC32MX340F128L():
    PIC32MX340F128H


def PIC32MX440F128H():
    PIC32MX340F128H


def PIC32MX440F128L():
    PIC32MX340F128H


def PIC32MX340F256H():
    pic32 = MemoryMap()
    pic32.add_region(0x00000000, 0x00007FFF, "RAM", MapType.PHYSICAL)
    pic32.add_region(0x1D000000, 0x1D03FFFF, "Program Flash", MapType.PHYSICAL)
    pic32.add_region(0x1F800000, 0x1F8FFFFF, "SFRs", MapType.PHYSICAL)
    pic32.add_region(0x1FC00000, 0x1FC02FEF, "Boot Flash", MapType.PHYSICAL)
    pic32.add_region(
        0x1FC02FF0, 0x1FC02FFF, "Device Configuration Registers", MapType.PHYSICAL
    )
    pic32.add_region(0x80000000, 0x80007FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0x9D000000, 0x9D03FFFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0x9FC00000, 0x9FC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0x9FC02FEF, 0x9FC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    pic32.add_region(0xA0000000, 0xA0007FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0xBD000000, 0xBD03FFFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0xBF800000, 0xBF8FFFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0xBFC00000, 0xBFC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0xBFC02FF0, 0xBFC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    return pic32


def PIC32MX360F256L():
    return PIC32MX340F256H()


def PIC32MX440F256H():
    return PIC32MX340F256H()


def PIC32MX460F256L():
    return PIC32MX340F256H()


def PIC32MX340F512H():
    pic32 = MemoryMap()
    pic32.add_region(0x00000000, 0x00007FFF, "RAM", MapType.PHYSICAL)
    pic32.add_region(0x1D000000, 0x1D07FFFF, "Program Flash", MapType.PHYSICAL)
    pic32.add_region(0x1F800000, 0x1F8FFFFF, "SFRs", MapType.PHYSICAL)
    pic32.add_region(0x1FC00000, 0x1FC02FEF, "Boot Flash", MapType.PHYSICAL)
    pic32.add_region(
        0x1FC02FEF, 0x1FC02FFF, "Device Configuration Registers", MapType.PHYSICAL
    )
    pic32.add_region(0x80000000, 0x80007FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0x9D000000, 0x9D07FFFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0x9FC00000, 0x9FC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0x9FC02FF0, 0x9FC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    pic32.add_region(0xA0000000, 0xA0007FFF, "RAM", MapType.VIRTUAL)
    pic32.add_region(0xBD000000, 0xBD07FFFF, "Program Flash", MapType.VIRTUAL)
    pic32.add_region(0xBF800000, 0xBF8FFFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0xBFC00000, 0xBFC02FEF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(
        0xBFC02FF0, 0xBFC02FFF, "Device Configuration Registers", MapType.VIRTUAL
    )
    return pic32


def PIC32MX360F512L():
    return PIC32MX340F512H()


def PIC32MX440F512H():
    return PIC32MX340F512H()


def PIC32MX460F512L():
    return PIC32MX340F512H()
