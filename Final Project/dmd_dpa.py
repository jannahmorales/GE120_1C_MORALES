from math import cos, sin, radians, sqrt
lines = [15,90,15,180,15,270,15,360]


x = list(map(str, lines))
x = " ".join(x)
x = x.replace('5', '5*')
y = x.split("*")
res = []
for i in y:
    i = i.strip
    i = i.split
    b = []
    for j in i:
        b.append(int(j))
    res.append(b)


latdeps = []

for line in lines:
    distance = lines.split(":")[0]
    azimuth = lines.split(":")[1]
    dep = -distance*sin(azimuth)
    lat = -distance*cos(azimuth)
    latdeps.append = (dep,lat)

    dmds = []
    dpas = []
    dpa_total = 0

    for i in range (len(lines)):
        if i == 0:
            dmd = latdeps [0][0]
        else:
            dmd = latdeps [i][0] + dmd [i-1] + latdeps[i-1][0]
        dmds.append(dmd)
        
        dpa = dmd * latdeps[i][1]
        dpa_total += dpa
        
        dpa.append(dpa)

        area = (dpa_total)*(0.5)

print(area)
