from rich.console import Console
from rich.table import Table

from cipher import caesar

console = Console()
message = input("암호로 바꿀 영어 문장: ")
shift = int(input("몇 칸 밀까요: "))

secret = caesar.encrypt(message, shift)
table = Table(title="카이사르 암호")
table.add_column("원래 문장")
table.add_column("암호문")
table.add_column("다시 푼 문장")
table.add_row(message, secret, caesar.decrypt(secret, shift))
console.print(table)
