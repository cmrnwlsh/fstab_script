from subprocess import run

blkid = run(["blkid"], capture_output=True, text=True)
ids = {
    line.split()[0][:-1]: line.split()[1].replace('"', "")
    for line in blkid.stdout.splitlines()
    if line[:4] == "/dev"
}

with open("/etc/fstab", "r+") as fstab:
    text = fstab.read()
    for dev in ids:
        text = text.replace(dev, ids[dev])
    fstab.seek(0)
    fstab.write(text)
