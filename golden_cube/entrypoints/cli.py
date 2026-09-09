import argparse

from golden_cube import __version__


def main() -> None:
    parser = argparse.ArgumentParser(prog="golden-cube")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command")

    serve = sub.add_parser("serve", help="Start the inference server")
    serve.add_argument("model", help="Model name or local path")

    args = parser.parse_args()

    if args.command == "serve":
        print(f"Golden Cube serving scaffold for model: {args.model}")
        print("OpenAI-compatible serving will be implemented in a later milestone.")
    else:
        parser.print_help()
