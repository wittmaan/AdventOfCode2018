
## --- Day 3: No Matter How You Slice It ---

## --- Part one ---


# id @ left-margin, top-margin: width x height

input <- c(
  "#1 @ 1,3: 4x4",
  "#2 @ 3,1: 4x4",
  "#3 @ 5,5: 2x2"
)

library(stringr)
library(data.table)
library(dplyr)

input <- fread("../resources/day3input.txt", sep = "\n", header = FALSE)$V1


input_tab <- str_match(input, "(#[0-9]+)\\s@\\s([0-9]+),([0-9]+):\\s([0-9]+)x([0-9]+)")[,2:6] %>%
  as.data.table()
colnames(input_tab) <- c("id", "left", "top", "width", "height")

create_area <- function(left, top, width, heigth) {
  area <- matrix(0, ncol=left+width, nrow=top+heigth)
  area[(top+1):(top+heigth), (left+1):(left+width)] <- 1
  area
}


areas <- apply(input_tab, 1, function(x) {
  create_area(as.numeric(x[2]), as.numeric(x[3]), as.numeric(x[4]), as.numeric(x[5]))
})

names(areas) <- input_tab$id
dims <- lapply(areas, function(x) dim(x)) %>% as.data.table()
overlapping <- data.table(row=rep(1:max(dims), max(dims)), col=rep(1:max(dims), each=max(dims)), count=0)

for (area in areas) {
  ind <- which(area == 1, arr.ind = TRUE)
  overlapping[row %in% ind[,1] & col %in% ind[,2], count := count + 1]
}

nrow(overlapping[count>1])

# 110383


## Part two

count <- 1
for (area in areas) {
  ind <- which(area == 1, arr.ind = TRUE)
  is_overlapping <- any(overlapping[row %in% ind[,1] & col %in% ind[,2], count] > 1)
  if (!is_overlapping) {
    print(names(areas)[count])
  }
  
  count <- count + 1
}

# 129
