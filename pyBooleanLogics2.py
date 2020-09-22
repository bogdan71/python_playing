a, b, c, d = True, True, True, False

if b and not d and a and not b:
    if b or a:
        print('42')
    elif d and c:
        print('yes')
    print('yes')
elif d and c or b:
    if b and not d or d:
        print('python')
    print('yes')
else:
    print('42')

    Solution
python
yes

Explanation
Boolean logic is a fundamental skill for any programmer. You need to have a solid understanding to be able to grasp the meaning of code quickly—and write your own bug-free code.

Oftentimes, you’ll find that the source of bugs in your code is because of flaws in your logic. So improving your ability to reason logically will improve your overall coding skill and will save you hours of painful debugging.

Boolean logic is the science of formulating and combining logical statements.

Definition: A logical statement is a statement that evaluates to a Boolean value True or False.

You can create logical statements recursively using the four Python operators and, or, not, and the bracket operator ( ).

The simplest logical statement would be "A=True" or "A=False". Now, you can create more complex logical statements using the Python operators:

- (A). The logical statement (A) evaluates to True if the statement A is already True. Usually, you’ll use the bracket operator to reorder the precedence relationship. This is called the bracket (or parenthesis) operator.
- not A. The logical statement not A evaluates to True if statement A evaluates to False. This is called the negation operator.
- A and B. The logical statement "A and B" evaluates to True if both statements "A" and "B" are already True. If only one of them is False, the statement "A and B" evaluates to False, too. This is called the logical AND operator.
- A or B. The logical statement "A or B" evaluates to True if at least one statement "A" or "B" is already True. Only if both of them are False, the statement "A or B" evaluates to False. This is called the logical OR operator.