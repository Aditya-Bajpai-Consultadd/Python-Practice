#Write a program to manage a voting system where each voter can 
# vote only once. Use sets to track voters and dictionaries to 
# count votes for candidates.

def main():
    voters = set()
    votes = {}
    while True:
        print("1. Vote")
        print("2. View Votes")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            vote(voters,votes)
        elif choice == 2:
            view_votes(votes)
        elif choice == 3:
            break
        else:
            print("Invalid choice")

def vote(voters,votes):
    voter = input("Enter voter name: ")
    if voter in voters:
        print("You have already voted")
    else:
        voters.add(voter)
        candidate = input("Enter candidate name: ")
        if candidate in votes:
            votes[candidate]+=1
        else:
            votes[candidate]=1
        print("Vote cast successfully")

def view_votes(votes):
    for i in votes:
        print(i,":",votes[i])


main()