import matplotlib.pyplot as plt

marks = list(map(int, input("Enter marks of the students (space-separated): ").split()))

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(marks, bins=bins, edgecolor="black", color="skyblue")

plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.title("Histogram of Students' Marks")

plt.show()
