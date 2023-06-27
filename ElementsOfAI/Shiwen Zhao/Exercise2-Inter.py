def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # https://sea-distances.org/
    # nautical miles converted to km

    D = [
            [0,8943,8019,3652,10545],
            [8943,0,2619,6317,2078],
            [8019,2619,0,5836,4939],
            [3652,6317,5836,0,7825],
            [10545,2078,4939,7825,0]
        ]

    # https://timeforchange.org/co2-emissions-shipping-goods
    # assume 20g per km per metric ton (of pineapples)


    co2 = 0.020
    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            if port2 == port3:
                continue
            for port4 in range(1, 5):
                if port2 == port4 or port3 == port4:
                    continue
                for port5 in range(1, 5):
                    if port2 == port5 or port3 == port5 or port4 == port5:
                        continue
                    route = [port1, port2, port3, port4, port5]
                    distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
                    emissions = distance * co2
                    print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)
    
main()