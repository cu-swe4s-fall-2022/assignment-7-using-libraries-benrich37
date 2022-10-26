test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

fname='deleteme.csv'

run test_save python write_random.py --row 5 --col 5 --fname $fname
assert_exit_code 0

run test_save_good python check_file.py --fname $fname
assert_exit_code 0
assert_in_stdout 'Found'