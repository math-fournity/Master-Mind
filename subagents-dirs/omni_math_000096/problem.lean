/-- AoPS omni_math Problem (id=96, source=china_team_selection_test, difficulty=9.0 )
    Informal statement: Find all functions $f:\mathbb {Z}\to\mathbb Z$, satisfy that for any integer ${a}$, ${b}$, ${c}$,
$$2f(a^2+b^2+c^2)-2f(ab+bc+ca)=f(a-b)^2+f(b-c)^2+f(c-a)^2$$
    Answer: f(x) = 0 \text{ or } f(x) = x
    Solution: 
We are given the functional equation for \( f: \mathbb{Z} \to \mathbb{Z} \):
\[
2f(a^2 + b^2 + c^2) - 2f(ab + bc + ca) = f(a - b)^2 + f(b - c)^2 + f(c - a)^2
\]
for any integers \( a, b, \) and \( c \).

To find all such functions \( f \), we proceed as follows:

### Step 1: Initial Analysis
Let \( P(a, b, c) \) denote the given assertion. Adding \( P(a, b, c) \) and \( P(-a, -b, -c) \) yields:
\[
2f(a^2 + b^2 + c^2) - 2f(ab + bc + ca) = f(a - b)^2 + f(b - c)^2 + f(c - a)^2.
\]
This simplifies 
-/
