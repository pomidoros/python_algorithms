from lists import release_list as tl
new = tl.List()
new.add_nodes(*[1, 2, 34])
new.delete_node(2)
print(new)