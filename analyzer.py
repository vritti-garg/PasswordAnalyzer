import argparse
from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)

    # Original score is 0–4, scale to 0–10
    score_10 = int((result['score'] / 4) * 10)

    print("\n[+] Password Analysis:")
    print(f"Password: {password}")
    print(f"Score (0-10): {score_10}")  
    print(f"Guesses: {result['guesses']}")
    print(f"Crack Time (offline fast hash): {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    print(f"Feedback: {result['feedback']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password Strength Analyzer")
    parser.add_argument("password", help="Password to analyze")
    args = parser.parse_args()

    analyze_password(args.password)