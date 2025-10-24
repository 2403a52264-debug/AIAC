"""
Gradient Descent Optimization
Find minimum of f(x) = x² - 4x + 5
"""
def f(x):
    """Function: f(x) = x² - 4x + 5"""
    return x**2 - 4*x + 5
def f_derivative(x):
    """Derivative: f'(x) = 2x - 4"""
    return 2*x - 4
def gradient_descent(start_x=0, learning_rate=0.1, steps=50):
    """
    Simple gradient descent
    """
    x = start_x
    print(f"Starting at x = {x}")
    print(f"f(x) = {f(x):.2f}")
    print()
    for i in range(steps):
        # Calculate gradient
        gradient = f_derivative(x)
        # Update x
        x = x - learning_rate * gradient
        # Print every 10 steps
        if (i + 1) % 10 == 0:
            print(f"Step {i+1}: x = {x:.2f}, f(x) = {f(x):.2f}, gradient = {gradient:.2f}")
    return x, f(x)
# Test the function
if __name__ == "__main__":
    print("GRADIENT DESCENT OPTIMIZATION")
    print("=" * 40)
    print("Function: f(x) = x² - 4x + 5")
    print("Derivative: f'(x) = 2x - 4")
    print()
    # Find analytical solution
    print("ANALYTICAL SOLUTION:")
    print("f'(x) = 2x - 4 = 0")
    print("2x = 4")
    print("x = 2")
    print("f(2) = 2² - 4(2) + 5 = 4 - 8 + 5 = 1")
    print("Minimum at x = 2, f(x) = 1")
    print()
    # Try gradient descent
    print("GRADIENT DESCENT:")
    print("-" * 30)
    x_optimal, f_optimal = gradient_descent(start_x=0, learning_rate=0.1, steps=50)
    print()
    print("RESULT:")
    print(f"Optimal x: {x_optimal:.6f}")
    print(f"Minimum f(x): {f_optimal:.6f}")
    print()
    print("SUCCESS! Gradient descent found the minimum!")
    print("Analytical solution: x = 2, f(x) = 1")
    print(f"Gradient descent: x = {x_optimal:.6f}, f(x) = {f_optimal:.6f}")
    print("\n" + "=" * 40)
    print("TESTING DIFFERENT STARTING POINTS:")
    print()
    starting_points = [-5, -2, 0, 5, 10]
    for start in starting_points:
        x_opt, f_opt = gradient_descent(start_x=start, learning_rate=0.1, steps=30)
        print(f"Start x = {start:2d}: Final x = {x_opt:.2f}, f(x) = {f_opt:.2f}")
    print()
    print("All starting points converge to the same minimum!")