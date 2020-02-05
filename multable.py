#!/usr/bin/python3

"""
    Script to teach children multiplication

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import random

answers = 0
target = 30

while answers < target:
    print(f'{answers} correct answers in sequence, {target - answers} to go')
    a, b = random.randrange(2, 13), random.randrange(2, 13)
    print(f'{a} * {b} = ?')
    c = input()
    try:
        c = int(c)
    except Exception as e:
        print('Cannot read answer! Resetting sequence')
        answers = 0
        continue
    if a * b != c:
        print('Incorrect answer! Resetting sequence')
        answers = 0
        continue
    print(random.choice(['Correct!', 'Good!', 'Well done!']))
    answers += 1

print('Congratulations! Test passed!')



