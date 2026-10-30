import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="두 수 계산")
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    parser.add_argument("--op", choices=["add", "mul"], default="add")
    args = parser.parse_args()
    print(args.a + args.b if args.op == "add" else args.a * args.b)


if __name__ == "__main__":
    main()
