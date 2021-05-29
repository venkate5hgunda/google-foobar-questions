# TO COMPUTE THE DICTIONARY, BUT HARDCODING IT FROM THE SOLUTION I GOT
# sentence="The quick brown fox jumps over the lazy dog"
# output="000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
# dictionary={"#": "000001"} # For capitalization check
# sI=0
# for i in range(0,int(len(output)/6)):
#     # print(sentence[sI],":",output[6*i:6*(i+1)][0:6])
#     if(output[6*i:6*(i+1)][0:6]!=dictionary["#"]):
#         dictionary[sentence[sI].lower()]=output[6*i:6*(i+1)][0:6]
#         sI=sI+1
# for item in sorted (dictionary):
#     print(item,":",dictionary[item])

# def solution(s):
#     dictionary={
#         " " : "000000",
#         "#" : "000001",
#         "a" : "100000",
#         "b" : "110000",
#         "c" : "100100",
#         "d" : "100110",
#         "e" : "100010",
#         "f" : "110100",
#         "g" : "110110",
#         "i" : "010100",
#         "j" : "010110",
#         "k" : "101000",
#         "l" : "111000",
#         "m" : "101100",
#         "n" : "101110",
#         "o" : "101010",
#         "p" : "111100",
#         "q" : "111110",
#         "r" : "111010",
#         "s" : "011100",
#         "t" : "011110",
#         "u" : "101001",
#         "v" : "111001",
#         "w" : "010111",
#         "x" : "101101",
#         "y" : "101111",
#         "z" : "101011"
#     }
#     sBraille=""
#     for c in s:
#         if(c.isupper()):
#             sBraille+=dictionary["#"]
#         sBraille+=dictionary[c.lower()]
#     print(sBraille)

dictionary={
    " " : "000000",
    "#" : "000001",
    "a" : "100000",
    "b" : "110000",
    "c" : "100100",
    "d" : "100110",
    "e" : "100010",
    "f" : "110100",
    "g" : "110110",
    "h" : "110010",
    "i" : "010100",
    "j" : "010110",
    "k" : "101000",
    "l" : "111000",
    "m" : "101100",
    "n" : "101110",
    "o" : "101010",
    "p" : "111100",
    "q" : "111110",
    "r" : "111010",
    "s" : "011100",
    "t" : "011110",
    "u" : "101001",
    "v" : "111001",
    "w" : "010111",
    "x" : "101101",
    "y" : "101111",
    "z" : "101011"
}
s="The quick brown fox jumps over the lazy dog"
sBraille=""
for c in s:
    if(c.isupper()):
        sBraille+=dictionary["#"]
    sBraille+=dictionary[c.lower()]
print(sBraille)
