def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

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

                    # Modify this if statement to check if the route is valid
                    if(True):
                        # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

main()

