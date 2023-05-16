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

    def __init__(self):
        self.accounts = []

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
        # - no attribute name or not being a string
        elif ('name' not in account.__dict__
              or not isinstance(account.name, str)):
            return True
        # - no attribute id or not being an int
        elif ('id' not in account.__dict__
              or not isinstance(account.id, int)):
            return True
        # - no attribute value or not being an int or a float
        elif ('value' not in account.__dict__
              or not isinstance(account.value, (int, float))):
            return True
        return False

    def __get_accounts_by_name(self,
                               origin: str,
                               dest: str) -> 'tuple[Account, Account]':
        """
        Return a tuple of two Account() instances from their name
        or raise a NameError if one of the account is not found in the Bank
        """
        origin_account: Account = None
        dest_account: Account = None
        for account in self.accounts:
            if account.name == origin:
                origin_account = account
                if dest_account is not None:
                    break
            elif account.name == dest:
                dest_account = account
                if origin_account is not None:
                    break
        if (origin_account is None or dest_account is None):
            raise NameError("Account not found.")
        return (origin_account, dest_account)

    def add(self, new_account: Account = Account("")) -> bool:
        """
        Add new_account in the Bank
        @new_account:  Account() new account to append
        @return   True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return False
        if not new_account.name:
            for i in range(len(self.accounts)):
                new_account_name: str = "default_name_{}".format(i)
                if not any(account.name == new_account_name
                           for account in self.accounts):
                    new_account.__dict__['name'] = new_account_name
                    break
        elif any(account.name == new_account.name
                 for account in self.accounts):
            return False
        self.accounts.append(new_account)
        return True

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
            return False
        try:
            (origin_account,
                dest_account) = self.__get_accounts_by_name(origin, dest)
        except NameError:
            return False
        if self.__is_account_corrupted(origin_account):
            return False
        if self.__is_account_corrupted(dest_account):
            return False
        if (origin_account.value < 0 or origin_account.value < amount):
            return False
        origin_account.transfer(-amount)
        dest_account.transfer(amount)
        return True

    def fix_account(self, name: str) -> bool:
        """
        fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False

        to_fix_account: Account = next((account for account in self.accounts
                                        if account.name == name), None)
        if to_fix_account is None:
            return False

        # Fixing the account with :

        # - an attribute starting with b
        for key in to_fix_account.__dict__:
            if key.startswith('b'):
                to_fix_account.__dict__.pop(key)

        # - no attribute starting with zip or addr
        if not any(key.startswith('zip')
                   for key in to_fix_account.__dict__):
            to_fix_account.__dict__['zip'] = 0
        if not any(key.startswith('addr')
                   for key in to_fix_account.__dict__):
            to_fix_account.__dict__['addr'] = 0

        # - no attribute name or not being a string
        if ('name' not in to_fix_account.__dict__
                or not isinstance(to_fix_account.name, str)):
            for i in range(len(self.accounts)):
                new_account_name: str = "default_name_{}".format(i)
                if not any(account.name == new_account_name
                           for account in self.accounts):
                    to_fix_account.__dict__['name'] = new_account_name
                    break
                i += 1

        # - no attribute id or not being an int
        if ('id' not in to_fix_account.__dict__
                or not isinstance(to_fix_account.id, int)):
            to_fix_account.__dict__['id'] = Account.ID_COUNT + 1
            Account.ID_COUNT += 1

        # - no attribute value or not being an int or a float
        if ('value' not in to_fix_account.__dict__
                or not isinstance(to_fix_account.value, (int, float))):
            to_fix_account.__dict__['value'] = 0.0

        # - an even number of attributes
        if (len(to_fix_account.__dict__) % 2) == 0:
            for i in range(len(to_fix_account.__dict__)):
                new_attribute_name: str = "new_attribute_{}".format(i)
                if new_attribute_name not in to_fix_account.__dict__:
                    to_fix_account.__dict__[new_attribute_name] = 42
                    break
                i += 1


if __name__ == "__main__":

    bank = Bank()

    # Test add a new account
    if (bank.add(Account("Smith", value=10000, zip="94700")) is False):
        print("Error: cannot add Smith account")

    # Test add an invalid account type
    if bank.add(42):
        print("Error: 42 is not an account")

    # Test add an account with an existing name
    if bank.add(Account("Smith", value=10000, zip="94700")):
        print("Error: Duplicate account Smith added")

    # Test add an account with a negative value
    try:
        if bank.add(Account("Dupont", value=-10000, zip="94700")):
            print("Error: Dupont account with negative value added")
    except AttributeError as error:
        print(error)

    # Test add an account with a non string name
    try:
        if bank.add(Account(42, value=10000, zip="94700")):
            print("Error: Dupont account with negative value added")
    except AttributeError as error:
        print(error)

    bank.transfer("Smith", "truc", 500)
