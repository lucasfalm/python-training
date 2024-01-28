def some_function():
  try:
    print("trying to execute")
    raise Exception("hm..... failed")

  except Exception as error:
    print(f"it failed!, reason: {error}")

  else:
    print("it worked!")

  finally:
    print("this will always run")

some_function()