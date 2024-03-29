# Shared-Secret-Cryptography
A Cryptography algorithm based on Randomness, created so than it's unbreakable by any means other than brute force. _Securing messages_ delivered via _insecure_ channels.

# How Does it work?
We have 2 entities: The __Sender__ and the __Reciever__, each of them gets handed a book with bit keys. __Only 2 copies of this book exist__ and only our 2 entities have access to it. For every message delivered, they choose the corresponding key in order to decode the message. For the $N^{th}$ message they choose the $N^{th}$ key from the book.

## __The Algorithm Step By Step:__
1. __Sender__ drafts a message.
2. They translate it into binary code _{0,1}_.
3. They apply the corresponding _key_ by using an __XOR Gate__ for each bit of message and key.
4. They translate the resulting bit sequence back to an alphabet string.
5. They send it to __Reciever__. 
6. The __Reciever__ translates the string into _binary code_.
7. They apply the same key using an __XOR__ Gate.
- Since __(A XOR B) XOR B = A__ they get the originally translated binary code produced in _Step 2._
8. They translate it back to an alphabet string and get the __original message__.
