from read import read
import os
import re

def parse_input(filename):
    input = read.from_file(filename)
    regex = "Valve (\w+) has flow rate=(\d+); (?:tunnels lead|tunnel leads) to (?:valve|valves) (.+)"
    data = {}
    for line in input:
        match = re.search(regex, line)
        if match:
            data[match.group(1)] = {'flow_rate': int(match.group(2)), 'tunnels': match.group(3).split(", ")}
    return data

def part1(filename):
    data = parse_input(filename)
    #[{opened_valves: [], current_valve, pressure_per_minute, total_pressure},]
    to_explore = [{"opened_valves": [], "current_valve": "AA", "pressure_per_minute": 0, "total_pressure": 0}]
    for m in range(1, 31):
        print("minute", m)
        new_history = []
        for path in to_explore:
            current_valve = path["current_valve"]
            # increase total pressure
            total_pressure = path["total_pressure"] + path["pressure_per_minute"]
            # open valve
            if path["current_valve"] not in path["opened_valves"]:
                opened_valves = path["opened_valves"][:]
                opened_valves.append(path["current_valve"])
                new_history.append({"opened_valves": opened_valves, "current_valve": current_valve, "pressure_per_minute": path["pressure_per_minute"] + data[current_valve]["flow_rate"], "total_pressure": total_pressure})
            # go to new tunnel
            for tunnel in data[current_valve]["tunnels"]:
                opened_valves = path["opened_valves"][:]
                similar_paths = [p for p in new_history if p["current_valve"] == tunnel]
                new_history.append({"opened_valves": opened_valves, "current_valve": tunnel, "pressure_per_minute": path["pressure_per_minute"], "total_pressure": total_pressure})
        to_explore = new_history
        # print(history)
    return max([path["total_pressure"] for path in to_explore])
                
            


#print(part2("{}/input.txt".format(os.path.dirname(__file__)), 4000000))