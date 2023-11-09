function Analyse(A)
    odd = 0
    even = 0
    for a in A
        if a % 2 == 0
            even += 1
        else
            odd += 1
        end
    end
    println("Odd: ", odd)
    println("Even: ", even)
end

Analyse(rand(0:10, 100))