import argparse
from router.model_router import ModelRouter

def main():
    parser = argparse.ArgumentParser(description="Avalon Round Table Prompt Dispatcher")
    parser.add_argument("--knight", required=True, help="Name of the Knight (e.g., 'Sir Nexus')")
    parser.add_argument("--prompt", required=True, help="Prompt to dispatch")
    args = parser.parse_args()

    router = ModelRouter()
    response = router.invoke(args.knight, args.prompt)
    print(f"\n🛡️ Response from {args.knight}:\n{response}\n")

if __name__ == "__main__":
    main()
