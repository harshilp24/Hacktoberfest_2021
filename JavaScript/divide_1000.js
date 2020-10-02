//it divides the n into 2 parts untill it's less 50. At the end you've got the number that's left and the number of iteration.
let n = 1000
    let numbl = 0
    do  {
        numbl++
        n/=2
    }
    while (n>50)
    console.log (n, numbl, 'циклов')  
    
