from datetime import datetime
import copy


cur_date = datetime.now().strftime("%d_%m_%Y").split("_")[1]
fff = copy.copy(cur_date)
print(fff)