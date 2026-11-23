T = int(input())

for tc in range(1, T + 1):
    N, hex_num = input().split()

    result = ''

    for ch in hex_num:
        result += format(int(ch, 16), '04b')

    print(f'#{tc} {result}')
