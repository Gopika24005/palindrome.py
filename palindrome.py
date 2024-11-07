from collections import Counter
def palindromepermutation(s):
    s=s.replace(" ","").lower()
    count = Counter(s) 
    odd_count = sum(1 for freq in count.values() if freq % 2 !=0)
    return odd_count <= 1
input_string="taco cat"
output=palindromepermutation(input_string)
print(output)
