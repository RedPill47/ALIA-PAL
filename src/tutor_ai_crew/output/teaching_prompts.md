# Teaching Prompt for AI Tutor: Understanding Function Call Execution and Function Calls in Python

## Student: John Doe
### Course Title: Understanding Function Call Execution and Function Calls in Python

---

### Module 1: Introduction to Functions

**Objective**: Ensure that John understands what functions are and the basic structure of functions in Python.

**Teaching Strategy**:
1. **Define Functions**: Start by explaining what a function is, emphasizing that it's a block of reusable code designed to perform a specific task.
2. **Structure**: Show the basic structure of a function in Python:
   - Syntax: `def function_name(parameters):`
   - Provide a simple example, e.g.:
     ```python
     def greet(name):
         return f"Hello, {name}!"
     ```
3. **Engage**: Ask John to describe a function he might use in a real-world scenario. Encourage him to think of simple tasks (e.g., calculating the area of a rectangle).
4. **Recap**: Reinforce learning by summarizing key points: definition, purpose, and basic syntax.

---

### Module 2: Function Call Execution

**Objective**: Explain the process involved in executing a function call, the flow of execution, and how control returns back to the caller.

**Teaching Strategy**:
1. **Function Call Process**: Describe what happens when a function is called. Explain terms like "calling" and "function body”.
2. **Flow of Execution**: Use a flowchart or step-by-step guide to illustrate the process:
   - Call the function.
   - Move to the function body.
   - Execute the statements within the body.
   - Return to the caller with a result.
3. **Example Walkthrough**: Provide detailed commentary on a simple function call:
   ```python
   result = greet("Alice")
   print(result)
   ```
   - Discuss each step in this example. What happens when `greet("Alice")` is called?
4. **Q&A**: Invite John to ask questions throughout the explanation to clarify any points and ensure understanding.

---

### Module 3: Function Calls in Practice

**Objective**: Familiarize John with the syntax for function calling in practice and demonstrate various examples.

**Teaching Strategy**:
1. **Syntax Explanation**: Clearly articulate how to properly call a function. Discuss passing different types of arguments (positional vs keyword).
2. **Examples**: Provide a variety of short, practical code examples that John can run:
   ```python
   def add(a, b):
       return a + b

   sum_result = add(5, 3)
   ```
3. **Hands-on Activity**: Have John practice calling functions on his own. Give him different scenarios and have him write small functions and call them.
4. **Feedback**: Monitor John's code and provide constructive feedback on any errors in syntax or logic.

---

### Module 4: Practice and Challenges

**Objective**: Engage John with practical exercises that reinforce learning and identify common mistakes.

**Teaching Strategy**:
1. **Scenarios and Challenges**: Present John with sample problems that require using functions. Examples include:
   - Writing a function to calculate the square of a number.
   - Debugging a function with common mistakes embedded purposely.
2. **Common Mistakes Review**: Discuss common pitfalls in defining and calling functions, such as:
   - Forgetting to use parentheses.
   - Mismatched parameters.
3. **Interactive Practice**: Create a quiz based on the previous modules that tests John's comprehension of function calls and execution processes.
   - Include a mix of multiple-choice and code correction questions.
4. **Review Quiz Answers**: Go through the quiz with John, discussing correct and incorrect answers, reinforcing understanding, and addressing any areas of confusion.

---

**Conclusion**: 
Throughout the course, maintain a supportive environment where John feels comfortable asking questions. Encourage him to express any difficulties he encounters and provide positive reinforcement to build his confidence in using functions in Python. 

---

Happy teaching!