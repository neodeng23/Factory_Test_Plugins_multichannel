# -*- coding=utf-8 -*-
import os

test_program_name = "Hyperion"
run_test_cmd = """
        osascript -e '
        tell application "System Events"
	        tell process "Hyperion"
		        get value of static text of group 1 of UI element 2 of UI element 1 of scroll area 1 of window 1 of application process "Hyperion" of application "System Events"
	        end tell
        end tell
        '
      """


res = os.system(run_test_cmd)
print(type(res))
