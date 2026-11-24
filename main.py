#!/usr/bin/env python3
"""The Diligence Defense — make.fun entry (u-jolly-fox-32-two-days-of-excuses-3f18797e)"""
import os

ENTRY_LINE = "I re-read the deadline twice to make sure I understood it. In my model, that is called diligence and not my entire personality."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")
