apr = 3908
apr_norm = apr / 100
initial_apr_per_day = apr_norm / 365
days_in_epoch = 7
crystal_per_epoch = [16, 12, 10, 8, 7, 6, 5, 5, 4, 4, 3, 3, 2, 2]


for num_epochs in [2,4,8,10,12]:
    print(f"num epochs {num_epochs}")
    #recompound once an day
    balance = 1
    curr_unlock = .05
    curr_apr_per_day = initial_apr_per_day
    locked_balance = 0
    for k in range(num_epochs):
        for i in range(days_in_epoch):
            locked_balance += balance * curr_apr_per_day * (1 - curr_unlock )
            balance += balance * curr_apr_per_day * curr_unlock
        curr_unlock += .02
        decrease = crystal_per_epoch[k+1] / crystal_per_epoch[k]
        curr_apr_per_day = initial_apr_per_day * decrease
    print(f"compound once a day balance {balance} locked {locked_balance}")

    #recompound once an hour
    locked_balance = 0
    balance = 1
    curr_unlock = .05
    claims_per_day = 24
    curr_apr_per_claim= initial_apr_per_day / claims_per_day
    for k in range(num_epochs):
        for i in range(days_in_epoch):
            for j in range(claims_per_day):
                locked_balance += balance * curr_apr_per_claim * (1 - curr_unlock )
                balance += balance * curr_apr_per_claim * curr_unlock
        curr_unlock += .02
        decrease = crystal_per_epoch[k+1] / crystal_per_epoch[k]
        curr_apr_per_claim = initial_apr_per_day * decrease / claims_per_day
    print(f"compound once an hour balance {balance} locked {locked_balance}")


    #hold
    balance_rewards = 0
    curr_apr_per_day = initial_apr_per_day
    curr_unlock = .05
    locked_balance = 0
    for k in range(num_epochs):
        for i in range(days_in_epoch):
            balance_rewards += 1 * curr_apr_per_day
        curr_unlock += .02
        decrease = crystal_per_epoch[k+1] / crystal_per_epoch[k]
        curr_apr_per_day = initial_apr_per_day * decrease
    curr_unlock -= .02
    balance_to_claim = balance_rewards * curr_unlock
    locked_balance = balance_rewards * (1 - curr_unlock)

    print(f"hold balance {1 + balance_to_claim} locked {locked_balance}")


print("SD")
apr = 400
apr_norm = apr / 100
initial_apr_per_day = apr_norm / 365
days_in_epoch = 7


for num_epochs in [2,4,8]:
    print(f"num epochs {num_epochs}")
    #recompound once an day
    balance = 1
    curr_unlock = .39
    curr_apr_per_day = initial_apr_per_day
    locked_balance = 0
    for k in range(num_epochs):
        for i in range(days_in_epoch):
            locked_balance += balance * curr_apr_per_day * (1 - curr_unlock )
            balance += balance * curr_apr_per_day * curr_unlock
        curr_unlock += .02
        #decrease = crystal_per_epoch[k+1] / crystal_per_epoch[k]
        curr_apr_per_day = initial_apr_per_day 
    print(f"compound once a day balance {balance} locked {locked_balance}")

    #recompound once an hour
    locked_balance = 0
    balance = 1
    curr_unlock = .39
    claims_per_day = 24
    curr_apr_per_claim= initial_apr_per_day / claims_per_day
    for k in range(num_epochs):
        for i in range(days_in_epoch):
            for j in range(claims_per_day):
                locked_balance += balance * curr_apr_per_claim * (1 - curr_unlock )
                balance += balance * curr_apr_per_claim * curr_unlock
        curr_unlock += .02
        #decrease = crystal_per_epoch[k+1] / crystal_per_epoch[k]
        curr_apr_per_claim = initial_apr_per_day  / claims_per_day
    print(f"compound once an hour balance {balance} locked {locked_balance}")


    #hold
    balance_rewards = 0
    curr_apr_per_day = initial_apr_per_day
    curr_unlock = .39
    locked_balance = 0
    for k in range(num_epochs):
        for i in range(days_in_epoch):
            balance_rewards += 1 * curr_apr_per_day
        curr_unlock += .02
        #decrease = crystal_per_epoch[k+1] / crystal_per_epoch[k]
        curr_apr_per_day = initial_apr_per_day
    curr_unlock -= .02
    balance_to_claim = balance_rewards * curr_unlock
    locked_balance = balance_rewards * (1 - curr_unlock)

    print(f"hold balance {1 + balance_to_claim} locked {locked_balance}")

