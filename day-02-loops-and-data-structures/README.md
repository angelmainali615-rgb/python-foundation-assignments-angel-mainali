# Day 02 – Loops and Data Structures

## Topics Covered

- `for` loops and `range()`
- `while` loops and `break`
- Modulo operator (`%`) for patterns
- Cleaning data with loops and `isinstance()`
- List comprehensions
- Built-in functions: `sorted()`, `sum()`, `len()`, `max()`
- Set operations: union, intersection, difference
- Dictionaries: iteration, filtering, and comprehensions
- Nested dictionaries
- Simple interactive menu using `while True` and `break`

## Exercises Completed

1. **Batch Processor** – Loop through batches 1–10 and print a checkpoint every 3 batches.
2. **Retry Simulation** – Simulate up to 3 retry attempts with early exit on success.
3. **Clean Numeric Values** – Filter a mixed list to keep only valid integers (loop + list comprehension).
4. **Sales List Analysis** – Sort sales, filter high values, add tax, compute total and average.
5. **Dataset Comparison** – Use sets to find union, intersection, and differences between two datasets.
6. **Student Score Dictionary** – Iterate over a dictionary, filter passing students, find top student, compute average.
7. **Nested Order Summary** – Work with nested dictionaries to summarize orders and add a new order.
8. **Stretch: Contact Book Menu** – Interactive contact book with add, search, delete, display, and exit options.

## What I Learned

- How to control loop execution using conditions and `break`.
- How to use the modulo operator to trigger actions at regular intervals.
- How to clean messy data by checking types with `isinstance()` and skipping invalid entries.
- How list and dictionary comprehensions can replace longer loops for filtering and transforming data.
- How to use set operations to compare groups of items.
- How to work with nested dictionaries and extract aggregated information (totals, counts, averages).
- How to build a simple text-based menu that keeps running until the user chooses to exit.

## Challenges Faced

- Understanding how `key=lambda item: item[1]` works with `max()` on dictionary items.
- Making sure loops stop correctly (avoiding infinite loops in the menu).
- Handling missing contacts in the contact book without crashing (using `if name in contacts`).
- Organizing code so each exercise is clear and easy to run separately.

## How to Run the Programs

1. Clone or open your GitHub repository:

   ```bash
   git clone <your-repo-url>
   cd <repo-folder>/day-02-loops-and-data-structures
   ```

2. Make sure you have Python installed:

   ```bash
   python --version
   # or
   python3 --version
   ```

3. Run each exercise individually from the terminal:

   ```bash
   python exercise-01-batch-processor.ipynb
   python exercise-02-retry-simulation.ipynb
   python exercise-03-clean-values.ipynb
   python exercise-04-sales-analysis.ipynb
   python exercise-05-dataset-comparison.ipynb
   python exercise-06-student-scores.ipynb
   python exercise-07-order-summary.ipynb
   python stretch-contact-book.ipynb
   
   ```

   On some systems you may need `python3` instead of `python`.

4. For the contact book (`stretch-contact-book.py`), follow the on-screen menu:
   - Enter `1` to add a contact
   - Enter `2` to search
   - Enter `3` to delete
   - Enter `4` to display all
   - Enter `5` to exit

All scripts are self-contained and do not require any external libraries beyond standard Python.