

# Introduction
Cryptography is associated with the process of converting ordinary plain text into unintelligible text and vice-versa. It is a method of storing and transmitting data in a particular form so that only those for whom it is intended can read and process it. Cryptography not only protects data from theft or alteration, but can also be used for user authentication.
Cryptography represent all the process used to insure the Confidentiality, the Authenticity and the Integrity of information. Warning : encryption != encoding ! When you encrypt data, you make sure that is only understandable by your targeted correspondants. When you encode a data, you transform it to another form to facilitate its use. For example, the base64 encoding is used in a lot of web applications (because it represents data with ascii characters only), but it is meant to be secure : anyone who has access to base64 data can decode it !

Some words you should know :

-   plaintext : unencrypted data
-   cipher : generic name for encryption algorithm
-   ciphertext : output of a cipher
# Challenges
## Caesar
Caesar cipher is one of the simplest encryption techniques. It is a type of substitution cipher in which each letter in the secret message is 'shifted' a certain number of places down the alphabet.

**For example with a shift of 4:**

> Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
> Secret message: REBLOCHON
> Cipher message: VIFPSGLSR

But you can also shuffle the alphabet to create a more complex pattern and even remove letters so your alphabet will not be 26 letters long. 

**For example with still a shift of 4 but a shuffle alphabet:**

> Alphabet: ABCDEFLSPZWTXIURNVQ
> Secret message: REBLOCHON
> Cipher message: APFWOLHOB

Now that you know how Caesar cipher works, it's time for you to start your first challenge:
		
 ***Can you please help me ? I am Alexander the Great and I need your help to decrypt a letter from Caesar that one of my spy got. 
 To do this write a python script that takes a cipher message and display all the possible shift. Your script should avoid to touch a character that are not in the alphabet and ignore the case of letters. Here is the letter:***
 
	 HGU{Lgmlw_ds_Ysmdw_wkl_guumhéw_hsj_dwk_Jgesafk._Lgmlw_?_Fgf_!_Mf_Naddsyw_hwmhdé_v’Ajjévmulatdwk_Ysmdgak_jékaklw_wfugjw_wl_lgmbgmjk_à_d’wfnszakkwmj.}
	
## Guess
Can you find what format this string is and break it ?

`7ecc19e1a0be36ba2c6f05d06b5d3058`

## eXORcisme
Every documents, images, sounds … can be stored in a file. A file contains data which must be used to render its content. The data organisation in a file is defined by its file format specifications (pdf, jpg, png, wav, zip …).

Almost all the main file formats have some structural similarities :

-   they start with a header describing the file : the size of its content, the targeted environments etc.
-   the content which can be organised in various ways
-   sometimes a end pattern, used to know where the parsers should stop

For example this is the format for JPEG:
![](https://ih0.redbubble.net/image.1889940775.6973/flat,1000x1000,075,f.u1.jpg)

The pictures in `eXORcism.zip` has been inadvertently encrypted. We are counting on you to decrypt them.
## Baby RSA
My grandpa used to be a cryptograph, for his 64 birthday his old colleague sent him this file (`rsa.txt`) saying he should give it to me in order to introduce me to cryptography. Help me solving it and I will pay you a lemonade.
## Jacques au secours !
One of our VIP clients, who wishes to remain anonymous, has apparently been hacked and all their important documents are now corrupted.
Can you help us recover the files? We found a strange piece of software that might have caused all of this. 

The piece of software is in `jacques.zip`.
