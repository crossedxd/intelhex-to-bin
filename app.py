#!/usr/bin/env python3

# INHX8M HEX-record format
# https://www.lucidtechnologies.info/inhx8m.htm

# INHX32 extended linear address example
# https://www.lucidtechnologies.info/inhx32.htm

# PIC32 documentation (for memory map)
# http://ww1.microchip.com/downloads/en/devicedoc/61143h.pdf


CURRENT_ADDRESS = 0
PROGRAM_BYTES = []


def calc_checksum(n):
    return ((n ^ 0xFF) + 1) & 0xFF


def parse_record(s):
    global CURRENT_ADDRESS
    global PROGRAM_BYTES

    # Extract values from line
    start_code = s[0]
    byte_count = int(s[1:3], 16)
    address = int(s[3:7], 16)
    record_type = int(s[7:9], 16)
    record_data = s[9 : 9 + (2 * byte_count)]
    record_data_size = len(record_data) >> 1
    checksum = int(s[-3:-1], 16)

    # Calculate checksum
    calculated_checksum = calc_checksum(
        sum([int(s[i : i + 2], 16) for i in range(1, len(s) - 4, 2)])
    )

    # Quick checks
    assert start_code == ":", "Line failed to begin with ':'"
    assert (
        checksum == calculated_checksum
    ), "Checksums didn't match: expected {}, got {}".format(
        hex(checksum), hex(calculated_checksum)
    )

    # Record type 00 is basic memory writing
    if record_type == 0:
        # Set the low bits to whatever's in the address field
        CURRENT_ADDRESS = (CURRENT_ADDRESS & 0xFFFF0000) | address
        # Extend the memory buffer if necessary (+ the number of bytes we're adding)
        if len(PROGRAM_BYTES) < CURRENT_ADDRESS + record_data_size:
            PROGRAM_BYTES += [0] * (
                CURRENT_ADDRESS - len(PROGRAM_BYTES) + record_data_size
            )
        for i in range(record_data_size):
            written_byte = int(record_data[i * 2 : (i * 2) + 2], 16)
            # print(f"writing byte at {CURRENT_ADDRESS + i:08x}: {written_byte:02x}")
            PROGRAM_BYTES[CURRENT_ADDRESS + i] = written_byte

    # Termination record (final record in the file, and there should only be one)
    if record_type == 1:
        assert byte_count == 0, "Byte count for a termination record should be 0"
        assert record_data == "", "Termination record should have no data field"

    # Record type 04 sets the extended linear address record
    if record_type == 4:
        assert address == 0, "Address field should be 0000 for type 04 records"
        # Clear the high bits and set them to whatever's in record data
        CURRENT_ADDRESS = (CURRENT_ADDRESS & 0xFF) | (int(record_data, 16) << 16)


# TODO add args parser
# fn = r"H:\workspace\tns\PIC32_SPI_Plib_Level0_4.X.production.hex"
# fn = r"H:\workspace\tns\PIC32_SPI_Plib_Level5.X.production.hex"
fn = r"H:\workspace\tns\blinky.hex"

with open(fn) as f:
    for row in f:
        parse_record(row)


PROGRAM_BYTES = bytes(PROGRAM_BYTES)
print(f"final program size: {len(PROGRAM_BYTES):08x}")


# TODO add output files (using hex names)
PROGRAM_FLASH = PROGRAM_BYTES[0x1D000000:0x1D008000]
with open(fn + ".pf.bin", "wb") as f:
    f.write(PROGRAM_FLASH)

BOOT_FLASH = PROGRAM_BYTES[0x1FC00000:0x1FC02FF0]
with open(fn + ".bf.bin", "wb") as f:
    f.write(BOOT_FLASH)
