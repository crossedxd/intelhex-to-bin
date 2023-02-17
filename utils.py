#!/usr/bin/env python3
from enum import Enum


def calc_checksum(n):
    return ((n ^ 0xFF) + 1) & 0xFF


class MapType(Enum):
    EMPTY = 1
    VIRTUAL = 2
    PHYSICAL = 3
    MIXED = 4


class MemoryMap:
    """
    The MemoryMap class is intended to be used to store memory as it's being
    ingested from .hex files.  I want this to remain controller-agnostic and
    allow for other elements further down the processing chain to be able to
    parse the data.  Therefore, the initial ingest will just load the memory
    into the dictionary, and an internal function will determine the map type
    and segments based on a given ControllerConfig (or something, idk).
    """

    def __init__(self):
        self.memory_map = dict()
        self.regions = list()

    def add_byte(self, byte, address):
        self.memory_map[address] = byte

    def remove_byte(self, address):
        if self.memory_map[address]:
            self.memory_map.pop(address)

    def get_map_type(self):
        """
        Map type is gonna be guesswork for now; I skimmed datasheets for the
        MM0064 and MX3xx/MX4xx families and all of the virtual memory is found
        at 0x80000000 and greater.
        """
        is_virtual = False
        is_physical = False

        for address in self.memory_map.keys():
            if address >= 0x80000000:
                is_virtual = True
            else:
                is_physical = True

        if is_virtual and is_physical:
            return MapType.MIXED
        elif is_virtual:
            return MapType.VIRTUAL
        elif is_physical:
            return MapType.PHYSICAL
        else:
            return MapType.EMPTY

    def add_region(self, start, end, name, map_type: MapType):
        self.regions.append(
            {"start": start, "end": end, "name": name, "map_type": map_type}
        )

    def generate_memory_regions(self):
        """
        This approach is slower/less efficient,
        but is easier to mock up in short order.
        """
        for region in self.regions:
            data = [0] * (region["end"] - region["start"] + 1)
            has_bytes = False
            for address in self.memory_map:
                if address >= region["start"] and address <= region["end"]:
                    data[address - region["start"]] = self.memory_map[address]
                    has_bytes = True
            if has_bytes:
                print(
                    f"[+] Found data in region 0x{region['start']:08x} - 0x{region['end']:08x} ({region['name']})"
                )
                with open(f"0x{region['start']:08x}.bin", "wb") as f:
                    f.write(bytes(data))


def parse_record(s, current_address, memory_map: MemoryMap):
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
    assert start_code == ":", "[!] Line failed to begin with ':'"
    assert (
        checksum == calculated_checksum
    ), "[!] Checksums didn't match: expected {}, got {}".format(
        hex(checksum), hex(calculated_checksum)
    )

    # Record type 00 is basic memory writing
    if record_type == 0:
        # Set the low bits to whatever's in the address field
        current_address = (current_address & 0xFFFF0000) | address
        # Write each of the bytes to their respective locations in the memory dictionary
        for i in range(record_data_size):
            written_byte = int(record_data[i * 2 : (i * 2) + 2], 16)
            memory_map.add_byte(written_byte, current_address + i)

    # Termination record (final record in the file, and there should only be one)
    if record_type == 1:
        assert byte_count == 0, "[!] Byte count for a termination record should be 0"
        assert record_data == "", "[!] Termination record should have no data field"

    # Record type 04 sets the extended linear address record
    if record_type == 4:
        assert address == 0, "Address field should be 0000 for type 04 records"
        # Clear the high bits and set them to whatever's in record data
        current_address = (current_address & 0xFF) | (int(record_data, 16) << 16)

    return current_address
