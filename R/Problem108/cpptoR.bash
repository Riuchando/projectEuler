#!/bin/bash

if [ "$#" != "1" ]; then
    echo
    echo "Usage: $0 [.cpp]"
    echo
    exit 1
fi

CPP="$1"
export PKG_CXXFLAGS=`Rscript -e "Rcpp:::CxxFlags()"`
export PKG_LIBS=`Rscript -e "Rcpp:::LdFlags()"`

R CMD SHLIB ${CPP}
