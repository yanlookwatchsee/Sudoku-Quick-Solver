#!/usr/bin/python
# Author: Yan Li
# Licence: BSD-like licence
from copy import deepcopy
import sys
import time
import argparse


class Record:
    def __init__(self):
        self.check = [False] * 9
        self.value = -1
        self.feasible = 9

    def elect(self):
        if self.value == -1 and self.feasible == 1:
            for i, c in enumerate(self.check):
                if not c:
                    return i + 1
        return None

    def set(self, v):
        if self.value != -1 and self.value != v:
            raise ValueError

        if self.check[v - 1]:
            raise ValueError
        self.value = v
        self.feasible = 1

    def eliminate(self, v):
        if self.value != -1:
            return

        if not self.check[v - 1]:
            self.check[v - 1] = True
            self.feasible -= 1
        if self.feasible == 0:
            raise ValueError


class SolveBuffer:
    def __init__(self):
        self.buf = []
        for i in xrange(9):
            self.buf.append([])
            for j in xrange(9):
                self.buf[i].append(Record())

    def solved(self):
        for i in xrange(9):
            for j in xrange(9):
                if self.buf[i][j].value == -1:
                    return False
        return True

    def populate(self, i, j, v):
        self.buf[i][j].set(v)
        # row
        for tj in xrange(9):
            self.buf[i][tj].eliminate(v)

        # column
        for ti in xrange(9):
            self.buf[ti][j].eliminate(v)

        # block
        for ti in xrange(i / 3 * 3, i / 3 * 3 + 3):
            for tj in xrange(j / 3 * 3, j / 3 * 3 + 3):
                self.buf[ti][tj].eliminate(v)

    def find_one(self):
        for i in xrange(9):
            for j in xrange(9):
                v = self.buf[i][j].elect()
                if not v:
                    continue
                return i, j, v
        return -1, -1, -1

    def find_first_feasible(self):
        l = []
        for i in xrange(9):
            for j in xrange(9):
                if self.buf[i][j].value == -1 and self.buf[i][j].feasible > 0:
                    for k in xrange(9):
                        if not self.buf[i][j].check[k]:
                            l.append(k + 1)
                    return i, j, l
        return -1, -1, []


def do_solve(sb):
    try:
        while True:
            i, j, v = sb.find_one()
            if i == -1:
                break
            sb.populate(i, j, v)
    except ValueError:
        return False

    if sb.solved():
        return True

    ti, tj, l = sb.find_first_feasible()
    if ti == -1:
        return False

    tsb = SolveBuffer()
    solved = False
    for tv in l:
        tsb.buf = deepcopy(sb.buf)
        tsb.populate(ti, tj, tv)
        if do_solve(tsb):
            solved = True
            break

    if solved:
        sb.buf = deepcopy(tsb.buf)
        return True

    return False


class Sudoku:
    def __init__(self, b):
        self.board = b
        self.sb = SolveBuffer()

    def dump(self):
        for i in xrange(9):
            for j in xrange(9):
                v = self.sb.buf[i][j].value
                if v == -1:
                    print '-',
                else:
                    print v,
            print ''

    def solve(self):
        self.sb = SolveBuffer()

        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] > 0:
                    self.sb.populate(i, j, board[i][j])

        return do_solve(self.sb)


def load_args(data):
    a = [None] * 9
    for i, d in enumerate(data):
        a[i] = [int(c) for c in d]
    return a


parser = argparse.ArgumentParser(description='A python program to solve Sudoku problem')
parser.add_argument('rows', nargs=9, metavar='row', help='9 rows of Sudoku to be solved')
args = parser.parse_args()

board = load_args(args.rows)

s = Sudoku(board)

print "********* SOLVE BEGIN *********\n\n\n"
print "\n\n\nThe solution is ...\n"
begin = time.time()
if not s.solve():
    print "The problem can not be solved"
    sys.exit(0)

timeCost = (time.time() - begin) * 1000
s.dump()
print "********* SOLVE DONE*********"
print "Total Cost: ", timeCost, "Mili Seconds"
