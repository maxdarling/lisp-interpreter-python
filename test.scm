;; Basic Scheme Hello World with function call
;; Define a simple greeting function
(define (greet name)
  (display "Hello, ") ;; inline comment!
  (display name)
  (display "! Welcome to Scheme!")
  (newline))

;; Call the function with a parameter
(greet "World")

;; Another example with a different name
(greet "Programmer")

;; Simple arithmetic function call
(+ 5 3)