(use '[clojure.string :only (join split)])
;Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

;(reduce +(map #(read-string %)
;              (split (slurp "/Users/stephenkinser/Projects/projectEuler/Clojure/problem13.txt") #"\n" )))

(defn problem13[filepath]
  (reduce +(map #(read-string %)
              (split (slurp filepath) #"\n" ))))
