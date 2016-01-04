;By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
;What is the 10 001st prime number?
(defn is-prime? [n]
  (empty? (filter #(= 0 (mod n %)) (range 2 n))))

(defn nth-prime [n]
  (last (take n (filter #(is-prime? %) (iterate inc 2)))))

(nth-prime 10001)

