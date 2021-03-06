;The prime factors of 13195 are 5, 7, 13 and 29.
;What is the largest prime factor of the number 600851475143 ?

(defn factor [number]
  (loop [n number
         factors '()
         start 2]
    (cond (< n start) factors
          (= 0 (mod n start)) (recur (/ n start) (conj factors start) (inc start))
          :else
          (recur n factors (inc start)))))
(println (factor 600851475143))
