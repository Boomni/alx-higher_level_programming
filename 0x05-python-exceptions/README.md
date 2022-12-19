# 0x05-python-exceptions

Errors and exceptions are two related but distinct concepts in programming. Errors refer to issues that prevent a program from running correctly, such as syntax errors or missing dependencies. Exceptions are runtime errors that occur when a program is executing. They can be caused by invalid input, resource unavailability, or other unexpected conditions.

Exceptions can be handled using try-except blocks. When a potential exception-causing statement is placed in a try block, the program will attempt to execute it. If an exception is raised, the program will immediately stop executing the try block and move to the except block, which can contain code to handle the exception. This allows you to gracefully handle exceptions and continue executing your program rather than having it crash.

You may need to use exceptions when you want to handle unexpected runtime errors, or when you want to validate user input or other data to ensure that it meets certain criteria.

To correctly handle an exception, you should place the code that may raise the exception in a try block and provide an except block to handle the exception. It is also a good idea to include a finally block, which will be executed regardless of whether an exception was raised. This can be useful for performing clean-up actions, such as closing files or releasing resources.

The purpose of catching exceptions is to prevent your program from crashing when an exception is raised and to allow you to gracefully handle the exception and continue executing your program.

You can raise a built-in exception by using the raise keyword and specifying the exception you want to raise.

You may need to implement a clean-up action after an exception if your program has acquired resources, such as file handles or database connections, that need to be released even if an exception is raised. This can be done using a finally block, which will be executed regardless of whether an exception was raised.
