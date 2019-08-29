# Python context manager protocol example
#
# - Comment/uncomment Code Block 1 to show unmanaged example.
# - Comment/uncomment the exception "raise UserWarning(...)" to raise an exception mid-access
# - Comment/uncomment Code Block 2 to use the managed example


class SafeDepositBox(object):
    def __init__(self, boxNumber):
        self.boxNumber = boxNumber

    def close(self):
        print("Closing box", str(self.boxNumber))

    def retrieve(self, item):
        print("Retrieving", item, "from box", self.boxNumber)
        # raise UserWarning("Urgent phone call")        # Exception occurring mid-access
        return item


def open_safe_deposit(boxNumber):
    print("Opening safe deposit box", boxNumber)
    return SafeDepositBox(boxNumber)


## Code Block 1
# safeDepositBox = open_safe_deposit(601)
# print("Accessing contents of safe deposit box:", safeDepositBox)
# safeStuff = safeDepositBox.retrieve("silver chalice")
# print("Safe deposit box closing...", "Retrieved", safeStuff)
# print("Safe deposit box closed")

print()


class ManagedSafeDepositBox(object):
    def __init__(self, boxNumber):
        self.safeDepositBox = open_safe_deposit(boxNumber)

    def __enter__(self):
        return self.safeDepositBox

    def __exit__(self, exception_type, exception_value, traceback):
        self.safeDepositBox.close()
        print("Safe deposit box closed")
        if exception_type:
            print("  An exception occurred:", exception_value)
        return True


## Code Block 2
with ManagedSafeDepositBox(601) as safeDepositBox:
    print("Accessing contents of safe deposit box:", safeDepositBox)
    safeStuff = safeDepositBox.retrieve("silver chalice")
    print("Safe deposit box closing...", "Retrieved", safeStuff)
