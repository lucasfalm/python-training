from datetime import datetime

def make_order(price, time, *args, **kwargs):
  if "fruits" in kwargs:
    print(f"you choose the fruits: {', '.join(kwargs['fruits'])}")

  if "foods" in kwargs:
    print(f"you choose the foods: {', '.join(kwargs['foods'])}")

  if "drinks" in kwargs:
    print(f"you choose the drinks: {', '.join(kwargs['drinks'])}")

  if len(args) == 2:
    address, comments = args

  response = f"order made at {time}\ntotal: {price}"

  if address:
    response += f"\nto deliver at: {address}"

  if comments:
    response += f"\nextra comments: {comments}"

  print(response)

today = datetime.now()

make_order(
  "$10.00",
  today,
  "5 my address, my city", # NOTE: extra dynamic params
  "remove tomato",         # NOTE: extra dynamic params
  foods  = ["pasta", "tacos"],
  fruits = ["apple"]
)
