#!/bin/bash

# Download Movie Review Data
# http://www.cs.cornell.edu/people/pabo/movie-review-data/
# http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.README.1.0.txt

FILE='rt-polaritydata.tar.gz'
URL="http://www.cs.cornell.edu/people/pabo/movie-review-data/${FILE}"

wget ${URL}
tar zxvf ${FILE}
