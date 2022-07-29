def solution(bridge_length, weight, truck_weights):
    bridge = [0 for i in range(bridge_length)]
    time = 0
    while bridge:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
            else:
                bridge.append(0)
    return time