"""Read a single sector of a physical disk. Tested on Mac OS 10.13.3 and Windows 8."""

import os


def main():  # Read the first sector of the first disk as example.
    """Demo usage of function."""
    if os.name == "nt":
        # Windows based OS normally uses '\\.\physicaldriveX' for disk drive identification.
        print(read_sector(r"\\.\physicaldrive0"))
    else:
        # Linux based OS normally uses '/dev/diskX' for disk drive identification.
        print(read_sector("/dev/disk0"))


def read_sector(disk, sector_no=0):
    """Read a single sector of the specified disk.

    Keyword arguments:
    disk -- the physical ID of the disk to read.
    sector_no -- the sector number to read (default: 0).
    """
    # Static typed variable
    read = None
    # File operations with `with` syntax. To reduce file handeling efforts.
    with open(disk, 'rb') as fp:
        fp.seek(sector_no * 512)
        read = fp.read(512)
    return read


if __name__ == "__main__":
    main()
