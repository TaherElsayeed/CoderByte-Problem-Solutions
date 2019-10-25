# Mathmatical Proof for Pentagonal Numbers
### Index
- ***[About](#about)***
- ***[Question](#question)***
- ***[Proof](#proof)***

---
## About
This is the proof that I found when solving for the CoderByte question titled _Pentagonal Numbers_

---
## Question
_Have the function PentagonalNumber(num) read num which will be a positive integer and determine how many dots exist in a pentagonal shape around a center dot on the Nth iteration. For example, in the image below you can see that on the first iteration there is only a single dot, on the second iteration there are 6 dots, on the third there are 16 dots, and on the fourth there are 31 dots. Your program should return the number of dots that exist in the whole pentagon on the Nth iteration._

---
## Proof
Let Z be both a natural number that can be 1 to infinity and the sum of all dots that make up a pentagon. Let N be a natural number from 1 to infintiy.

The equation to calculate the number of dots that make up a pentagon as laid out in the question is as follows:

> _Z<sub>n</sub> = (N - 1) * 5 + Z<sub>n - 1</sub>_
