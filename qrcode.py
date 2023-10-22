import segno
import sys

# Check if at least one command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: python3 qrcode.py <arg1>")
    exit
else:
    # Iterate through the command-line arguments and print them
    input_arg =  sys.argv[1]

print("Generating QR code for:", input_arg)

qrcode = segno.make_qr(input_arg)
qrcode.save(
    "qrcode.png",
    scale=10,
    quiet_zone=None,
    light=None,
    dark="grey",
    data_dark="grey",
    data_light=None,
)
