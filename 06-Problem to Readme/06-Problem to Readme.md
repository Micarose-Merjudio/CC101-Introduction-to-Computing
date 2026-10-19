# SORSOGON STATE UNIVERSITY
### COLLEGE OF INFORMATION AND COMMUNICATIONS TECHNOLOGY
**Bulan Campus — Zone 8, Bulan, Sorsogon**

**Course:** CC 101 - Introduction to Computing  
**Activity Title:** "From Problem to README": Designing a Number-System Converter and Documenting It in Markdown  
**Name:** MICA ROSE D. MERJUDIO  
**Block:** BSCS 1-1  
**Computer Unit Used:** LAPTOP, HUAWEI  
**Date:** OCTOBER 16, 2026  
**Instructor:** Prof. John Mark Gabrentina  
**School Year:** 2026-2027  

---

## I. Objectives
At the end of this activity, you should be able to:
* Analyze a number-system conversion problem by identifying its inputs, processes, loop condition, and outputs.
* Write pseudocode using sequence, selection, and iteration.
* Draw flowcharts using standard symbols and check them by tracing and testing with sample data.
* Create a properly formatted `README.md` file in Markdown using Notepad, without an Internet connection.
* Upload the `README.md` to your CC 101 GitHub Computing Portfolio repository (take-home part).

---

## II. Materials Needed
* A computer running Windows 11 with Notepad (no network or Internet connection is needed in the laboratory)
* This worksheet, a pencil, and a ruler (or a flowchart template) for drawing flowcharts
* A USB flash drive, to bring your `README.md` home for uploading
* For Part G only (outside the laboratory): any device with Internet access and a free GitHub account
* Week 7 lecture notes, for reference on pseudocode, flowchart symbols, and Markdown syntax

---

## III. Background
Programmers do not start by typing code. They first analyze the problem, plan the solution as pseudocode and a flowchart, and check it by hand. In this activity, you will design a program that converts numbers between the decimal and binary number systems you learned in Week 5.

An algorithm can be written as pseudocode (English-like steps) or drawn as a flowchart (standard symbols connected by arrows). Good work is also documented. On GitHub, the standard way to introduce a project is a `README.md` file written in Markdown, a plain-text format that uses symbols such as `#`, `*`, and `-` for headings, emphasis, and lists. Because Markdown is plain text, you can write it in Notepad with no Internet connection and upload it to GitHub later.

---

## IV. Procedure

### Part A - Analyze the Problem (Problem 1)
**Problem 1: Decimal-to-Binary Converter.** Design a program that asks the user for a whole number in decimal (base 10) that is 0 or greater, converts it to binary (base 2), and displays the binary result.

*Worked example (13 in decimal):*
* $13 \div 2 = 6 \quad \text{r } 1$
* $6 \div 2 = 3 \quad \text{r } 0$
* $3 \div 2 = 1 \quad \text{r } 1$
* $1 \div 2 = 0 \quad \text{r } 1$

Reading the remainders from bottom to top gives $1101_2$.

1. Convert 13 and 25 to binary by hand using the method above, so you understand every step before writing the pseudocode.
2. Complete Table 1: list the input, the output, the processes (operations), the decision or loop condition, and the variables you will need.

### Part B - Write the Pseudocode
3. In Box 1, write the pseudocode for Problem 1. Use `START`, `INPUT`, `SET`, `WHILE ... DO ... ENDWHILE`, `IF ... THEN ... ELSE ... ENDIF`, `DISPLAY`, and `END`, and indent the steps inside the loop.

*Tip:* Use `MOD` for the remainder of a division ($13 \text{ MOD } 2 = 1$) and `DIV` for whole-number division ($13 \text{ DIV } 2 = 6$). Each new remainder must be placed at the left of the binary digits found so far, for example `SET binary = remainder + binary`. Also decide what your algorithm should display when the input is 0.

### Part C - Draw the Flowchart and Desk Check
4. In Figure 1, draw the flowchart for Problem 1 using the standard symbols: oval (start/end), parallelogram (input/output), rectangle (process), and diamond (decision). Show the loop with an arrow going back to the decision, and label every decision exit Yes or No.
5. Trace your pseudocode with the input 13 and fill in one row of Table 2 for each pass through the loop. The last column should end with 1101.
6. Test your pseudocode and flowchart with the five inputs in Table 3. First convert each number by hand, then follow your pseudocode or flowchart step by step. If the two results do not match, find and correct the error in your pseudocode and flowchart.

### Part D - Reverse Conversion (Problem 2)
**Problem 2: Binary-to-Decimal Converter.** Design a program that asks the user for a binary number (entered as digits 0 and 1, such as 1101) and displays its decimal value. Use the positional (place value) method: starting from the rightmost digit, multiply each digit by its place value ($1, 2, 4, 8, 16, \dots$) and add the products.

*Worked example (1101 in binary):*
$$
(1 \times 1) + (0 \times 2) + (1 \times 4) + (1 \times 8) = 1 + 0 + 4 + 8 = 13
$$

7. In Box 2, write the pseudocode. You can take the rightmost digit with `binary MOD 10` and remove it with `binary DIV 10`; the place value starts at 1 and doubles after each digit.
8. In Figure 2, draw its flowchart.
9. Test your pseudocode with the inputs in Table 4, comparing hand computation with the result of following your pseudocode.
10. *Optional / Bonus:* Extend Problem 1 so the user can choose the target base (2, 8, or 16). For base 16, remainders 10 to 15 must be displayed as the letters A to F. Write the extended pseudocode in the Bonus box.

### Part E - Create Your README.md Offline
11. Show file extensions in File Explorer.
12. Create the workspace folder structure: `cc101-portfolio/` containing `week07-algorithms/` and `images/`.
13. Open Notepad and type the project documentation using standard Markdown.
14. Save as `README.md` in UTF-8 encoding.
15. Verify via Command Prompt (`cmd`) and record `dir` and `type` outputs.

---

## V. Data and Findings

### Table 1. Problem Analysis for Problem 1 (Part A)

| Item | Your Answer |
| :--- | :--- |
| **Restated problem (your own words)** | Create a program that accepts a non-negative whole number in decimal (base 10) format from the user, converts that value into its binary (base 2) equivalent, and outputs the final binary result. |
| **Input** | Whole number in decimal (base 10) that is 0 or greater. |
| **Output** | The corresponding binary of the input number, displayed as a result. |
| **Processes (operations)** | Division by 2 to find quotients, modulo operation (or finding remainders) to extract binary digits (0 or 1), and string concatenation or accumulation to reverse/order the remainders correctly. |
| **Loop condition (when loop stops)** | The loop continues as long as the decimal number is greater than 0 (stops when the decimal number reaches 0). |
| **Variables needed** | `decimal_number`: Stores the user's input value.<br>`binary_string`: Stores or accumulates the resulting binary digits.<br>`R`: Holds the remainder of each division step.<br>`N`: Temporary working variable for the decimal number. |
| **13 and 25 in binary (computed by hand)** | **13 to Binary:**<br>$13 \div 2 = 6 \quad \text{remainder } 1$<br>$6 \div 2 = 3 \quad \text{remainder } 0$<br>$3 \div 2 = 1 \quad \text{remainder } 1$<br>$1 \div 2 = 0 \quad \text{remainder } 1$<br>**Answer:** $1101_2$<br><br>**25 to Binary:**<br>$25 \div 2 = 12 \quad \text{remainder } 1$<br>$12 \div 2 = 6 \quad \text{remainder } 0$<br>$6 \div 2 = 3 \quad \text{remainder } 0$<br>$3 \div 2 = 1 \quad \text{remainder } 1$<br>$1 \div 2 = 0 \quad \text{remainder } 1$<br>**Answer:** $11001_2$ |

---

### Box 1. Pseudocode for Problem 1 (Part B)

```text
START
    INPUT Decimal_number
    SET Binary_string = ""
    SET N = Decimal_number
    WHILE N > 0 DO
        SET R = N MOD 2
        SET Binary_string = String(R) + Binary_string
        SET N = N DIV 2
    ENDWHILE
    DISPLAY Binary_string
END
```

---

### Figure 1. Flowchart for Problem 1 (Part C)

```
       +------------------+
       |      Start       |
       +--------+---------+
                |
                v
       +------------------+
       | Input:           |
       | Decimal_number   |
       +--------+---------+
                |
                v
       +------------------+
       | Binary_string =""|
       | N = Decimal_num  |
       +--------+---------+
                |
                v
       +------------------+
  +--->|      N > 0?      |--- No/False ---> [ Display Binary_string ] ---> ( END )
  |    +--------+---------+
  |             |
  |          Yes/True
  |             |
  |             v
  |    +------------------+
  |    |  R = N % 2       |
  |    |  Binary_string = |
  |    |   String(R) +    |
  |    |   Binary_string  |
  |    +--------+---------+
  |             |
  |             v
  |    +------------------+
  |    |  N = N / 2       |
  |    +--------+---------+
  |             |
  +-------------+
```

---

### Table 2. Trace of Problem 1 with Input 13 (Part C)

| Pass | N (before) | N MOD 2 (remainder) | N DIV 2 (new N) | Binary (so far) |
| :---: | :---: | :---: | :---: | :---: |
| **1** | 13 | 1 | 6 | "1" |
| **2** | 6 | 0 | 3 | "01" |
| **3** | 3 | 1 | 1 | "101" |
| **4** | 1 | 1 | 0 | "1101" |
| **5** | *Loop stops here ($N = 0$)* | — | — | — |

**Value displayed at the end:** `1101`

---

### Table 3. Test Cases for Problem 1 (Part C)

| Case | Decimal Input | Binary (by hand) | Binary From Your Pseudocode | Match? (Y/N) |
| :---: | :---: | :---: | :---: | :---: |
| **1** | 0 | 0 | 0 | Y |
| **2** | 5 | 101 | 101 | Y |
| **3** | 13 | 1101 | 1101 | Y |
| **4** | 25 | 11001 | 11001 | Y |
| **5** | 255 | 11111111 | 11111111 | Y |

---

### Box 2. Pseudocode for Problem 2 (Part D)

```text
START
    INPUT binary_number
    SET decimal_value = 0
    SET place_value = 1
    WHILE binary_number > 0 DO
        SET digit = binary_number MOD 10
        SET decimal_value = decimal_value + (digit * place_value)
        SET binary_number = binary_number DIV 10
        SET place_value = place_value * 2
    ENDWHILE
    DISPLAY decimal_value
END
```

---

### Figure 2. Flowchart for Problem 2 (Part D)

```
       +------------------+
       |      START       |
       +--------+---------+
                |
                v
       +------------------+
       | Input:           |
       | binary_number    |
       +--------+---------+
                |
                v
       +------------------+
       | SET decimal_val=0|
       | SET place_val = 1|
       +--------+---------+
                |
                v
       +------------------+
  +--->| binary_number >0?|--- No/False ---> [ Display decimal_value ] ---> ( END )
  |    +--------+---------+
  |             |
  |          Yes/True
  |             |
  |             v
  |    +----------------------------------+
  |    | digit = binary_number MOD 10     |
  |    | decimal_value = decimal_value + |
  |    |   (digit * place_value)          |
  |    +----------------+-----------------+
  |                     |
  |                     v
  |    +----------------------------------+
  |    | binary_number = binary_number/10 |
  |    | place_value = place_value * 2    |
  |    +----------------+-----------------+
  |                     |
  +---------------------+
```

---

### Table 4. Test Cases for Problem 2 (Part D)

| Case | Binary Input | Decimal (by hand) | Decimal From Your Pseudocode | Match? (Y/N) |
| :---: | :---: | :--- | :---: | :---: |
| **1** | 1101 | $(1 \times 1) + (0 \times 2) + (1 \times 4) + (1 \times 8) = 1 + 0 + 4 + 8 = 13$ | 13 | Y |
| **2** | 101010 | $(0 \times 1) + (1 \times 2) + (0 \times 4) + (1 \times 8) + (0 \times 16) + (1 \times 32) = 2 + 8 + 32 = 42$ | 42 | Y |
| **3** | 11111111 | $1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 = 255$ | 255 | Y |
| **4** | 10000000 | $(0 \times 1) + \dots + (1 \times 128) = 128$ | 128 | Y |

---

### Bonus Box. Extended Pseudocode: Decimal to Base 2, 8, or 16 (Optional)

```text
START
    INPUT decimal_number
    INPUT target_base
    IF decimal_number == 0 THEN
        SET result = "0"
    ELSE
        SET result = ""
        WHILE decimal_number > 0 DO
            SET remainder = decimal_number MOD target_base
            IF target_base == 16 THEN
                IF remainder == 10 THEN
                    SET rem_char = "A"
                ELSE IF remainder == 11 THEN
                    SET rem_char = "B"
                ELSE IF remainder == 12 THEN
                    SET rem_char = "C"
                ELSE IF remainder == 13 THEN
                    SET rem_char = "D"
                ELSE IF remainder == 14 THEN
                    SET rem_char = "E"
                ELSE IF remainder == 15 THEN
                    SET rem_char = "F"
                ELSE
                    SET rem_char = String(remainder)
                ENDIF
            ELSE
                SET rem_char = String(remainder)
            ENDIF
            SET result = rem_char + result
            SET decimal_number = decimal_number DIV target_base
        ENDWHILE
    ENDIF
    DISPLAY result
END
```

---

### Table 5. README.md File Check (Part E)

| Item | Your Findings |
| :--- | :--- |
| **Full folder path of cc101-portfolio** | `C:\Users\merju\OneDrive\Documents\cc101-portfolio` |
| **File name shown in File Explorer** | `README.md` |
| **Type shown in File Explorer (Details view)** | Markdown File or MD File |
| **Size of README.md shown by dir (bytes)** | 1,221 bytes |
| **Console Verification Log** | ```text<br>Directory of C:\Users\merju\OneDrive\Documents\cc101-portfolio<br>16/10/2026  02:09 PM    <DIR>          .<br>16/10/2026  02:09 PM    <DIR>          ..<br>16/10/2026  02:07 PM    <DIR>          images<br>16/10/2026  02:09 PM             1,221 README.md<br>15/10/2026  09:18 PM    <DIR>          week07-algorithms<br>               1 File(s)          1,221 bytes<br>``` |
| **Does type README.md show your Markdown text? (Y/N)** | Y |
| **Notepad formatted view available? (Y/N)** | Y |
| **Elements that appeared formatted in Notepad** | Headings, bold text, and lists (tables, images, and code blocks remain plain text) |

---

### Table 6. Peer Review Checklist (Part F)

**Reviewer's name:** ANGEL LYRA ESCANDOR  
**Owner of the README:** MICA ROSE D. MERJUDIO  

| Element | Markdown Used | Present and Correct? (Y/N) |
| :--- | :--- | :---: |
| **Level-1 heading** | `#` | Y |
| **Level-2 headings** | `##` | Y |
| **Paragraph** | Text with a blank line before and after | Y |
| **Bold and italic text** | `**bold**` `*italic*` | Y |
| **Bulleted list** | `- item` | Y |
| **Numbered list** | `1. item` | Y |
| **Table** | `\| header separator` | Y |
| **Link** | `[text](url)` | Y |
| **Image** | `![alt](path)` | Y |
| **Code block** | Lines between two lines of three backticks | Y |
| **Horizontal rule** | `---` | Y |
| **File saved as README.md (not .txt)** | `README.md` | Y |

---

### Table 7. GitHub Submission (Part G, Take-Home)

| Item | Your Answer |
| :--- | :--- |
| **GitHub username** | Micarose-Merjudio |
| **Repository URL** | `https://github.com/Micarose-Merjudio/cc101-portfolio` |
| **Date uploaded (YYYY-MM-DD)** | 2026-10-16 |
| **Does the README display formatted on GitHub? (Y/N)** | Y |
| **Elements that did not display as expected, and why** | None |

---

## VI. Realization (Reflection)

1. **Which was easier for you to create, the pseudocode or the flowchart? Why?**  
   Writing the pseudocode was easier for me because its structured text format allowed me to map out the control flow, loop conditions, and mathematical operations directly using standard programming constructs like `WHILE`, `MOD`, and `DIV`. In contrast, creating the flowchart required extra effort to lay out symbols neatly, align arrows properly, and ensure every decision branch was explicitly labeled with Yes or No. Overall, pseudocode made it quicker to focus on solving the logic before worrying about visual structure.

2. **Did tracing and testing reveal any errors in your pseudocode or flowcharts? Describe what you found and how you corrected it.**  
   Yes, tracing the conversion process through the desk check table revealed an edge case when handling an input of zero. Initially, the standard `WHILE (N > 0)` loop condition skipped execution completely for 0, which would leave the binary result completely empty instead of returning `"0"`. I corrected this by adding an explicit `IF decimal_number == 0 THEN` check before entering the loop to ensure zero outputs correctly.

3. **How is writing a README in Markdown different from typing a document in Microsoft Word?**  
   Writing a README in Markdown relies on plain text symbols—such as `#` for headings, `**` for bold text, and pipe characters for tables—to define formatting rather than relying on a visual graphical toolbar. Microsoft Word uses a What-You-See-Is-What-You-Get (WYSIWYG) interface, whereas Markdown keeps the underlying content lightweight and separate from rendered styling. This makes Markdown ideal for code repositories since it displays consistently across development environments like GitHub without heavy formatting files.

4. **How can a GitHub portfolio help you as a future computing professional?**  
   A GitHub portfolio serves as tangible, public proof of my technical competence, showcasing my programming projects, problem-solving skills, and documentation capabilities to future employers. It demonstrates my proficiency with version control, collaborative workflows, and structured project management early in my academic journey. Having a clean and updated repository allows recruiters and peers to review my real-world code and development history directly.

---

## VII. Scoring Guide

| Criteria | Description | Points |
| :--- | :--- | :---: |
| **Problem Analysis & Pseudocode** | Table 1 is complete; the pseudocode for both conversions is correct (correct use of `MOD`, `DIV`, and the loop), uses proper keywords, and is indented. | 25 |
| **Flowcharts & Testing** | Both flowcharts use the correct symbols with labeled decisions and a clear loop; the trace (Table 2) and test cases (Tables 3 and 4) are correct. | 25 |
| **README.md & GitHub Upload** | The file is saved correctly as `README.md`, uses all required Markdown elements, and passes the peer review in Table 6. The README is uploaded to a public `cc101-portfolio` repository and the URL is submitted (Table 7). | 35 |
| **Realization / Reflection** | Answers are thoughtful, specific to the student's own work, and well written. | 10 |
| **Neatness & Timeliness** | Worksheet is legible/well-formatted and submitted on time. | 5 |
| **Total** | | **100** |