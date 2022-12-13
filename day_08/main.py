FILE = "input"

total_visible_trees = 0
content = []
with open(FILE) as in_file:
    for line in in_file:
        content.append(line.strip())

outside_trees = []
# Gets all trees that are bordering the forrest and will be visible
for i, trees in enumerate(content):
    if i == 0:
        for tree in trees:
            outside_trees.append(tree)
    if trees == content[-1]:
        for tree in trees:
            outside_trees.append(tree)
    if i != 0 and trees != content[-1]:
        outside_trees.append(trees[0])
        outside_trees.append(trees[-1])

inner_trees = []
# Check remaining inner trees
for i, trees in enumerate(content, 1):
    if trees != content[0] and trees != content[-1]:
        for j, tree in enumerate(trees):
            if j != 0 and j != len(trees) - 1:  # Don't check outer numbers already counted in border
                tree_counted = False
                count_trees_left = j
                while count_trees_left != 0:
                    if tree > trees[count_trees_left - 1] and count_trees_left == 1:
                        inner_trees.append(tree)
                        count_trees_left = 0
                        tree_counted = True
                    elif tree > trees[count_trees_left - 1]:
                        count_trees_left -= 1
                    elif tree <= trees[count_trees_left - 1]:
                        count_trees_left = 0

                count_trees_right = j
                while count_trees_right != len(trees) - 1 and not tree_counted:
                    if tree > trees[count_trees_right + 1] and count_trees_right + 1 == len(trees) - 1:
                        inner_trees.append(tree)
                        count_trees_right = len(trees) - 1
                        tree_counted = True
                    elif tree > trees[count_trees_right + 1]:
                        count_trees_right += 1
                    elif tree <= trees[count_trees_right + 1]:
                        count_trees_right = len(trees) - 1

                count_trees_up = i - 1
                while count_trees_up != 0 and not tree_counted:
                    if int(tree) > int(content[count_trees_up - 1][j]) and count_trees_up == 1:
                        inner_trees.append(tree)
                        count_trees_up = 0
                        tree_counted = True
                    elif int(tree) > int(content[count_trees_up - 1][j]):
                        count_trees_up -= 1
                    elif int(tree) <= int(content[count_trees_up - 1][j]):
                        count_trees_up = 0

                    count_trees_down = i - 1
                    while count_trees_down != len(content) - 1 and not tree_counted:
                        if int(tree) > int(content[count_trees_down + 1][j]) and count_trees_down + 1 == len(
                                content) - 1:
                            inner_trees.append(tree)
                            count_trees_down = len(content) - 1
                            tree_counted = True
                        elif int(tree) > int(content[count_trees_down + 1][j]):
                            count_trees_down += 1
                        elif int(tree) <= int(content[count_trees_down + 1][j]):
                            count_trees_down = len(content) - 1


print("Trees Visible:", len(outside_trees) + len(inner_trees))
