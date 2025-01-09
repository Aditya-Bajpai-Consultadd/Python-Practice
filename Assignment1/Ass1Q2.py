#Develop a program to take user input for multiple numbers, 
# store them in a list, and compute basic statistical metrics 
# like mean, median, mode.

def main():
    numbers  = list(map(int,input("Enter numbers separated by space: ").split(" ")))
    print("Mean: ",mean(numbers))
    print("Median: ",median(numbers))
    print("Mode: ",mode(numbers))
    

def mean(numbers):
    return sum(numbers)/len(numbers)

def median(numbers):
    n = len(numbers)
    numbers.sort()
    if n%2 == 0:
        return (numbers[n//2]+numbers[n//2-1])/2
    return numbers[n//2]

def mode(numbers):
    freq = {}
    for i in numbers:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    ans = 0
    for i in freq:
        if freq[i]>ans:
            ans=i
    return ans

main()
