(ns hartisabuttocks.core 
  (:require [clojure.string :as str])
            ;[clojure.math.numeric-tower :as math])
  (use clojure.java.io)
  )

;(:require [clojure.math.numeric-tower :as math]
 ;         [clojure.math.combinatorics :as combo])
(def myList #(list %))

(def GeneticMap {:label :id :sequence :lengthSeq})
(def AAMap {:GeneticMap :readingFrame })
(def DNAMap {:GeneticMap :codingRegion })
(def RNAMap { :GeneticMap :RNAtype})
(def database {})
;(def DNA #{:keys [label id sequence lengthSeq codingRegion]})
;(def AA {:keys [label id sequence lengthSeq readingFrame]})
;(def RNA #{:keys [label id sequence lengthSeq  RNAType]} )
(defn newGMap [label id mysequence lengthSeq]
  (into (hash-map) [ [:label label] [:id id] [:sequence mysequence] [:lengthSeq lengthSeq]]))

(defn newAAMap [label id mysequence lengthSeq readingFrame]
  (conj (newGMap label id mysequence lengthSeq) 
        (into (hash-map) [[:readingFrame readingFrame]])))

(defn newDNAMap [label id mysequence lengthSeq codingRegion]
  (conj (newGMap label id mysequence lengthSeq) 
        (into (hash-map) [[:codingRegion codingRegion]])))

(defn newRNAMap [label id mysequence lengthSeq rtype]
  (conj (newGMap label id mysequence lengthSeq) 
        (into (hash-map) [[:RNAtype rtype]])))

(defn printSequence[aMap]
         (let[{:as all} aMap]
           (println all)))

(defn makeDatabase [filepath]
  (with-open [rdr (reader filepath)]
    (doseq [command (str/split (line-seq rdr) #" ")]
      (cond (= (first command) "A") (assoc-in database [(count database)] (newAAMap (rest command)))
        (= (first command) "D")(assoc-in database [(count database)] (newDNAMap (rest command)))
        (= (first command) "R")(assoc-in database [(count database)] (newRNAMap (rest command)))
        (= (first command) "P") (printSequence (re-find #(rest command)))    
      ))))


(defn destructureDNA[]  
  (let [{:keys [codingRegion] {:keys [label id sequence lengthSeq]}:GeneticMap } DNAMap]
    (println label id sequence lengthSeq codingRegion)))


(defn gcd ; this is a comment
 "finds the greates common denominator"
 [x y] ; there are two variables being passed in in the function call
 (loop [val1 x ; two local variables that will hold the values passsed in
        val2 y]
   (if (=(mod val1 val2) 0) ; the base case, which will give the answer
         val2; the answer
     (recur val2 ; I pass it the second value instead of swapping it around
            (mod val1 val2)));this evaluates the two functions and passes it
   ))
(defn exp [ x n]
  "returns an exponent"
  (reduce *' (repeat n x)))

(defn split-digits [n] ; int to string
  (map #(- (int %) 48) (seq (str n))))

(defn sumOfDigits [ds]
  (reduce + ds))

(defn expsSum[a d]
  (sumOfDigits(split-digits(exp a d))))

(defn fib-step [[a b]]
  [b (+ a b)])

 (defn tn2minus1 [x]
   (-(* 2 x x)1))
 
 (defn squrem
   [number power]
   (mod 
     (+' (exp ( -' number 1N) power)(exp (+' number 1N)power ))
   (exp number 2N)
   ))
 
 (defn maxSqurem
   [x]
   (loop[start 1N
         answer 0N]
     (if (= start ( + x x))
         answer
   (recur (inc start )
          (if(> (squrem x start) answer)(squrem x start) answer ))))) 
  ; start))))
 (defn problem120[]
   ;(print 5)
   (loop[a 3
         oanswer 0N]
     ;(print a)
        (if(= a 1001N)
          oanswer
          (recur (inc a)(+' (maxSqurem a) oanswer)))))
 (defn isPrime [y]
 ; (ns clojure.math.numeric-tower)
 
 (loop [upperbound (java.lang.Math/sqrt y)
      start 2N]
  (if (=(mod y start)0)
   0
  (if (>= y upperbound)
   1
  (recur upperbound (inc start))))))
(defn harshad [x]
  (if(=(mod x (sumOfDigits(split-digits x)))0)
    1)
  )
(defn truncatableharshad [x]
  (loop [value x]
    (println value)
    (if (= value 0N)
    1
     (if (= (harshad value)1)
       (recur (/ value 10N) 
    )))))
(defn fib-seq []
  (map first (iterate fib-step [0N 1N])))

(defn problem56[]
  ( max
    (let [answer (0)]
      (for [a (range 1 100)
            b (range 1 100)
            :let [answer (into answer '((expsSum a b)))]
            :when(<= (apply max answer) (expsSum a b))
            ]answer))))

  (defn exp2 [x n z]
  (loop [acc 1 n n]
    (if (zero? n) acc
        (recur (mod (* x acc)z) (dec n)))))

(defn tetration [x y]
  (let [tot108 100000000N]
      (loop[ answer x
            iterations y]
        (if(= iterations 1N)
           answer
    (recur (exp2 x answer tot108)
           (dec iterations))))))

(defn factorial
  [x] 
  (loop [number x
         factSum 1N]
    (if (= number 1)
      factSum ;why does this need to be here?
    (recur (dec number)(* factSum number)))))
  
(defn totient
  [x]; a single variable
  "finds all  coprime numbers in raltion the the given number 
    less than the given number"
  (loop [upperbound (- x 1N) ; there is a new local variable that holds x-1
         totient 1N]; initialize a new variable called totient that will hold the variable
    (if (= upperbound 1N); the base case
      totient; the final answer
      (recur(- upperbound 1); the first parameter as discussed before
            ( if (=(gcd x upperbound)1N) 
              (+ totient 1N); if the above statement is true
              totient) ; if the statement is false
            ))))