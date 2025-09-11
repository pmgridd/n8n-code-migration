import sys

class App:
    @staticmethod
    def main():
        print("Starting Python equivalent of IFEVAL.CBL")
        print("---------------------------------------")

        App.example1()
        App.example2()
        App.example3()
        App.example4()
        App.example5()
        App.example6()
        App.example7()

        print("---------------------------------------")
        print("Processing complete.")

    # Example 1: IF statement, 2 alphanumeric items.
    @staticmethod
    def example1():
        print("\n--- Example 1: Comparing two alphanumeric items ---")
        alpha1 = "cucumber"
        alpha2 = "radish"
        result_of_compare = ""

        # Compare two alphanumeric items
        if alpha1 == alpha2:
            result_of_compare = "equal"
        else:
            result_of_compare = "different"
        print(f"'{alpha1}' and '{alpha2}' are {result_of_compare}")

        alpha2 = "cucumber"
        if alpha1 == alpha2:
            result_of_compare = "equal"
        else:
            result_of_compare = "different"
        print(f"'{alpha1}' and '{alpha2}' are {result_of_compare}")

    # Example 2: IF statement, alphanumeric field vs literal.
    @staticmethod
    def example2():
        print("\n--- Example 2: Comparing alphanumeric field vs literal ---")
        alpha1 = "foobar"
        result_of_compare = ""

        if alpha1 == "foobar":
            result_of_compare = "equal"
        else:
            result_of_compare = "different"
        print(f"'{alpha1}' and 'foobar' are {result_of_compare}")

    # Example 3: Verify a numeric item contains numeric data.
    @staticmethod
    def example3():
        print("\n--- Example 3: Verifying numeric data ---")
        numeric_input = "garbage"
        numeric2 = 0 # Initialize with a default value

        try:
            numeric2 = int(numeric_input)
            numeric2 += 1
        except ValueError:
            print(f"'{numeric_input}' is not numeric. Initializing to 1.")
            numeric2 = 1
        print(f"Value of numeric2: {numeric2}")

        numeric_input = "123"
        try:
            numeric2 = int(numeric_input)
            numeric2 += 1
            print(f"'{numeric_input}' is numeric. Incremented value: {numeric2}")
        except ValueError:
            # This part will not be executed for "123"
            pass

    # Example 4: Verify a numeric item is greater than zero.
    @staticmethod
    def example4():
        print("\n--- Example 4: Verifying a numeric item is greater than zero ---")
        numeric1 = 0
        numeric2 = 100

        if numeric1 > 0:
            numeric2 = numeric2 / numeric1
        else:
            print("numeric1 is not greater than zero. Avoiding division by zero.")
            numeric2 = numeric2 - 1
        print(f"Result of numeric2: {numeric2}")

    # Example 5: IF statement, two numeric fields.
    @staticmethod
    def example5():
        print("\n--- Example 5: Comparing two numeric fields ---")
        numeric1 = 7
        numeric2 = 36
        result_of_compare = ""

        if numeric1 > numeric2:
            result_of_compare = "numeric-1"
        else:
            result_of_compare = "numeric-2"
        print(f"Between {numeric1} and {numeric2}, the greater is: {result_of_compare}")

    # Example 6: EVALUATE statement (like switch/if-else-if).
    @staticmethod
    def example6():
        print("\n--- Example 6: EVALUATE statement (like switch/if-else-if) ---")
        numeric1 = 8
        numeric2 = 13
        result_of_compare = ""

        if numeric1 > numeric2:
            result_of_compare = "numeric-1"
        elif numeric1 < numeric2:
            result_of_compare = "numeric-2"
        else:
            result_of_compare = "equal"
        print(f"Evaluation of {numeric1} and {numeric2}: {result_of_compare}")

    # Example 7: EVALUATE statement, two conditions.
    @staticmethod
    def example7():
        print("\n--- Example 7: EVALUATE statement with two conditions ---")
        numeric1 = 8
        numeric2 = 13
        alpha1 = "THX-1138"
        alpha2 = "Terminator"
        result_of_compare = ""

        if numeric1 > numeric2 and alpha1.startswith("THX"):
            result_of_compare = "THX and numeric-1"
        elif numeric1 < numeric2 and alpha1.startswith("THX"):
            result_of_compare = "THX and numeric-2"
        elif numeric1 == numeric1 and alpha2 == "Terminator": # This condition is always true in the COBOL example
            result_of_compare = "Terminator and equal numbers"
        else:
            result_of_compare = "undefined"
        print(f"Result of complex evaluation: {result_of_compare}")

if __name__ == '__main__':
    App.main()