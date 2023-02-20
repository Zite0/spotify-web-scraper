import scrape
from introcs import assert_equals

# Test remove_dups

lst1 = ['a','b','c','d','a']
lst2 = ['a','b','c','d']
assert_equals(lst2,scrape.remove_dups(lst1))

lst1 = ['b','b','b','b']
lst2 = ['b']
assert_equals(lst2,scrape.remove_dups(lst1))

lst1 = ['aab','ttt','aab','aab']
lst2 = ['aab','ttt']
assert_equals(lst2,scrape.remove_dups(lst1))

lst1 = [1,2,3,4,44,44]
lst2 = [1,2,3,4,44]
assert_equals(lst2,scrape.remove_dups(lst1))

lst1 = [1,1,1,1]
lst2 = [1]
assert_equals(lst2,scrape.remove_dups(lst1))

scrape.albums('https://open.spotify.com/artist/7Ln80lUS6He07XvHI8qqHH')
print(scrape.songs())