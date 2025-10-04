class CalculatorPlugin:
    name = "calculator"
    description = "Perform math calculations. Usage: use_plugin('calculator', expression='<math expression>')"

    def run(self, expression):
        try:
            # WARNING: eval is dangerous, but for demo purposes we restrict the builtins
            result = eval(expression, {"__builtins__": {}})
            return str(result)
        except Exception as e:
            return f"Calculation error: {e}"
