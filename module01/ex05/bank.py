# Classe Account : Ne pas toucher !
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

# Fin de la classe account


class Bank:

    def __init__(self):
        # Accounts Storage
        self.accounts = {}

    # Transfer method
    def transfer(self, origin: Account, destination: Account) -> bool:

        if (self.is_secured(origin) is False
            or self.is_secured(destination) is False):
            return False

        return True

    # Security checks method
    def is_secured(self) -> bool:
        return False


    def transfer(self, amount):
        self.value += amount

#     def is_secured(self) -> bool:
        # # Check if has the right objects,
        # # if it's not corrupted
        # # and stores enough money to complete the transaction
        # return True
        # return False

    def is_corrupted(self) -> bool:
        # An account is corrupted if there is :
        # - an even number of attributes
        if (len(self.__dict__) % 2) == 0:
            return True
        # - an attribute starting with b
        elif any(key.startswith('b') for key in self.__dict__):
            return True
        # - no attribute starting with zip or addr
        elif not any(key.startswith('zip') or key.startswith('addr')
                     for key in self.__dict__):
            return True
        # - no attribute name
        elif 'name' not in self.__dict__:
            return True
        # - no attribute id
        elif 'id' not in self.__dict__:
            return True
        # - no attribute value
        elif 'value' not in self.__dict__:
            return True
        # - name not being a string
        elif not isinstance(self.name, str):
            return True
        # - id not being an int
        elif not isinstance(self.id, int):
            return True
        # - value not being an int or a float
        elif not isinstance(self.value, (int, float)):
            return True
        return False


class Bank:
    def __init__(self):
        self.accounts = {}

    def add(self, account: Account) -> bool:
        if not isinstance(account, Account):
            return False
        if account.id in self.accounts:
            return False
        self.accounts[account.id] = account
        return True

    def transfer(self, origin: Account, dest: Account, amount: float) -> bool:
        if not isinstance(origin, Account) or not isinstance(dest, Account):
            return False
        if origin.id not in self.accounts or dest.id not in self.accounts:
            return False
        if origin.value < amount:
            return False
        origin.value -= amount
        dest.transfer(amount)
        return True


if __name__ == "__main__":
    bank = Bank()

    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31'
    ))

    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation'
    ))

    print("Accounts: ", bank.accounts[1].name)

    # if bank.transfer('William John', 'Smith Jane', 545.0) is False:
    #     print('Failed')
    # else:
    #     print('Success')
