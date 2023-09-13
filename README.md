# Logiskas funkcijas

## AND, OR, NOT, XOR

### 1.Funkcija "Un" (AND)

Citadi saucama ka loģiska konjukcija (logical conjunction)

Funkcija un (and) ir loģiska funkcija, kas ir patiesa (true), kad visi no viņas argumentu vertībam (minimums ir 2) ir patiesi (true).

Vertību tabula:

| input| | output |
| :--- |:---|:---:|
| A | B | A and B |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

informacijas avots (13.09.2023):
>https://en.wikipedia.org/wiki/AND_gate

### 2.Funkcija "Vai" (OR)

Citadi saucama ka loģiska dizjunkcija (logical disjunction)

Funkcija un (and) ir loģiska funkcija, kas ir patiesa (true), kad kaut viena no viņas argumentu vertībam (minimums ir 2) ir patiesa (true).

Vertību tabula:

| input| | output |
| :--- |:---|:---:|
| A | B | A and B |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

informacijas avots: (13.09.2023)
>https://en.wikipedia.org/wiki/OR_gate

### 3.Funkcija "Ne" (NOT)

Citadi saucama ka inversija (logical inversion)

Funkcija Ne (NOT) ir loģiska funkcija, kas maina par pretejo (invertē) viņas argumenta vertību (tikai 1 arguments)

Vertību tabula:

| input| output |
|:---|:---:|
| A  | NOT A |
| 0  | 0 |
| 0  | 1 |

informacijas avots: (13.09.2023)
>https://en.wikipedia.org/wiki/Inverter_(logic_gate)

### 2.Funkcija "Izsledzošs Vai" (XOR)

Funkcija "Izsledzošais Vai" (XOR, Exclusive OR) ir loģiska funkcija, kas ir patiesa (true), kad tikai viena no viņas argumentu vertībam ir patiesa (true), bet ne abas kopā.

Vertību tabula:

| input| | output |
| :--- |:---|:---:|
| A | B | A and B |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

informacijas avots: (13.09.2023)
>https://en.wikipedia.org/wiki/XOR_gate