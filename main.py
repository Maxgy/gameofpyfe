#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random


class Cell:
    def __init__(self, alive):
        self.alive = alive
        self.will_live = True

    def print(self):
        if self.alive:
            return "█"
        else:
            return " "


grid = []

w, h = os.get_terminal_size()

for y in range(h - 1):
    row = []
    for x in range(w - 1):
        row.append(Cell(bool(round(random.random()))))
    grid.append(row)


def print_grid():
    render = ""
    for row in grid:
        for cell in row:
            render += cell.print()
        render += "\n"
    print(render)


def change_cells():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            adjacent_count = 0

            if y > 1 and x > 0 and grid[y - 1][x - 1].alive:
                adjacent_count += 1
            if y > 1 and grid[y - 1][x].alive:
                adjacent_count += 1
            if y > 1 and x < w - 2 and grid[y - 1][x + 1].alive:
                adjacent_count += 1
            if x > 0 and grid[y][x - 1].alive:
                adjacent_count += 1
            if x < w - 2 and grid[y][x + 1].alive:
                adjacent_count += 1
            if y < h - 2 and x > 0 and grid[y + 1][x - 1].alive:
                adjacent_count += 1
            if y < h - 2 and grid[y + 1][x].alive:
                adjacent_count += 1
            if y < h - 2 and x < w - 2 and grid[y + 1][x + 1].alive:
                adjacent_count += 1

            if adjacent_count < 2 or adjacent_count > 3:
                grid[y][x].will_live = False
            elif grid[y][
                    x].alive and adjacent_count == 2 or adjacent_count == 3:
                grid[y][x].will_live = True


def update_cells():
    for row in grid:
        for cell in row:
            cell.alive = cell.will_live


while True:
    print_grid()
    change_cells()
    update_cells()
