#Print the fibonnaci series

def gen_fib(n):
    fib_seq = [0,1]
    while len(fib_seq)<n:
        next_term= fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_term)
        return fib_seq
    user_input= input("Enter the length of fibonnaci series:")
    num_input= int(num_input)
    seq= gen_fib(num_input)
    print("The first (num_input) terms if fibonnaci series is (seq) ")
    

    
 