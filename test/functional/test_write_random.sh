test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

csvfname='deleteme.csv'

run test_save python write_random.py --row 5 --col 5 --fname $csvfname
assert_exit_code 0

run test_save_good python check_file.py --fname $csvfname
assert_exit_code 0
assert_in_stdout 'Found'

# Cleaning
rm $fname
rm ssshtest