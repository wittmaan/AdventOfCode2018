
## --- Day 2: Inventory Management System ---

## --- Part one ---

library(data.table)
library(dplyr)

input <- fread("../resources/day2input.txt", header = FALSE, sep = "\n")$V1
#input <- c("abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab")

counts <- lapply(strsplit(input, ""), function(x) {
  tab <- table(x)
  two_times <- tab[tab==2]
  three_times <- tab[tab==3]
  data.table(two_times = as.numeric(length(two_times) > 0), three_times = as.numeric(length(three_times) > 0))
}) %>% rbindlist()

counts[, lapply(.SD, sum)][, two_times * three_times]

# 7533

## --- Part two ---

input <- c("abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz")
input <- strsplit(sort(input), "")

for (i in 2:length(input)) {
  ident <- input[[i-1]] == input[[i]]
  equal_char <- sum(ident)
  if (length(input[[i]]) - 1 == equal_char) {
    print(paste0(input[[i]][ident], collapse = ""))
  }
}

# "mphcuasvrnjzzkbgdtqeoylva"

