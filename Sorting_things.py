### Method 1 ==> ordonner un string  avec ''.join + sorted
# ==> avec sorted(iterable) 
# crée une liste ordonnée
# +
# ==> ''.join(sorted(iterable))
# recrée un string 


letters = 'zyx'
new_string = ''.join(sorted(letters))
#                    <-------------->
#                        |--> make alist from any string, tuple
print(new_string)
# xyz

# string
print(''.join(sorted("letters")))
# eelrstt

# dictionnary
print(''.join(sorted({"z":24,"y":23,"x":22,"a":1})))
# axyz

# set
print(''.join(sorted({"z","y","x","a"})))
# axyz

# tuple
print(''.join(sorted(("z","y","x","a"))))
# axyz

# list
print(''.join(sorted(["z","y","x","a"])))
# axyz



### Method 2 ==> faire une list à partir d'un iterable + .sort() puis ''.join() 
# make a list form a string, sort it then making a string with .join()
tmp = list(letters)
tmp.sort()
new_string = ''.join(tmp)

data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8]
 
def find_high_low(nums):
    nums.sort()
    print(nums)                        
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return nums[-1], nums[0]
    
high, low = find_high_low(data)
 
print(
    ('The highest number is {} ' +
     'and the lowest number is {}.').format(high, low)
)
# The highest number is 10 and the lowest number is 1.