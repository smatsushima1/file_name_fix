

import os
import time

# Start timer for functinos
def start_function(func_name):
    start_time = time.time()
    print('\n' + ('#' * 80))
    print('Function: %s\nStarting...' % (func_name))
    return start_time

# End timer for functions
def end_function(start_time):
    end_time = time.time() - start_time
    if end_time > 60:
        res = end_time / 60
        res_spl = str(res).split('.')
        mins = res_spl[0]
        secs = round(float('.' + res_spl[1]) * 60, 3)
        print('''Function finished in %s' %s"''' % (mins, secs))
    else:
        print('Function finished in %s"' % round(time.time() - start_time, 3))

def rename_files():
    start_time = start_function("rename_files")
    # d = directories, sd = subdirectories, f = files
    for d, sd, f in os.walk("."):
        for i in f:
            # Only check for specific file extensions and if includes a (
            if i.endswith(".jpg") == True and "(" in i:
                # First find where parenethesis are
                paren_num1 = i.find("(")
                paren_num2 = i.find(")")
                # Isolate the file iteration
                file_num = i[paren_num1 + 1:paren_num2]
                # Save the old file iteration minus the file extension
                old_file_num = i[paren_num1 - 1:paren_num2 + 1] 
                # Convert the old file_num to the new iteration
                new_file_num = "_" + (4 - len(file_num))*"0" + file_num
                # Get full path of old and new names
                old_name = os.path.abspath(os.path.join(d, i))
                new_name = old_name.replace(old_file_num, new_file_num)
                # Finally, convert the old to the new
                os.rename(old_name, new_name)
    end_function(start_time)

rename_files()

