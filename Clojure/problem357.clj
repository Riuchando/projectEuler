;Consider the divisors of 30: 1,2,3,5,6,10,15,30.
;It can be seen that for every divisor d of 30, d+30/d is prime.

;Find the sum of all positive integers n not exceeding 100 000 000
;such that for every divisor d of n, d+n/d is prime.
; (conj '() 10)
(defn divisors [number]
  (loop [n 1
         return '()]
    (cond (= n number) (conj  return n)
          (= (mod number n) 0) (recur (inc n) (conj  return n))
          :else
          (recur (inc n) return))))

; (divisors 10)
(defn is-prime? [n]
  (empty? (filter #(= 0 (mod n %)) (range 2 n))))
; (divisors 30)

(println (map #(+ (/ 30 %) %) (divisors 30)))
(defn primeGenrating [d]
  (every? true? (map #(is-prime? (+ (/ d %) %)) (divisors d))))

(println (primeGenrating 30))

; too slow
; (println (reduce + (filter #(primeGenrating %) (range 2 100000000))))
