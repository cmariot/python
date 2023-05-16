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


# Classe Bank : A implementer
class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account: Account) -> bool:
        """
        Add new_account in the Bank
        @new_account:  Account() new account to append
        @return   True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code  ...
        if not isinstance(new_account, Account):
            print("Error: new_account is not an Account() instance")
            return False
        for account in self.accounts:
            if new_account.name == account.name:
                print("Error: {} name is already used".format(account.name))
                return False
        self.accounts.append(new_account)
        return True

    def __get_accounts_by_name(self,
                               origin: str,
                               dest: str) -> 'tuple[Account, Account]':
        origin_account: Account = None
        dest_account: Account = None
        for account in self.accounts:
            if account.name == origin:
                origin_account = account
            elif account.name == dest:
                dest_account = account
        if (origin_account is None or dest_account is None):
            raise FileNotFoundError("Account not found.")
        return (origin_account, dest_account)

    def __error(error: str) -> bool:
        print(error)
        return False

    def transfer(self, origin: str, dest: str, amount: float) -> bool:
        """"
        Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        if (not isinstance(origin, str)
            or not isinstance(dest, str)
                or not isinstance(amount, (float, int))):
            print("Error: invalid arg type during the transfer.")
            return False

        try:
            (origin_account,
                dest_account) = self.__get_accounts_by_name(origin,
                                                            dest)
        except FileNotFoundError as error:
            return self.__error(error)

        else:
            if self.__is_account_corrupted(origin_account):
                # fix origin account
                return self.__error("Error: origin account corrupted")
            elif self.__is_account_corrupted(dest_account):
                # fix dest account
                return self.__error("Error: dest account corrupted")
            else:
                if (origin_account.value < 0 or origin_account.value < amount):
                    return self.__error("Error: invalid transaction")

    def fix_account(self, name):
        """
        fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        # ... Your code  ...

    def __is_account_corrupted(self, account: Account) -> bool:
        # An account is corrupted if there is :
        # - an even number of attributes
        if (len(account.__dict__) % 2) == 0:
            return True
        # - an attribute starting with b
        elif any(key.startswith('b') for key in account.__dict__):
            return True
        # - no attribute starting with zip or addr
        elif not any(key.startswith('zip') or key.startswith('addr')
                     for key in account.__dict__):
            return True
        # - no attribute name
        elif 'name' not in account.__dict__:
            return True
        # - no attribute id
        elif 'id' not in account.__dict__:
            return True
        # - no attribute value
        elif 'value' not in account.__dict__:
            return True
        # - name not being a string
        elif not isinstance(account.name, str):
            return True
        # - id not being an int
        elif not isinstance(account.id, int):
            return True
        # - value not being an int or a float
        elif not isinstance(account.value, (int, float)):
            return True
        return False


if __name__ == "__main__":
    bank = Bank()
    bank.add(Account("Smith", value=10000, zip="94700"))
    bank.add(Account("Doe", value=1000, zip="91000"))

    bank.transfer("Smith", "truc", 500)
