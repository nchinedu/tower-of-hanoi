def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def record_state():
        # Append a copy of the current state of rods
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move_disks(num, source, target, auxiliary):
        if num == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()
        else:
            move_disks(num - 1, source, auxiliary, target)
            move_disks(1, source, target, auxiliary)
            move_disks(num - 1, auxiliary, target, source)

    record_state()
    move_disks(n, 0, 2, 1)
    return "\n".join(moves)

