import Data.Maybe (fromMaybe)

fizzes = [Nothing, Nothing, Just "Fizz"]

buzzes = [Nothing, Nothing, Nothing, Nothing, Just "Buzz"]

num = show <$> [1..]

fizzbuzzes = zipWith (<>) (cycle f) (cycle b)

finalfbs n = zipWith fromMaybe (map show [1..n]) fbs

main :: IO()
main = print $ finalfbs 20

