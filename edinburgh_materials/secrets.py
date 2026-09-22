"""
A script to demonstrate reading secrets from environment variables.

To see existing variables in the console, run the following:

+ `env`  # Bash
+ `dir env:`  # Powershell

"""
import os
import sys

try:
    MY_SECRET = os.environ["MY_SECRET"]
except KeyError:
    # KeyError is thrown if environment variable isn't set
    print("MY_SECRET environment variable is not set. "
          "Set with `$env:MY_SECRET=password123` or "
          "`export MY_SECRET=password123`")

    # Exit the script with a non-zero error code, which tells the operating
    # system that the task failed.
    sys.exit(1)

print(f"My password is {MY_SECRET}")
