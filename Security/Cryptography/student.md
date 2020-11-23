# Introduction

# Useful tools

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
	


## eXORcisme
Every documents, images, sounds … can be stored in a file. A file contains data which must be used to render its content. The data organisation in a file is defined by its file format specifications (pdf, jpg, png, wav, zip …).

Almost all the main file formats have some structural similarities :

-   they start with a header describing the file : the size of its content, the targeted environments etc.
-   the content which can be organised in various ways
-   sometimes a end pattern, used to know where the parsers should stop

## RSA Sage
RSA keys need to conform to certain mathematical properties in order to be secure. If the key is not generated carefully it can have vulnerabilities which may totally compromise the encryption algorithm. Sometimes this can be determined from the public key alone. This article describes vulnerabilities that can be tested when in possession of a RSA public key.

If the RSA key is too short, the modulus can be factored by just using brute force. A 256-bit modulus can be factored in a couple of minutes. A 512-bit modulus takes several weeks on modern consumer hardware. Factoring 1024-bit keys is definitely not possible in a reasonable time with reasonable means, but may be possible for well equipped attackers. 2048-bit is secure against brute force factoring.

But actually with Sagemath (a mathematical open-source software) we can do a ROCA Attack on a 512-bit key and break it in only minutes.
## AES
