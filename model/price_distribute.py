from conf import cursor 

class price_distribute:

  @staticmethod
  def index(params):
    sql="SELECT price, SUM(if(deal_type='buy', quantity, null)) as buy, sum(if(deal_type='sale', quantity, null)) as sale FROM deal GROUP BY price";
    cursor.execute(sql)
    results = cursor.fetchall()

    if len(results) == 0:
      return {}
    else:
      data = []

      for result in results: 
        row = {}
        row["price"] = str(result[0])
        row["buy"] = str(result[1])
        row["sale"] = str(result[2])

        data.append(row)

      return data
