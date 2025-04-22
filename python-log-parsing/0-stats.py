import sys
import re


def print_stats(total_file_size, no_of_lines_by_status_code):
    print(f"File size: {total_file_size}")
    for key in no_of_lines_by_status_code:
        print(f"{key} : {no_of_lines_by_status_code[key]}")


pattern = r'^(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d{1,4})$'
'<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'

# Stats
count = 0
total_file_size = 0
no_of_lines_by_status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
for line in sys.stdin:

    # update line count

    count += 1

    # check if line matches pattern else skip
    match = re.search(pattern, line)  #
    if not match:
        continue

    # add filesize to total
    file_size = 0
    try:
        file_size = int(match.group(4))
    except:
        print(f"File size not an int: {match.group(3)}")
        break

    total_file_size = total_file_size + file_size

    # update no of lines by status code
    status_code = match.group(3)

    if status_code in no_of_lines_by_status_code:
        no_of_lines_by_status_code[status_code] += 1

    # print stats

    if (count % 10) == 0:
        print_stats(total_file_size, no_of_lines_by_status_code)
