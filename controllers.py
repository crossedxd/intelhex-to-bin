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


"""
PIC32MMXXXXGPLXXX FAMILY
https://ww1.microchip.com/downloads/en/DeviceDoc/PIC32MM0064GPL036-Family-Data-Sheet-DS60001324C.pdf
"""


def PIC32MM0016GPL020():
    pic32 = MemoryMap()
    pic32.add_region(0x00000000, 0x00000FFF, "4 Kbytes RAM", MapType.PHYSICAL)
    pic32.add_region(0x1D000000, 0x1D003FFF, "16 Kbytes Flash", MapType.PHYSICAL)
    pic32.add_region(0x1F800000, 0x1F80FFFF, "SFRs", MapType.PHYSICAL)
    pic32.add_region(0x1FC00000, 0x1FC016FF, "Boot Flash", MapType.PHYSICAL)
    pic32.add_region(0x1FC01700, 0x1FC017FF, "Configuration Bits", MapType.PHYSICAL)
    pic32.add_region(0x80000000, 0x80000FFF, "4 Kbytes RAM", MapType.VIRTUAL)
    pic32.add_region(0x9D000000, 0x9D003FFF, "16 Kbytes Flash", MapType.VIRTUAL)
    pic32.add_region(0x9F800000, 0x9F80FFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0x9FC00000, 0x9FC016FF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(0x9FC01700, 0x9FC017FF, "Configuration Bits", MapType.VIRTUAL)
    pic32.add_region(0xA0000000, 0xA0000FFF, "4 Kbytes RAM", MapType.VIRTUAL)
    pic32.add_region(0xBD000000, 0xBD003FFF, "16 Kbytes Flash", MapType.VIRTUAL)
    pic32.add_region(0xBF800000, 0xBF80FFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0xBFC00000, 0xBFC016FF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(0xBFC01700, 0xBFC017FF, "Configuration Bits", MapType.VIRTUAL)
    return pic32


def PIC32MM0016GPL028():
    return PIC32MM0016GPL020()


def PIC32MM0016GPL036():
    return PIC32MM0016GPL020()


def PIC32MM0032GPL020():
    pic32 = MemoryMap()
    pic32.add_region(0x00000000, 0x00001FFF, "8 Kbytes RAM", MapType.PHYSICAL)
    pic32.add_region(0x1D000000, 0x1D007FFF, "32 Kbytes Flash", MapType.PHYSICAL)
    pic32.add_region(0x1F800000, 0x1F80FFFF, "SFRs", MapType.PHYSICAL)
    pic32.add_region(0x1FC00000, 0x1FC016FF, "Boot Flash", MapType.PHYSICAL)
    pic32.add_region(0x1FC01700, 0x1FC017FF, "Configuration Bits", MapType.PHYSICAL)
    pic32.add_region(0x80000000, 0x80001FFF, "8 Kbytes RAM", MapType.VIRTUAL)
    pic32.add_region(0x9D000000, 0x9D007FFF, "32 Kbytes Flash", MapType.VIRTUAL)
    pic32.add_region(0x9F800000, 0x9F80FFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0x9FC00000, 0x9FC016FF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(0x9FC01700, 0x9FC017FF, "Configuration Bits", MapType.VIRTUAL)
    pic32.add_region(0xA0000000, 0xA0001FFF, "8 Kbytes RAM", MapType.VIRTUAL)
    pic32.add_region(0xBD000000, 0xBD007FFF, "32 Kbytes Flash", MapType.VIRTUAL)
    pic32.add_region(0xBF800000, 0xBF80FFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0xBFC00000, 0xBFC016FF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(0xBFC01700, 0xBFC017FF, "Configuration Bits", MapType.VIRTUAL)
    return pic32


def PIC32MM0032GPL028():
    return PIC32MM0032GPL020()


def PIC32MM0032GPL036():
    return PIC32MM0032GPL020()


def PIC32MM0064GPL020():
    pic32 = MemoryMap()
    pic32.add_region(0x00000000, 0x00001FFF, "8 Kbytes RAM", MapType.PHYSICAL)
    pic32.add_region(0x1D000000, 0x1D00FFFF, "64 Kbytes Flash", MapType.PHYSICAL)
    pic32.add_region(0x1F800000, 0x1F80FFFF, "SFRs", MapType.PHYSICAL)
    pic32.add_region(0x1FC00000, 0x1FC016FF, "Boot Flash", MapType.PHYSICAL)
    pic32.add_region(0x1FC01700, 0x1FC017FF, "Configuration Bits", MapType.PHYSICAL)
    pic32.add_region(0x80000000, 0x80001FFF, "8 Kbytes RAM", MapType.VIRTUAL)
    pic32.add_region(0x9D000000, 0x9D00FFFF, "64 Kbytes Flash", MapType.VIRTUAL)
    pic32.add_region(0x9F800000, 0x9F80FFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0x9FC00000, 0x9FC016FF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(0x9FC01700, 0x9FC017FF, "Configuration Bits", MapType.VIRTUAL)
    pic32.add_region(0xA0000000, 0xA0001FFF, "8 Kbytes RAM", MapType.VIRTUAL)
    pic32.add_region(0xBD000000, 0xBD00FFFF, "64 Kbytes Flash", MapType.VIRTUAL)
    pic32.add_region(0xBF800000, 0xBF80FFFF, "SFRs", MapType.VIRTUAL)
    pic32.add_region(0xBFC00000, 0xBFC016FF, "Boot Flash", MapType.VIRTUAL)
    pic32.add_region(0xBFC01700, 0xBFC017FF, "Configuration Bits", MapType.VIRTUAL)
    return pic32


def PIC32MM0064GPL028():
    return PIC32MM0064GPL020()


def PIC32MM0064GPL036():
    return PIC32MM0064GPL020()
