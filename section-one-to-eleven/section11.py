# Modifying Global Scope

enemies = 2


def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 4


enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")


# enemies = "Skeleton"


# def increase_enemies():
#     enemies = "Zombie"
#     print(f"Enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"Enemies outside function: {enemies}")


enemies = 2


# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"Enemies outside function: {enemies}")