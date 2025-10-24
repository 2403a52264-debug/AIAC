"""
Simple Linear Optimization Example
Problem: Maximize profit from selling two products
"""

def simple_optimization():
    """
    Simple linear optimization using basic math
    """
    # Problem: Maximize profit = 3x + 4y
    # Constraints: 2x + y <= 100, x + 2y <= 80, x >= 0, y >= 0
    
    # Find corner points of feasible region
    # Point 1: (0, 0) - origin
    point1 = (0, 0)
    profit1 = 3 * point1[0] + 4 * point1[1]
    
    # Point 2: (0, 40) - intersection of y-axis and second constraint
    point2 = (0, 40)
    profit2 = 3 * point2[0] + 4 * point2[1]
    
    # Point 3: (50, 0) - intersection of x-axis and first constraint
    point3 = (50, 0)
    profit3 = 3 * point3[0] + 4 * point3[1]
    
    # Point 4: (40, 20) - intersection of both constraints
    # Solving: 2x + y = 100, x + 2y = 80
    # x = 40, y = 20
    point4 = (40, 20)
    profit4 = 3 * point4[0] + 4 * point4[1]
    
    # Find maximum profit
    points = [point1, point2, point3, point4]
    profits = [profit1, profit2, profit3, profit4]
    
    max_profit = max(profits)
    best_point = points[profits.index(max_profit)]
    
    return best_point, max_profit

def solve_with_scipy():
    """
    Simple optimization using scipy
    """
    try:
        from scipy.optimize import linprog
        
        # Objective: maximize 3x + 4y = minimize -3x - 4y
        c = [-3, -4]
        
        # Constraints: 2x + y <= 100, x + 2y <= 80
        A = [[2, 1], [1, 2]]
        b = [100, 80]
        
        # Bounds: x >= 0, y >= 0
        bounds = [(0, None), (0, None)]
        
        # Solve
        result = linprog(c, A_ub=A, b_ub=b, bounds=bounds)
        
        return result.x, -result.fun  # Convert back to maximization
        
    except ImportError:
        print("Scipy not available. Using manual method.")
        return None, None

# Test the optimization
if __name__ == "__main__":
    print("SIMPLE LINEAR OPTIMIZATION")
    print("=" * 40)
    print("Problem: Maximize profit = 3x + 4y")
    print("Constraints: 2x + y ≤ 100, x + 2y ≤ 80")
    print("Variables: x ≥ 0, y ≥ 0")
    print()
    
    # Method 1: Manual calculation
    print("Method 1: Manual Calculation")
    print("-" * 30)
    best_point, max_profit = simple_optimization()
    print(f"Optimal solution: x = {best_point[0]}, y = {best_point[1]}")
    print(f"Maximum profit: ${max_profit}")
    print()
    
    # Method 2: Using scipy (if available)
    print("Method 2: Using Scipy")
    print("-" * 30)
    scipy_solution, scipy_profit = solve_with_scipy()
    
    if scipy_solution is not None:
        print(f"Optimal solution: x = {scipy_solution[0]:.1f}, y = {scipy_solution[1]:.1f}")
        print(f"Maximum profit: ${scipy_profit:.2f}")
    else:
        print("Scipy not available - install with: pip install scipy")
    
    print()
    print("Verification:")
    print(f"Constraint 1: 2({best_point[0]}) + {best_point[1]} = {2*best_point[0] + best_point[1]} ≤ 100")
    print(f"Constraint 2: {best_point[0]} + 2({best_point[1]}) = {best_point[0] + 2*best_point[1]} ≤ 80")