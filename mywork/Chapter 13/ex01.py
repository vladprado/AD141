verse = """{ngarrafas} bottle{plural} of water on the wall!
{ngarrafas} bottle{plural} of water!
Take on down
And pass it around"""
plural = "s"
last = "{} bottles of water on the wall!\n"

for ngarrafas in range(99, 0, -1):
    if ngarrafas == 1:
        plural = ""
    elif ngarrafas == 0:
        break
    print(verse.format(ngarrafas = ngarrafas, plural = plural ))
print("No more bottles of water on the wall!\n")