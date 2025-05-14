#Write a simple python program to solve towers of hanoi problem.
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, auxiliary, source, destination)
n = 4
hanoi(n, 'A', 'B', 'C')