cd ../..
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_plotting python plotter.py
assert_exit_code 0

cd test/functional/
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
fname1='iris_boxplot.png'
fname2='petal_length_v_width_scatter.png'
fname3='multi_panel_figure.png'
run test_save_1 python check_file.py --fname $fname1
assert_exit_code 0
assert_in_stdout 'Found'
run test_save_2 python check_file.py --fname $fname2
assert_exit_code 0
assert_in_stdout 'Found'
run test_save_3 python check_file.py --fname $fname3
assert_exit_code 0
assert_in_stdout 'Found'

# Cleaning
rm ssshtest
cd ../..
rm $fname1
rm $fname2
rm $fname3
rm ssshtest
