tool_df = pd.read_excel("./semiconductor_data.xlsx", sheet_name=2)

class WIP():
    def __init__(self,lot_id,qty,r_qt,arrive_t,urgent_w,recipe,canrun_tool):
        #self.lot_id=lot_id
        self.qty=qty
        self.r_qt=r_qt
        self.arrive_t=arrive_t
        self.urgent_w=urgent_w
        self.recipe=recipe
        self.canrun_tool=canrun_tool
    
#讀取方式
lot_id001=WIP(tool_df[0][])
