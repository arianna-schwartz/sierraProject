import sys

verification_code = sys.stdin.readline().strip().replace("-", "")

print(f"Received verification code: {verification_code}")