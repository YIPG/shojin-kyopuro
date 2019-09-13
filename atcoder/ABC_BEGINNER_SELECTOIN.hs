main = do 
  a <- getLine
  bc <- getLine
  text <- getLine
  let abc = a ++ " " ++ bc
  let ans = sum $ map read (words abc)
  putStrLn $ (show ans) ++ " " ++ text