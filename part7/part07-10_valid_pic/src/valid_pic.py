from datetime import datetime


def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False

    ddmmyy = pic[:6]
    century = pic[6]
    century_marker = {"+": 18, "-": 19, "A": 20}
    picNum = pic[7:10]
    control_ch_remainder = int(ddmmyy + picNum) % 31
    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    try:
        if century not in century_marker:
            raise ValueError("invalid century!")
        datetime(
            century_marker[century] + int(ddmmyy[4:]), int(ddmmyy[2:4]), int(ddmmyy[:2])
        )
        return pic[-1] == string[control_ch_remainder]

    except ValueError:
        return False
