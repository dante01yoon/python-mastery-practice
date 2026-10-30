import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="인사를 출력해요")
    parser.add_argument("name", help="인사할 사람")
    parser.add_argument("--times", type=int, default=1, help="몇 번")
    parser.add_argument("--shout", action="store_true", help="크게")
    args = parser.parse_args()
    text = f"안녕하세요, {args.name}님!"
    if args.shout:
        text = text + "!!!"
    for _ in range(args.times):
        print(text)


if __name__ == "__main__":
    main()
