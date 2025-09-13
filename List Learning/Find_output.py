# Find the output.

s = "Hello, everyone how are you"
print(s.split())
#Output: ['Hello,', 'everyone', 'how', 'are', 'you']


s = "Hello-everyone-how are you"
print(s.split("-"))
#Output:  ['Hello', 'everyone', 'how are you']


word = 'Suyash:Chaudhary:Noida'
print(word.split(':'))
#Output:  ['Suyash', 'Chaudhary', 'Noida']


t = "23456"
print(t.split())
#Output:  ['23456']


t = "2 3 4 5"
print(t.split())
#Output:   ['2', '3', '4', '5']