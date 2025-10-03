esc_cine = 0
esc_bol = 0
for i in range(7):
    esc = input().upper()
    if esc == "CINEMA":
        esc_cine += 1
    elif esc == "BOLICHE":
        esc_bol += 1
        
if esc_cine > esc_bol:
    print("CINEMA")
else:
    print("BOLICHE")
