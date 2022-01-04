def bouncing_ball(h, bounce, window):
    x = 0
    b_height = h
    if h > 0 and (bounce > 0 and bounce < 1) and window < h:
        #First bounce
        x += 1
        b_height *= bounce
        #other bounces
        while b_height > window:
            x += 2
            b_height *= bounce
        return x
    else:
        return -1

#Test:
print(bouncing_ball(3,0.66,1.5))