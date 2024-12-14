def is_valid_letter(char):
    return char == "M" or char == "S"

def check_top_row(row):
    return is_valid_letter(row[0]) and is_valid_letter(row[2])

def check_mid_row(row):
    return row[1] == "A"

def check_bottom_row(bottom_row, top_row):
    if top_row[0] == bottom_row[0] and top_row[2] == bottom_row[2] and not top_row[0] == top_row[2]:
        return True
    elif top_row[0] == top_row[2] and bottom_row[0] == bottom_row[2] and not top_row[0] == bottom_row[0] and is_valid_letter(bottom_row[0]):
        return True
    else:
        return False


with open('input.txt') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
col_count = len(lines)
found = 0
for y in range(col_count-2):
    xM = lines[y].find("M")
    xS = lines[y].find("S")
    x = min(xS, xM)
    top_row = lines[y][x:]
    while len(top_row) >= 3:
        #print(f"toprow: {top_row}, len {len(top_row)}")
        if check_top_row(top_row):
            mid_row = lines[y+1][x:]
            #print(f"midrow: {mid_row}")
            if check_mid_row(mid_row):
                bottom_row = lines[y+2][x:]
                #print(f"bottomrow: {bottom_row}")
                if check_bottom_row(bottom_row, top_row):
                    #print(f"{top_row}\n{mid_row}\n{bottom_row}")
                    #print("----------")
                    found+=1
        x += 1
        top_row = lines[y][x:]
print(found)



        

    