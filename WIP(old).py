# tool_df = pd.read_excel("./semiconductor_data.xlsx", sheet_name=2)

class WIP():
    def __init__(self, configure):
        setattr(self, configure.to_dict())
        self.configure = configure.to_dict()
        
    def __repr__(self):
        print(self.configure)

    # def __init__(self,lot_id,qty,r_qt,arrive_t,urgent_w,recipe,canrun_tool):
    #     #self.lot_id=lot_id
    #     self.qty=qty
    #     self.r_qt=r_qt
    #     self.arrive_t=arrive_t
    #     self.urgent_w=urgent_w
    #     self.recipe=recipe
    #     self.canrun_tool=canrun_tool
    
#讀取方式
# lot_id001=WIP(tool_df[0][])

#測試用
if __name__ == '__main__':
    print("hello world")
    pass