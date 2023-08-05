n , m = input().split()
n = int(n) * 100
m = int(m) * 100

Number_of_tiles_required = (n*m) / 1000

def Number_of_packages_required(Number_of_tile_required):
    if Number_of_tile_required % 10 != 0:
        return int((Number_of_tile_required // 10) + 1)
    else:
        return int(Number_of_tile_required // 10)

Number_of_package_required = Number_of_packages_required(Number_of_tiles_required)

print(Number_of_package_required)