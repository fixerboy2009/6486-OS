# Main boot thing, runs the boot.py file
BOOT_FILE = "./sys6486/boot/boot.py"

ARGS = {
    "_VAR_VER": 1,
}

with open(BOOT_FILE, 'r') as F:
    st = ""
    lines = F.readlines()
    for line in lines:
        st = st + line

    exec(st, ARGS)