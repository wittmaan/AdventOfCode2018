
## --- Day 1: Chronal Calibration ---

## --- Part one ---

library(data.table)

input <- fread("../resources/day1input.txt", header = FALSE, sep = "\n")$V1
tail(cumsum(input), 1)

## 553


## --- Part two ---

input_repeated <- rep(input, 1000)
tmp <- cumsum(input_repeated)
head(tmp[duplicated(tmp)], 1)

## 78724
