# Lab Notes  
*Lab 07  
Sivert Log  
March 2025*  

### Extra Credit

The list of keys is simply a list of keys, any time a new key
is added it is appended to the list.
To keep track of which key is used, each encryption is stored in `encrypted_list`
with the index of the corresponding key. When assigning keys,
`enc_menu()` iterates through the key list according to the
last key used, and wraps back to the first key when the end
of the list is reached.  
It is currently commented out, but I added a 6th
menu item 'Uber Dumb(debug)' that calls `uber_dump()` which
shows each key, then each encrypted message with it's corresponding
key.
