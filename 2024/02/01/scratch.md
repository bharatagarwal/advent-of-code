- reports, one report per line
  - line, each report is a list of levels

```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

-------
- reports, one report per line
  - line, each report is a list of levels

How many reports are safe?

Safe
  - all increasing
  - all decreasing
    - max-change == 3
    - min-change == 1

parse reports into levels
split into pairs
check if delta is mentained
check if direction is maintained
