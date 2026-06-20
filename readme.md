# Python Operators - Complete Guide

## 1. Arithmetic Operators

Mathematical calculations ke liye use hote hain.

| Operator | Description         | Example  |
| -------- | ------------------- | -------- |
| `+`      | Addition            | `a + b`  |
| `-`      | Subtraction         | `a - b`  |
| `*`      | Multiplication      | `a * b`  |
| `/`      | Division            | `a / b`  |
| `//`     | Floor Division      | `a // b` |
| `%`      | Modulus (Remainder) | `a % b`  |
| `**`     | Exponentiation      | `a ** b` |

### Example

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

### Use Cases

* Calculator
* Percentage calculation
* Scientific calculations
* Data analysis

---

# 2. Assignment Operators

Variables me value assign karne ke liye.

| Operator | Example   | Equivalent   |
| -------- | --------- | ------------ |
| `=`      | `x = 5`   | Assign       |
| `+=`     | `x += 3`  | `x = x + 3`  |
| `-=`     | `x -= 3`  | `x = x - 3`  |
| `*=`     | `x *= 3`  | `x = x * 3`  |
| `/=`     | `x /= 3`  | `x = x / 3`  |
| `%=`     | `x %= 3`  | `x = x % 3`  |
| `//=`    | `x //= 3` | `x = x // 3` |
| `**=`    | `x **= 3` | `x = x ** 3` |

### Example

```python
x = 10

x += 5
print(x)

x *= 2
print(x)
```

### Use Cases

* Counters
* Score systems
* Loop updates

---

# 3. Comparison Operators

Do values compare karne ke liye.

| Operator | Meaning            |
| -------- | ------------------ |
| `==`     | Equal              |
| `!=`     | Not Equal          |
| `>`      | Greater Than       |
| `<`      | Less Than          |
| `>=`     | Greater Than Equal |
| `<=`     | Less Than Equal    |

### Example

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a > b)
```

### Use Cases

* Login validation
* Age checking
* Sorting conditions

---

# 4. Logical Operators

Multiple conditions combine karne ke liye.

| Operator | Meaning                |
| -------- | ---------------------- |
| `and`    | Dono True hone chahiye |
| `or`     | Koi ek True            |
| `not`    | Reverse karta hai      |

### Example

```python
age = 20
citizen = True

print(age >= 18 and citizen)

print(age < 18 or citizen)

print(not citizen)
```

### Use Cases

* Authentication
* Permission systems
* Decision making

---

# 5. Identity Operators

Memory location compare karte hain.

| Operator | Meaning          |
| -------- | ---------------- |
| `is`     | Same Object      |
| `is not` | Different Object |

### Example

```python
a = [1,2]
b = a
c = [1,2]

print(a is b)
print(a is c)

print(a == c)
```

### Output

```python
True
False
True
```

### Use Cases

* Checking None

```python
if data is None:
    print("No Data")
```

---

# 6. Membership Operators

Collection me value present hai ya nahi.

| Operator | Meaning     |
| -------- | ----------- |
| `in`     | Present     |
| `not in` | Not Present |

### Example

```python
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)

print("grapes" not in fruits)
```

### Use Cases

* Search
* Validation
* Permission checking

---

# 7. Bitwise Operators

Bits level pe operations.

| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left Shift  |    |
| `>>`     | Right Shift |    |

### Example

```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)
```

### Use Cases

* Networking
* Cryptography
* Performance optimization

---

# 8. Walrus Operator (Python 3.8+)

Operator: `:=`

### Example

```python
if (n := len("Python")) > 5:
    print(n)
```

### Use Cases

* Shorter code
* Loops
* Conditional assignments

---

# 9. Ternary Operator

Single line if-else.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

### Use Cases

* Quick assignments
* UI labels
* Status checks

---

# 10. Operator Precedence

Priority order:

```text
()
**
+x, -x, ~x
*, /, //, %
+, -
<<, >>
&
^
|
==, !=, >, <, >=, <=
not
and
or
```

### Example

```python
print(2 + 3 * 4)
```

Output:

```python
14
```

Because multiplication pehle execute hota hai.

---

# Quick Cheat Sheet

```python
# Arithmetic
+  -  *  /  //  %  **

# Assignment
= += -= *= /= //= %= **=

# Comparison
== != > < >= <=

# Logical
and or not

# Identity
is is not

# Membership
in not in

# Bitwise
& | ^ ~ << >>

# Walrus
:=

# Ternary
a if condition else b
```

---

# Real World Usage Summary

| Operator Type | Common Use            |
| ------------- | --------------------- |
| Arithmetic    | Calculations          |
| Assignment    | Updating variables    |
| Comparison    | Conditions            |
| Logical       | Multiple conditions   |
| Identity      | Checking same object  |
| Membership    | Searching             |
| Bitwise       | Low-level programming |
| Walrus        | Compact code          |
| Ternary       | One-line decisions    |

Happy Coding 🚀
