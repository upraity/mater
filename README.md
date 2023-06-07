# Mater - Collection of Mathematical Python Functions and Classes.

Mater is a comprehensive repository that houses a diverse collection of Python functions, classes, and generators. It is organized into different directories for better code readability and maintainability.

## Repository Structure

The repository has the following directory structure:

- **main**: This directory contains the `mater.py` file, which serves as the main entry point for accessing all the functions, classes, and generators provided by Mater.

- **functions**: This directory contains individual files for each function implemented in Mater. The separate files, such as `factorial.py` and `is_prime.py`, focus on specific mathematical tasks and provide dedicated functions for those operations.

- **classes**: The classes directory includes separate files for each class implemented in Mater. The files, such as `Square.py` and `Rectangle.py`, encapsulate the logic and functionality of different shapes and provide methods for calculating their properties.


## Usage

To utilize Mater in your Python projects, follow the steps below:

1. Clone the repository:

   ```
   git clone https://github.com/amanbabuhemant/mater.git
   ```

2. Import the required modules into your Python script:

   ```python
   from mater import factorial, is_prime, Square, Rectangle
   ```
   or just import everything
   ~~~python
   from mater import *
   ~~~
3. Begin utilizing the functions and classes:

   ```python
   # Example usage of functions
   fact = factorial(5)
   is_prime_number = is_prime(7)

   # Example usage of classes
   square = Square(5)
   rect = Rectangle(4, 6)
   ```

Feel free to explore the repository and modify the code to suit your specific requirements. Contributions and improvements are highly encouraged.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## About the Developer

Mater was built by **Aman Babu Hemant**, a college student with a keen interest in programming and mathematics. As a continuously evolving project, contributions and feedback from the community are greatly appreciated. Together, we can enhance the functionality and versatility of Mater.
