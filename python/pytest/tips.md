### Tips
#### verify error message
- You can test error message by following ways
1. Use assertRaisesRegex
  - you can specify message for verification as second argument

        ```python
        class TestDivideFunction(unittest.TestCase):
            def test_divide_by_zero_message(self):
                with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
                    divide(10, 0)
        ```
2. Use assertRaises with context manager
   - extract the error message from context manager to verify it

    ```python
    class TestDivideFunction(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as cm:
            divide(10, 0)
        # You can access the exception instance if needed
        self.assertEqual(str(cm.exception), "Cannot divide by zero")
    ```