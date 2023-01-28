# `Info-amount`

![This is an image](https://img.shields.io/badge/Python-100%25-orange)
![This is an image](https://img.shields.io/badge/version-0.1-lightblue)

Investigate probabilistic parameters of the Ukrainian language to estimate the amount of text information. Investigate the impact of various information encoding methods on its quantity

## Theory

**The informativeness of the text** is the ability of the text to be the carrier of a complete message, to convey information. Informativeness as an important property of the text characterizes the amount of information contained in it, its importance and novelty. The essence of this concept appears differently in the texts, because it depends on the type of information used by the author of the message.
Types of information (according to I.R. Halperin):

  **·** Content-factual (what we see);

  **·** Content-conceptual (reflects the author's attitude);

  **·** Content-subtextual

The alphabetical approach to measuring information allows you to determine the amount of information contained in the text, it is an objective method, that is, it does not depend on the subject (person) who perceives the text. The set of symbols used in writing text is called the alphabet. The total number of characters in the alphabet is called the power (size) of the alphabet. If we assume that all characters of the alphabet occur in the text with the same frequency, then the amount of information that each character carries is calculated by the formula:<p align="center">$l = log_2 N$</p>
Where **N** is the strength of the alphabet.

So, in the 2-character alphabet, each character "weights" 1 bit; in the 4-character alphabet, each character carries 2 bits of information; in the 8th character - 3 bits, etc. One character from the alphabet of power 256 ( ) carries 8 bits of information (1 byte) in the text. An alphabet of 256 characters is used to display texts in a computer.
