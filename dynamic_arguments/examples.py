from datetime import datetime

# ------------ X ------------ X ------------ #

def print_choice(type, items):
  print(f"you choose the {type}: {', '.join(items)}")

# ------------ X ------------ X ------------ #

def make_order(price, time, *args, **kwargs):
  if "fruits" in kwargs:
    print_choice("fruits", kwargs["fruits"])

  if "foods" in kwargs:
    print_choice("foods", kwargs["foods"])

  if "drinks" in kwargs:
    print_choice("drinks", kwargs["drinks"])

  response = f"order made at {time}\ntotal: {price}"

  if len(args) == 2:
    address, comments = args

    response += f"\nto deliver at: {address}"
    response += f"\nextra comments: {comments}"

  print(response)

# ------------ X ------------ X ------------ #

today = datetime.now()

make_order(
  "$10.00",
  today,
  "5 my address, my city", # NOTE: extra dynamic params
  "remove tomato",         # NOTE: extra dynamic params
  foods  = ["pasta", "tacos"],
  fruits = ["apple"]
)
