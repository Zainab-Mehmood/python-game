import time, os

def STAR_WAR_NAME(first_name, last_name, mum_maiden, city):
  first_slice = first_name[:3]
  second_slice = last_name[:3]
  third_slice = mum_maiden[:2]
  forth_slice = city[-3:][::-1]
  print()
  print("Generating your Star War name...")
  full_name = f"{first_slice}{second_slice} {third_slice}{forth_slice}"
  print(f"> Your Star Wars🌟 name is {full_name}.")


def main():
  print("STAR WARS NAME GENETATOR⭐")
  print()
  first_name = input("Enter your first name: ").capitalize().strip()
  last_name = input("Enter your last name: ").lower().strip()
  mum_maiden = input("Enter your Mum's maiden name: ").capitalize().strip()
  city = input("Enter the city where you were born: ").capitalize().strip()

  STAR_WAR_NAME(first_name, last_name, mum_maiden, city)

main()

