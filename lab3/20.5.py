def lucky(ticket):
    global lastTicket
    ticket = list(str(ticket))
    lastTicket = list(str(lastTicket))
    ticket = list(map(lambda x: int(x), ticket))
    lastTicket = list(map(lambda x: int(x), lastTicket))
    while len(ticket) != 6:
        ticket.insert(0, 0)
    if sum(ticket[:3]) == sum(ticket[3:]) and sum(lastTicket[:3]) == sum(lastTicket[3:]):
        return 'Счастливый'
    else:
        return 'Несчастливый'


lastTicket = 123123
print(lucky(100001))