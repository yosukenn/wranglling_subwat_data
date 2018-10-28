import csv

def fix_turnstile_data(input_file):
    f_in = open('../datas/' + input_file, 'r')
    f_out = open('../datas/updated_' + input_file, 'w')

    reader_in = csv.reader(f_in, delimiter=',')
    writer_out = csv.writer(f_out, delimiter=',')

    for line in reader_in:
        turnstile_code = line[:3]
        i = 1
        n = 3
        while i < 9:
            if line[n:n+5]:
                slice_line = turnstile_code + line[n:n+5]
                writer_out.writerow(slice_line)
            i += 1
            n += 5

    f_in.close()
    f_out.close()

fix_turnstile_data('turnstile_110507.txt')
