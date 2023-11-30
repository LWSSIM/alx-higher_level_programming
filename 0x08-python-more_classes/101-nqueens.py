#!/usr/bin/python3
'''This Module is an attempt on Backtracking
    Nth queen problem
'''


from sys import argv


def main():
    '''Main function

        Args:
            argv: cli args vector

        Return:
            list contaning possible solutions
    '''
    col = set()
    diag_p = set()
    diag_n = set()

    board = []

    def BackTrack(n, r):
        if r == n:
            print(board)

        for c in range(n):
            if c in col or (r + c) in diag_p or (r - c) in diag_n:
                continue
            col.add(c)
            diag_p.add(r + c)
            diag_n.add(r - c)

            board.append([r, c])

            BackTrack(n, r + 1)

            col.remove(c)
            diag_p.remove(r + c)
            diag_n.remove(r - c)
            board.pop()

    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    if not argv[1].isdigit():
        print('N must be a number')
        exit(1)
    N = int(argv[1])
    if N < 4:
        print('N must be at least 4')
        exit(1)

    BackTrack(N, 0)


if __name__ == "__main__":
    main()
