# Introduction
Steganography is the art of hiding the fact that you are hiding something . Basically this means that all the process of hiding data in a file (image, sound, pdf…) is steganography. In this workshop, we are going to learn some basic techniques to hide data ad reverse them to retrieve it.
# Useful tools

# Challenges
## Spectre Audio
## PDF
## Filter pictures
## LSB
How to hide data in an image without using the filter technique and without concatenation ? With the widely used LSB technique, you can hide data in the image bits. LSB stands for Least Significant Bit which is the Bit which has the less importance on the final appearance of the image.

![LSB](https://pwnh4.com/lsb.png)

This technique consists of encoding the data to hide to base64 and wrote, bit per bit, to the byte describing the image content.

The disadvantage is that you can detect the use of this technique if you open the image at high contrast and check the pixel color : if it’s not as uniform as it appeared to be, some content must be stored with the LSB technique.
## Terrorist Attack
