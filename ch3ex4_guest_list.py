guests = ['guest no1', 'guest no2', 'guest no3']

print(f'You, {guests[0].title()}, are cordially invited to my dinner party.')
print(f'You, {guests[1].title()}, are cordially invited to my dinner party.')
print(f'You, {guests[2].title()}, are cordially invited to my dinner party.')

# 3.5 Changing Guest List

rsvp_no = "guest no3"
print(f"Unfortunately, {rsvp_no.title()} cannot make the dinner party.")
guests[2] = "replacement guest"
print(f'You, {guests[0].title()}, are cordially invited to my dinner party.')
print(f'You, {guests[1].title()}, are cordially invited to my dinner party.')
print(f'You, {guests[2].title()}, are cordially invited to my dinner party.')

# 3.6 More Guests

print("I have obtained a larger table and can now fit three more guests.")
guests.insert(0, "new guest1")
guests.insert(0, "new guest2")
guests.append("new guest3")

print(f'You, {guests[0].title()}, are cordially invited to my dinner party.')
print(f'You, {guests[1].title()}, are cordially invited to my dinner party.')
print(f'You, {guests[2].title()}, are cordially invited to my dinner party.')
print(f'You, {guests[3].title()}, are cordially invited to my dinner party.')
print(f'You, {guests[4].title()}, are cordially invited to my dinner party.')
print(f'You, {guests[5].title()}, are cordially invited to my dinner party.')

# 3.7 Shrinking Guest List

print("Unfortunately, the new table will not arrive on time. I now only have space for two dinner guests.")

uninvited = guests.pop()
print(f"I regret to inform you, {uninvited.title()}, that I must recend your invitation to my dinner party.")
uninvited = guests.pop()
print(f"I regret to inform you, {uninvited.title()}, that I must recend your invitation to my dinner party.")
uninvited = guests.pop()
print(f"I regret to inform you, {uninvited.title()}, that I must recend your invitation to my dinner party.")
uninvited = guests.pop()
print(f"I regret to inform you, {uninvited.title()}, that I must recend your invitation to my dinner party.")

print(f"You, {guests[0].title()}, are still cordially invited to my dinner party.")
print(f"You, {guests[1].title()}, are still cordially invited to my dinner party.")

del guests[0]
del guests[0]
print(guests)