from smartcard.CardRequest import CardRequest
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.CardType import AnyCardType
from smartcard import util
import time

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

    blocks = {"00","01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F"} 

    for block in blocks:
        write = util.toBytes(f"FF B0 00 {block} 04")
        data, sw1, sw2 = conn.transmit(write)
        data = util.toHexString(data)
        status = util.toHexString([sw1, sw2])
        print("data = {}\tstatus = {}".format(data, status))
        