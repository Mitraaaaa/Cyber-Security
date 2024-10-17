## Project Description

This code is designed to read an encrypted message from a file, estimate the key length used in a Vigenere cipher, determine the key, and then decrypt the message using the Vigenere decryption algorithm. The decryption process includes calculating the index of coincidence for different substrings and applying frequency analysis. The program prints the estimated key length, the recovered key, and the decrypted message.

## Note on Ciphertext:
Since this type of attack relies on letter frequency, the ciphertext must be long enough to allow for accurate key length estimation and key recovery using English letter frequency. Short ciphertexts may result in incorrect key guesses. Therefore, a dataset named `ciphertext.txt` from the internet is used, providing sufficient letter frequency for more accurate results. The dataset is included with this project.
