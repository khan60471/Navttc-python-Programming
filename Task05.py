def calculate_pyramid_height(num_blocks):
    height = 0
    layer_blocks = 1

    while num_blocks >= layer_blocks:
        height += 1
        num_blocks -= layer_blocks
        layer_blocks += 1

    return height

# Test the code
num_blocks = int(input("Enter the number of blocks: "))
pyramid_height = calculate_pyramid_height(num_blocks)
print("The height of the pyramid is:", pyramid_height)