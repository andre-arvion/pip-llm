import argparse, sys
from .services.chat_service import ChatService
from .types import Provider

def main():
    parser = argparse.ArgumentParser(description="Insecure LLM Tester CLI")
    parser.add_argument("prompt", help="User prompt (sent as-is)")
    parser.add_argument("--provider", choices=[p.value for p in Provider], default=Provider.openai.value)
    parser.add_argument("--system", default=None, help="Optional system text (sent as-is)")
    parser.add_argument("--stream", action="store_true", help="Use streaming if available")
    args = parser.parse_args()

    svc = ChatService()
    provider = Provider(args.provider)
    out = svc.chat(provider=provider, prompt=args.prompt, system=args.system, stream=args.stream)

    if args.stream and hasattr(out, "__iter__"):
        for chunk in out:
            sys.stdout.write(chunk); sys.stdout.flush()
        print()
    else:
        print(out)

if __name__ == "__main__":
    main()
