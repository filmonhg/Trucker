(ns bitcoin
  (:use     [streamparse.specs])
  (:gen-class))

(defn bitcoin [options]
   [
    ;; spout configuration
    {"kafka-spout" (python-spout-spec
          options
          "spouts.kafkaconsumer.KafkaSpout"
          ["transaction"]
          )
    }
    ;; bolt configuration
    { "counter-bolt" (python-bolt-spec
          options
          {"kafka-spout" ["transaction"]}
          "bolts.counter.TransactionCounter"
          [ ]
          :p 1
          )
    }

  ]
)
