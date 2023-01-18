from smartcard.CardRequest import CardRequest
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.CardType import AnyCardType
from smartcard import util

WAIT_FOR_SECONDS = 20

if __name__ == '__main__':
    # respond to the insertion of any type of smart card
    card_type = AnyCardType()

    # create the request. Wait for up to x seconds for a card to be attached
    request = CardRequest(timeout=WAIT_FOR_SECONDS, cardType=card_type)

    # listen for the card
    service = None
    try:
        service = request.waitforcard()
    except CardRequestTimeoutException:
        print("ERROR: No card detected")
        exit(-1)

    # when a card is attached, open a connection
    conn = service.connection
    conn.connect()

    # send the ACR122u a command and receive any data and response codes.
    write = util.toBytes(f"FF 00 52 00 00")
    data, sw1, sw2 = conn.transmit(write)
    data = util.toHexString(data)
    status = util.toHexString([sw1, sw2])
    print("data = {}\tstatus = {}".format(data, status))

    # write = util.toBytes(f"30 04")
    # data, sw1, sw2 = conn.transmit(write)
    # data = util.toHexString(data)
    # status = util.toHexString([sw1, sw2])
    # print("data = {}\tstatus = {}".format(data, status))

    # write = util.toBytes(f"30 08")
    # data, sw1, sw2 = conn.transmit(write)
    # data = util.toHexString(data)
    # status = util.toHexString([sw1, sw2])
    # print("data = {}\tstatus = {}".format(data, status))

    # write = util.toBytes(f"30 0C")
    # data, sw1, sw2 = conn.transmit(write)
    # data = util.toHexString(data)
    # status = util.toHexString([sw1, sw2])
    # print("data = {}\tstatus = {}".format(data, status))