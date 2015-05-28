modts <- function(X)
{ X [ ifelse(((X %% 3) == 0), T, F )]
}

modfs <- function(X)
{ X [ ifelse(((X %% 5) == 0), T, F )]
}

thing= seq(8000001, 8100001, by=2)
other= modts(thing)
other