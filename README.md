# `Info-amount`

![This is an image](https://img.shields.io/badge/Python-100%25-orange)
![This is an image](https://img.shields.io/badge/version-0.5-lightblue)

Investigate probabilistic parameters of the Ukrainian language to estimate the amount of text information. Investigate the impact of various information encoding methods on its quantity

## Theory

**The informativeness of the text** is the ability of the text to be the carrier of a complete message, to convey information. Informativeness as an important property of the text characterizes the amount of information contained in it, its importance and novelty. The essence of this concept appears differently in the texts, because it depends on the type of information used by the author of the message.
Types of information (according to I.R. Halperin):

  **·** Content-factual (what we see);

  **·** Content-conceptual (reflects the author's attitude);

  **·** Content-subtextual

The alphabetical approach to measuring information allows you to determine the amount of information contained in the text, it is an objective method, that is, it does not depend on the subject (person) who perceives the text. The set of symbols used in writing text is called the alphabet. The total number of characters in the alphabet is called the power (size) of the alphabet. If we assume that all characters of the alphabet occur in the text with the same frequency, then the amount of information that each character carries is calculated by the formula:<p align="center">$l = log_2 N$</p>
Where **N** is the strength of the alphabet.

So, in the 2-character alphabet, each character "*weights*" 1 bit; in the 4-character alphabet, each character carries 2 bits of information; in the 8th character - 3 bits, etc. One character from the alphabet of power 256 ( ) carries 8 bits of information (1 byte) in the text. An alphabet of 256 characters is used to display texts in a computer.


The relative frequency of occurrence of a symbol is the probability of occurrence of a certain symbol in a certain place of the text, that is, the ratio of the number of occurrences of the symbol in the text to the total number of symbols.
Information entropy is the average rate at which a stochastic data source produces information. The measure of entropy information is the negative logarithm of the probability mass function:

<p align="center">$S = - \Sigma_{i} {P_i l n P_i} $</p>

Thus, when a data source has a less probable value (eg, when a low-probability event occurs), that event carries more information than when a data source has a more probable value. The amount of information transmitted by each generation event thus determined becomes a random variable whose mathematical expectation is the information entropy.
### The average entropy of the non-probable alphabet:
<p align="center">$H = \sum^m_{i=1}{p_i log_2 \frac{1}{p_i} } = \sum^m_{i=1}{p_i log_2{p_i} } $</p>

where *m* - is the number of characters of the alphabet, *p* - is the probability of the character appearing


Entropy is measured in bits (as a representation of the number of possible options)

**The amount of information in the text** - is the average entropy of the original alphabet multiplied by the number of characters in the text

**Base64** - is a data encoding standard that uses only 64 ASCII characters. The symbols A-Z, a-z, 0-9 and two more symbols are used for coding, they differ depending on the implementation, the most common option is **+** and **/**. If the byte array is not a multiple of 3, then the array is supplemented with the symbol = so that the size of the transferred data becomes a multiple of 3.

## Base64 table from RFC 4648

| Index | Binary | Char | 
| :---         |     :---:      |          ---: |
| 0   | 000000     | A    |
| 1     | 000001       | B      |
| 2   | 000010     | C    |
| 3     | 000011       | D      |
| 4   | 000100     | E    |
| 5     | 000101       | F      |
| 6   | 000110     | G    |
| 7     | 000111       | H      |
| 8   | 001000     | I    |
| 9     | 001001       | J      |
| 10   | 001010     | K    |
| 11     | 001011       | L      |
| 12   | 001100     | M    |
| 13     | 001101       | N      |
| 14   | 001110     | O    |
| 15     | 001111       | P      |
| 16   | 010000     | Q    |
| 17     | 010001       | R      |
| 18   | 010010     | S    |
| 19     | 010011       | T      |
| 20   | 010100     | U    |
| 21     | 010101       | V      |
| 22   | 010110     | W    |
| 23     | 010111       | X      |
| 24   | 011000     | Y    |
| 25     | 011001       | Z      |
| 26   | 011010     | a    |
| 27     | 011011       | b      |
| 28   | 011100     | c    |
| 29    | 011101       | d      |
| 30   | 011110     | e    |
| 31     | 011111       | f      |
| 32   | 100000     | g    |
| 33     | 100001       | h      |
| 34   | 100010     | i    |
| 35     | 100011       | j      |
| 36   | 100100     | k    |
| 37     | 100101       | l      |
| 38   | 100110     | m    |
| 39     | 100111       | n      |
| 40   | 101000     | o    |
| 41     | 101001       | p      |
| 42   | 101010     | q    |
| 43     | 101011       | r      |
| 44   | 101100     | s    |
| 45     | 101101       | t      |
| 46   | 101110     | u    |
| 47     | 101111       | v      |
| 48   | 110000     | w    |
| 49     | 110001       | x      |
| 50   | 110010     | y    |
| 51     | 110011       | z      |
| 52   | 110100     | 0    |
| 53     | 110101       | 1      |
| 54     | 110110       | 2      |
| 55   | 110111     | 3    |
| 56     | 111000       | 4      |
| 57   | 111001     | 5    |
| 58     | 111010       | 6      |
| 59   | 111011     | 7    |
| 60     | 111100       | 8      |
| 61     | 111101       | 9      |
| 62   | 111110     | +    |
| 63     | 111111       | /      |

Base64 encoding algorithm:

1. Separation of the input stream of bytes into blocks of 3 bytes

2.  Division of 24 bits of each 3-byte block into 4 groups of 6 bits
 
3. Mapping each group of 6 bits to 1 symbol based on the encoding table
 
4. If the last 3-byte block contains only 1 byte of input data, fill 2 bytes with the symbol =, if the last 3-byte block contains only 2 bytes of input data, fill 1 byte with the symbol =.

![alt text](https://www.101computing.net/wp/wp-content/uploads/cryptography-base64-hexadecimal.png)

<p align="center">IMG: Text to base_64 and after base_16 encoding example</p>
<p align="center">(I'll do *cyrillic text* to binary and then to base_64 encoding)</p>