from src.character import Character


class Enemy(Character):

    def __init__(self,_name,_lv,_hp,_HpMax,_atk,_def,_money,_exp):
        super().__init__(_name,_lv,_hp,_atk,_def,_money,_exp)
        self.HpMax = _HpMax