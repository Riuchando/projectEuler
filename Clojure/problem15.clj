
  (count [1 2 3])

  (defn validate-word [word]
  ; your code
  (map #(=  %2 2 )(frequencies word))
  )
  (not (every? false? (map #( = (second %) 1 )  (into [](frequencies "abcabc")))))
  (not-any? false? (map #( = (second %) 1 )  (into [](frequencies "abca"))))
  (not-any? false? (map #( = (second %) 1 )  (into [](frequencies "abc"))))
  (apply = (map #(second %)(into [](frequencies (clojure.string/lower-case "abc")))))
  (apply = (map #(second %)(into [](frequencies (clojure.string/lower-case "abcabcABC")))))
  (apply =  [1 1 1])
  (into [] (frequencies "abcabc"))

(count (filter #(>  (int (key %)) 109) (frequencies "hai")))
