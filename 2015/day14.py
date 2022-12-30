"""
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""

reindeer_dict = {
    "Comet": {"speed": 14, "fly": 10, "rest": 127},
    "Dancer": {"speed": 16, "fly": 11, "rest": 162},
}

time = 10
for t in range(time):
    for key, val in reindeer_dict.items():
        speed = val["speed"]
        fly_t = val["fly"]
        rest_t = val["rest"]
        print(f"{key}: {speed*fly_t}km travelled every {fly_t+rest_t}s ({rest_t}s rest).")

# {(distance * (periods + 1))*(t/fly_t)}km travelled in {t}s ({periods} periods completed, {modulo}s into next period).")

    # for k, v in reindeer_dict[key].items():
    #     total_time = 1000
    #     speed = reindeer_dict[key]["speed"]
    #     length = reindeer_dict[key]["length"]
    #     rest = reindeer_dict[key]["rest"]

    #     distance = speed * length
    #     period = length + rest

    #     periods = total_time // period
    #     modulo = total_time%period
