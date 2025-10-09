main_string <- "R programming language"
search_char <- "g"
# Find positions using gregexpr()
positions <- gregexpr(search_char, main_string)[[1]]
if (positions[1] != -1) {
  cat(sprintf("Character '%s' found at positions: %s\n",
              search_char,
              paste(positions, collapse = ", ")))
} else {
  cat(sprintf("Character '%s' not found.\n", search_char))
}