#!/usr/bin/env python3
import os
import sys

def main():
    app_env = os.environ.get("APP_ENV")
    if not app_env:
        print("ERROR: APP_ENV is not set")
        sys.exit(1)
    print(f"Config check: OK (APP_ENV={app_env})")
    sys.exit(0)

if __name__ == "__main__":
    main()
