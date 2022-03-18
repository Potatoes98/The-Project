from dotmap import DotMap

# action format:
# (action type):(subtype):({data})

# example:
# attack:technique:{name: 'placeholder', multiplier: '69'}
# prepare:none:none
# retreat:none:(agility: '69')

class battle:
  def __init__(self, opp1, opp2):
    self.opp1 = DotMap({"opp1":opp1, "action":"none"})
    self.opp2 = DotMap({"opp2":opp2, "action":"none"})

    self.battleState = "none"

  def submitAction(opp, action):
    self["opp"+str(opp)].action = action

  def update():
    if self.opp1.action = "none" or self.opp2.action = "none":
      return

    opp1Action = self.opp1.action
    opp2Action = self.opp2.action

    if "attack" in opp1Action:
      return