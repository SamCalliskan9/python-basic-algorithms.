Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... import random
... import time
... 
... def banner():
...     print("-" * 50)
...     print("SYSTEM DIAGNOSTİC & TASK ANALYZER")
...     print("-" * 50)
... 
... def get_user_task():
...     task = input("Enter a task name to analyze:")
...     return task
... 
... def evaluate_task():
...     print(f"\nAnalyzing task: {task}...")
...     time.sleep(1)
...     difficulty = random.choice(["Easy", "Meduim", "Hard"])
...     duration = random.randint(1,120)
...     priority = random.randint(1,5)
... 
...     return difficulty, duration, priority
... 
... def display_result(task, difficulty, duration, priority):
...     print("\n--- Task Report ---")
...     print(f"Task Name: {task}")
...     print(f"Difficulty: {difficulty}")
...     print(f"Estimated Time: {duration}")
...     print(f"Priority : {priority}/5")
... 
...     if priority >= 4:
...         print("Status : HİGH PRIORITY - Complete soon!")
...     elif priority == 3:
...         print("Status : MEDIUM PRIORITY - Plan it properly.")
...     else:
...         print("Status : LOW PRIORITY - Not urgent.")
... 
... def main():
    banner()

    while True:
        task = get_user_task()
        diff, dur, pr = evaluate_task(task)
        display_result(task, diff, dur, pr)

        again = input("\nAnalyze another task? (y/n):").lower()
        if again != "y":
            print("Exiting system...")
            break

if __name__ == "__main__":
    main()

