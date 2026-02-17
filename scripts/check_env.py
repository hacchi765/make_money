from src.config import Config
import sys

def check_env():
    print(f"Python version: {sys.version}")
    print(f"Loading config...")
    if Config.X_USERNAME:
        print(f"X_USERNAME found: {Config.X_USERNAME}")
    else:
        print("X_USERNAME not found in .env")

if __name__ == "__main__":
    check_env()
