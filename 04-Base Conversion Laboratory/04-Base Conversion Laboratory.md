# CC 101 - ACTIVITY 4

**Name:** Mica Rose D. Merjudio  
**Course & Section:** BSCS 1-1  
**Date:** 09/30/26  
**Instructor:** Prof. John Mark Gabrentina  

---

## STATION 1

### 1. Convert $10011011_2$ to decimal

**Place values:**
* $2^7 = 128$
* $2^6 = 64$
* $2^5 = 32$
* $2^4 = 16$
* $2^3 = 8$
* $2^2 = 4$
* $2^1 = 2$
* $2^0 = 1$

**Digit $\times$ Place value:**
* $1 \times 128 = 128$
* $0 \times 64 = 0$
* $0 \times 32 = 0$
* $1 \times 16 = 16$
* $1 \times 8 = 8$
* $0 \times 4 = 0$
* $1 \times 2 = 2$
* $1 \times 1 = 1$

$$\text{Sum} = 128 + 0 + 0 + 16 + 8 + 0 + 2 + 1 = \boxed{155}$$

---

### 2. Convert $3466_8$ to decimal

**Place values:**
* $8^3 = 512$
* $8^2 = 64$
* $8^1 = 8$
* $8^0 = 1$

**Digit $\times$ Place value:**
* $3 \times 512 = 1536$
* $4 \times 64 = 256$
* $6 \times 8 = 48$
* $6 \times 1 = 6$

$$\text{Sum} = 1536 + 256 + 48 + 6 = \boxed{1846}$$

---

### 3. Convert $\text{F7C}_{16}$ to decimal

**Digit values (Hexadecimal):**  
$A = 10, B = 11, C = 12, D = 13, E = 14, F = 15$
* $F = 15$
* $7 = 7$
* $C = 12$

**Place values:**
* $16^2 = 256$
* $16^1 = 16$
* $16^0 = 1$

**Digit $\times$ Place value:**
* $15 \times 256 = 3840$
* $7 \times 16 = 112$
* $12 \times 1 = 12$

$$\text{Sum} = 3840 + 112 + 12 = \boxed{3964}$$

---

## STATION 2

### 1. Convert $224$ (decimal) to binary

| Operation | Quotient | Remainder |
| :--- | :---: | :---: |
| $224 \div 2$ | 112 | 0 |
| $112 \div 2$ | 56 | 0 |
| $56 \div 2$ | 28 | 0 |
| $28 \div 2$ | 14 | 0 |
| $14 \div 2$ | 7 | 0 |
| $7 \div 2$ | 3 | 1 |
| $3 \div 2$ | 1 | 1 |
| $1 \div 2$ | 0 | 1 |

$$\text{Answer (remainders read bottom to top): } 224_{10} = \boxed{11100000_2}$$

---

### 2. Convert $2430$ (decimal) to octal

| Operation | Quotient | Remainder |
| :--- | :---: | :---: |
| $2430 \div 8$ | 303 | 6 |
| $303 \div 8$ | 37 | 7 |
| $37 \div 8$ | 4 | 5 |
| $4 \div 8$ | 0 | 4 |

$$\text{Answer: } 2430_{10} = \boxed{4576_8}$$

---

### 3. Convert $1917$ (decimal) to hexadecimal

| Operation | Quotient | Remainder | Hex Digit |
| :--- | :---: | :---: | :---: |
| $1917 \div 16$ | 119 | 13 | D |
| $119 \div 16$ | 7 | 7 | 7 |
| $7 \div 16$ | 0 | 7 | 7 |

$$\text{Answer: } 1917_{10} = \boxed{77\text{D}_{16}}$$

---

## STATION 3

### 1. Grouping shortcut: Convert $11111010001_2$ to hexadecimal (without passing through decimal)

Split the binary string into 4-bit groups from right to left, padding the left group with leading zeros:

$$11111010001_2 \longrightarrow \underbrace{0111}_{\text{Left}} \quad \underbrace{1101}_{\text{Middle}} \quad \underbrace{0001}_{\text{Right}}$$

* **Left group ($0111_2$):** $0 \cdot 8 + 1 \cdot 4 + 1 \cdot 2 + 1 \cdot 1 = 7$
* **Middle group ($1101_2$):** $1 \cdot 8 + 1 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 13 \longrightarrow \text{D}$
* **Right group ($0001_2$):** $0 \cdot 8 + 0 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 1$

$$\text{Final Answer: } \boxed{7\text{D}1_{16}}$$

---

### 2. Grouping shortcut: Convert $1101110001_2$ to octal (without passing through decimal)

Split the binary string into 3-bit groups from right to left, padding the left group with leading zeros:

$$1101110001_2 \longrightarrow \underbrace{001}_{\text{Left 2}} \quad \underbrace{101}_{\text{Left 1}} \quad \underbrace{110}_{\text{Right 1}} \quad \underbrace{001}_{\text{Right 2}}$$

* **Left 2 group ($001_2$):** $0 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 1$
* **Left 1 group ($101_2$):** $1 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 5$
* **Right 1 group ($110_2$):** $1 \cdot 4 + 1 \cdot 2 + 0 \cdot 1 = 6$
* **Right 2 group ($001_2$):** $0 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 1$

$$\text{Final Answer: } \boxed{1561_8}$$

---

### 3. Expansion shortcut: Convert $2\text{E}8_{16}$ to binary

Replace each hex digit with its 4-bit binary equivalent:

* **$2_{16}$:** $0010_2$
* **$\text{E}_{16}$ ($14_{10}$):** $1110_2$
* **$8_{16}$:** $1000_2$

$$\text{Joined: } 001011101000_2$$  
$$\text{Dropping leading zeros: } \boxed{1011101000_2}$$

---

### 4. Two-step shortcut: Convert $623_8$ to hexadecimal through binary

**Step 1: Convert each octal digit to a 3-bit binary pattern**
* $6_8 = 110_2$
* $2_8 = 010_2$
* $3_8 = 011_2$

$$\text{Joined Binary: } 110010011_2$$

**Step 2: Regroup into 4-bit groups from right to left (pad left with zeros)**
$$0001 \quad 1001 \quad 0011$$

* **Left group ($0001_2$):** $1$
* **Middle group ($1001_2$):** $8 + 0 + 0 + 1 = 9$
* **Right group ($0011_2$):** $0 + 0 + 2 + 1 = 3$

$$\text{Final Answer: } \boxed{193_{16}}$$

---

## STATION 4

### 1. IPv4 Address Conversion

Convert each octet of the IPv4 address **10.18.44.244** to an 8-bit binary number:

* **10:** $00001010_2$
* **18:** $00010010_2$
* **44:** $00101100_2$
* **244:** $11110100_2$

$$\text{Full Binary IP Address: } \boxed{00001010.00010010.00101100.11110100}$$

---

### 2. Web Colors (Hexadecimal $\leftrightarrow$ RGB)

#### **Decode Hex Color:** `#DFEADD`
* **Red (DF):** $13 \times 16 + 15 = 208 + 15 = 223$
* **Green (EA):** $14 \times 16 + 10 = 224 + 10 = 234$
* **Blue (DD):** $13 \times 16 + 13 = 208 + 13 = 221$

$$\text{RGB Value: } \boxed{\text{rgb}(223, 234, 221)}$$

#### **Encode RGB Color:** `rgb(142, 91, 237)`
* **Red (142):** $142 \div 16 = 8 \text{ R } 14 (\text{E}) \longrightarrow 8\text{E}$
* **Green (91):** $91 \div 16 = 5 \text{ R } 11 (\text{B}) \longrightarrow 5\text{B}$
* **Blue (237):** $237 \div 16 = 14 (\text{E}) \text{ R } 13 (\text{D}) \longrightarrow \text{ED}$

$$\text{Hex Color Code: } \boxed{\#8\text{E}5\text{BED}}$$

---

### 3. Linux File Permissions

The command `chmod 600 report.txt` sets permissions using octal digits:
Each digit maps to a 3-bit binary representation: $\text{r (read)} = 4, \text{w (write)} = 2, \text{x (execute)} = 1$.

* **Owner (6):** Binary $110_2 \longrightarrow \text{Read} = \text{Yes}, \text{Write} = \text{Yes}, \text{Execute} = \text{No} \longrightarrow \text{rw-}$
* **Group (0):** Binary $000_2 \longrightarrow \text{Read} = \text{No}, \text{Write} = \text{No}, \text{Execute} = \text{No} \longrightarrow \text{---}$
* **Others (0):** Binary $000_2 \longrightarrow \text{Read} = \text{No}, \text{Write} = \text{No}, \text{Execute} = \text{No} \longrightarrow \text{---}$

$$\text{Full Permission String: } \boxed{\text{rw-------}}$$

---

### 4. Storage Limits (Unsigned 7-bit Field)

* **How many different values can it store?**  
  $$2^7 = \boxed{128 \text{ values}}$$

* **Largest value in decimal:**  
  $$2^7 - 1 = \boxed{127}$$

* **Largest value in binary:**  
  $$\boxed{1111111_2}$$

* **Largest value in hexadecimal:**  
  $$0111_2 \ (7) \quad 1111_2 \ (\text{F}) \longrightarrow \boxed{7\text{F}_{16}}$$

---

## STATION 5

### 1. Conversions for $N = 302$

#### **Binary (Base 2):**
* $302 \div 2 = 151 \quad \text{Remainder } 0$
* $151 \div 2 = 75 \quad \text{Remainder } 1$
* $75 \div 2 = 37 \quad \text{Remainder } 1$
* $37 \div 2 = 18 \quad \text{Remainder } 1$
* $18 \div 2 = 9 \quad \text{Remainder } 0$
* $9 \div 2 = 4 \quad \text{Remainder } 1$
* $4 \div 2 = 2 \quad \text{Remainder } 0$
* $2 \div 2 = 1 \quad \text{Remainder } 0$
* $1 \div 2 = 0 \quad \text{Remainder } 1$

$$\text{Binary: } \boxed{100101110_2}$$

#### **Octal (Base 8):**
* $302 \div 8 = 37 \quad \text{Remainder } 6$
* $37 \div 8 = 4 \quad \text{Remainder } 5$
* $4 \div 8 = 0 \quad \text{Remainder } 4$

$$\text{Octal: } \boxed{456_8}$$

#### **Hexadecimal (Base 16):**
* $302 \div 16 = 18 \quad \text{Remainder } 14 \ (\text{E})$
* $18 \div 16 = 1 \quad \text{Remainder } 2$
* $1 \div 16 = 0 \quad \text{Remainder } 1$

$$\text{Hexadecimal: } \boxed{12\text{E}_{16}}$$

---

### 2. Error Analysis

> **Scenario:** A classmate got the answer wrong because they wrote down the remainders in the wrong direction. They read them from top to bottom instead of bottom to top (LSB to MSB). Doing it upside down gave them $011101_2$, which is actually $29$ in decimal.
>
> **Correction:** The correct answer for $46_{10}$ in binary (read from bottom to top) is $\boxed{101110_2}$.