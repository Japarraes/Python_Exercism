def fail_safe(temperature, neutrons_produced_per_second, threshold):
    
    if (temperature * neutrons_produced_per_second) < (0.9 * threshold):
        return "LOW"
        
    min = threshold - (threshold * 0.1)
    max = threshold + (threshold * 0.1)
    if (temperature * neutrons_produced_per_second) >= min and (temperature * neutrons_produced_per_second) <= max:
        return "NORMAL"
    else:
        return "DANGER"

print(fail_safe(10,399,10000))# LOW
print(fail_safe(10,300,10000))# LOW
print(fail_safe(10,1,10000)) # )LOW
print(fail_safe(10,0,10000)) # )LOW
print(fail_safe(10,899,10000))# LOW
print(fail_safe(10,700,10000))# LOW
print(fail_safe(10,400,10000))# LOW
print(fail_safe(10,901,10000))# NORMAL
print(fail_safe(10,1000,10000)) # NORMAL
print(fail_safe(10,1099,10000)) # NORMAL
print(fail_safe(10,1101,10000)) # DANGER
print(fail_safe(10,1200,10000)) # DANGER