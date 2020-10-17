digits :: Int -> [Int]
digits n = if n < 10 then [n]
            else (rem n 10) : digits (quot n 10)


main = do
    print(digits 123)

