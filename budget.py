class Category:

  def __init__(self, name, ledger=None, balance=None, total_withdraw=None):
    self.name = name
    balance = 0
    self.balance = balance
    ledger = []
    self.ledger = ledger
    total_withdraw = 0
    self.total_withdraw = total_withdraw
    return None

  def deposit(self, amount, description=None):
    if description != None:
      if amount > 0:
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        return True
      else:
        return False
    else:
      description = str()
      if amount > 0:
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        return True
      else:
        return False

  ## self.balance = track of baslance

  def withdraw(self, amount, description=None):

    if description != None:
      if amount > 0:
        if self.balance - amount >= 0:
          self.balance -= amount
          self.total_withdraw -= amount
          self.ledger.append({"amount": -amount, "description": description})
          return True
        else:
          return False
      else:
        return False
    else:
      description = str()
      if amount > 0:
        if self.balance - amount >= 0:
          self.balance -= amount
          self.total_withdraw -= amount
          self.ledger.append({"amount": -amount, "description": description})
          return True
        else:
          return False
      else:
        return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, destination):
    if amount > 0:
      if self.balance - amount >= 0:

        self.withdraw(amount, f"Transfer to {destination.name}")
        destination.deposit(amount, f"Transfer from {self.name}")
        return True
      else:
        return False
    else:
      return False

  def check_funds(self, amount):
    if amount > 0:
      if self.balance >= amount:
        return True
      else:
        return False
    else:
      return False

  def __str__(self):
    arranged_string = ""
    aa = ""
    bb = ""

    for i in range(len(self.ledger)):
      money = ("%.2f" % self.ledger[i]['amount'])
      des = self.ledger[i]['description'][0:23]
      if i == 0:
        aa = ('{:*^30}'.format(self.name))
        bb = ('{:<23}{:>7}'.format(des, money))
        arranged_string = f'{aa}\n{bb}'
      else:
        cc = ('{:<23}{:>7}'.format(des, money))
        arranged_string = f'{arranged_string}\n{cc}'
    arranged_string += f'\nTotal: {self.balance}'
    return arranged_string


def create_spend_chart(category):
  ##count total wd
  WD = []
  percent = []
  stat = {}
  name = []
  arranged = []
  for i in category:
    name.append(i.name)
    WD.append(i.total_withdraw)
  TWD = sum(WD)
  for i in WD:
    x = i / TWD * 100
    percent.append(x)

  greeting = "Percentage spent by category"

  for x in range(len(name)):
    n = 110
    stat[x] = []
    for i in range(11):
      n -= 10

      if n < percent[x]:
        stat[x] += ["o"]
      else:
        stat[x] += [" "]

  indicator = 0

  n = 110
  for i in range(11):
    s1 = stat[0][i]
    indicator = 1
    try:
      s2 = stat[1][i]
      indicator = 2
    except:
      pass
    try:
      s3 = stat[2][i]
      indicator = 3
    except:
      pass
    try:
      s4 = stat[3][i]
      indicator = 4
    except:
      pass
    n -= 10
    percentage = '{:>3}'.format(n)

    if indicator == 1:
      arranged.append(f'{percentage}| {s1}  ')
    if indicator == 2:
      arranged.append(f'{percentage}| {s1}  {s2}  ')
    if indicator == 3:
      arranged.append(f'{percentage}| {s1}  {s2}  {s3}  ')
    if indicator == 4:
      arranged.append(f'{percentage}| {s1}  {s2}  {s3}  {s4}  ')

  category_name = {}
  arranged_category = []
  for x in range(len(name)):
    category_name[x] = []
    for i in range(len(max(name, key=len))):
      try:
        category_name[x] += [name[x][i]]
      except:
        category_name[x] += " "

  for i in range(len(max(name, key=len))):
    s1 = category_name[0][i]
    indicator = 1
    try:
      s2 = category_name[1][i]
      indicator = 2
    except:
      pass
    try:
      s3 = category_name[2][i]
      indicator = 3
    except:
      pass
    try:
      s4 = category_name[3][i]
      indicator = 4
    except:
      pass

    if indicator == 1:
      arranged_category.append(f'     {s1}  ')
    if indicator == 2:
      arranged_category.append(f'     {s1}  {s2}  ')
    if indicator == 3:
      arranged_category.append(f'     {s1}  {s2}  {s3}  ')
    if indicator == 4:
      arranged_category.append(f'     {s1}  {s2}  {s3}  {s4}  ')

  chart = "\n".join(arranged)
  arr_name = "\n".join(arranged_category)
  #dash line
  dash = ('-' * (len(arranged[-1]) - 4))
  category_name = []

  return (f'{greeting}\n{chart}\n    {dash}\n{arr_name}')
