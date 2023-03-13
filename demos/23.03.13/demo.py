#!/usr/bin/env python3

NUM_DISKS = 4
MAX_HEIGHT = NUM_DISKS + 1

rod1 = ["|", "|", "|", "|", "#"]
rod2 = ["|", "|", "|", "|", "###"]
rod3 = ["|", "|", "|", "#####", "#######"]
# rod1 = ["|", "|", "|", "|", "#############"]
# rod2 = ["|", "|", "|", "|", "#############"]
# rod3 = ["|", "|", "|", "#####", "#############"]

template = "{:^15}{:^15}{:^15}"

print()
for idx in range(MAX_HEIGHT):
    print(template.format(rod1[idx], rod2[idx], rod3[idx]))
