(use '[clojure.string :only (join split)])
; Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

(defn problem13 [filepath]
  (reduce + (map #(read-string %)
                 (split (slurp filepath) #"\n"))))

(println (problem13 "problem13.txt"))