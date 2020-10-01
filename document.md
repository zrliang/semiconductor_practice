# Tool(Machines)
- eqp_id
- recover_time +

# EOQ_RECIPE(程式)
- eqp_id
- recipe
- process_time

# WIP(Jobs)
- lot_id
- qty +
- r_qt +
- arrive_t +
- urgent_w +
- recipe +
- canrun_tool ? 多參數*

# set_up_time

# chromosome

## Process
1. import data
    + 
2. create jobs

## Questions
1. 全部寫在同一檔案? 分開
2. 讀取方式(ex:machine &recipe) 
3. id要嘛 ok
4. canrun_tool  切開
5. setuptime   有
6. 函式之間的關係
7. seris>>dit