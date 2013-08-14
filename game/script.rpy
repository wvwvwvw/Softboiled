# You can place the script of your game in this file.

transform midright:
    xalign 1.0 yalign 0.5

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg park = "park.jpg"
image bg park2 = "park2.jpg"
image bg office = "office.jpg"
image bg bar = "bar.png"
image bg bar2 = "bar2.png"
image bg mall = "mall.png"

image detect normal = "detectfrown.png"
image detect alert = "detectfrownalert.png"
image detect sour = "detectsour.png"
image detect trashed = "detecttrashed.png"

image bourbon full = "bourbonfull.png"
image bourbon half = "bourbonhalf.png"
image bourbon empty = "bourbonempty.png"

image caller normal = "handset.png"

image mystery normal = "mystery.png"

# Declare characters used by this game.

define d = Character('Detective', color="#c8ffc8")
define m = Character('Mysterious Figure', color="#c8c8ff")
define p = Character('Caller', color="#c8c8ff")
define n = Character('Detective\'s Mom', color="#c8c8ff")
define a = Character('Annoyed mom', color="c8c8ff")
define b = Character('Bartender', color="1ffff7")

# The game starts here.
label start:

scene bg office
with fade

show detect normal
with dissolve

d "How did I get here?"

"RING RING RRRRR-RING"

d "sorry, I need to get this"

show caller normal at right
show detect alert at left
with move

d "Hello?"

p "Detective!"

d "Mom?"

show detect trashed at left

n "I haven't heard from you in months, how is your little agency"

n "working out for you?"

n "Why don't you come home and have some of your favorite"

n "food?"

n "Rabbit, carrot, salmon and parsley soup!"

d "well mom, we both know I'd like that but I have some, uh"

d "open cases to tie up"

n "I understand, you must be very busy"

n "I should let you go"

n "-CLICK-"

scene bg office
show detect normal
with move

d "Sigh..."

d "Well let\'s look through my \"cases\""

jump casemenu

label casemenu:

menu:

    "case 1":

        jump case1

    "case 2":
        
        jump case2

    "Face Menu":

        jump facemenu

label facemenu:

menu:
    "Regular face or frown":
        show detect normal
        jump facemenu

    "Sour face":
        show detect sour
        jump facemenu

    "Alert face":
        show detect alert
        jump facemenu

    "Trashed face":
        show detect trashed
        jump facemenu

    "Hit the bar":
        jump bar

    "Back":
        jump casemenu

label case1:
    "Oh"
    "This one is a headache"
    "A lady called me this afternoon"
    jump parkparty
label case2:
    "I see"
    jump park

label parkparty:
    scene bg park with wipedown

    a "The incompetence of it all"
    a "the agency the, uh.. the entertainment agency"
    a "well they aren't answering their phone"
    a "and the personal number for the stupid clown..."
    a "well that lazy jerk isn\'t answering, either!"
    a "I get what I want and it's important that my kid"
    a "gets what they want too!"

    scene bg office with pixellate
    show detect normal

    d "That was about two hours ago"
    d "I hope the party\'s still on"
    "-opens bottom drawer-"
    show bourbon full at midright
    with move
    d "ah, yes..."
    scene bg office with pixellate
    d "mmm... mmm-hmm"
    d "So... good"
    show bourbon half at midright
    pause 2.5
    scene bg office with pixellate
    d "glug a lug"
    scene bg office with pixellate
    show bourbon empty at midright
    d "ah...."
    d "....!"
    show detect trashed
    with wipeup
    d "....Well that\'s breakfast!"
    show detect sour
    d "-BELCH-"
    d "oooh th- tbe back of my um"
    show detect trashed
    pause 1.5
    show detect sour
    d "mmm, I best get my to work"
    show detect trashed
    d "do a little go-walkies"
    show bg park
    a "Is anybody going to show up for me today?"
    a "oh there he is"
    scene bg park
    show detect sour
    pause 1.5
    show detect trashed
    d "N-h,hello! Howd\'ya do?"
    a "goodness you've shown up!"
    d "do you happen to know any information that could be useful"
    d "to me?"
    a "Yes!"
    a "Clowns wear bright clothing and makeup"
    a "and are generally easy to locate in public"
    a "I would do it myself if I didn't have to run a birthday party"
    a "for my freaking kid."
    a "I don't know how much longer my giant plastic tub of carmel swirled"
    a "ice cream is going to keep these children pacified"
    a "now if you\'ll excuse me, I must get back to my mildly disappointed"
    a "group"
    "she leaves"
    d "I had a feeling right then and there that I couldn't discern whether I"
    d "was in the future or the past"
    d "but I can\'t afford to get caught distracted by enumerous details"
    d "if I wanted to brag about my wages per hour"
    d "at some point in the future"
    d "Where should I start?"
    jump travelmenu


label bar:
scene bg bar
show detect trashed at left
with pixellate

"my old haunt"
"my stomping grounds"
"we smell, or at least tend to smell like each other"

b "hey old buddy"
d "Thank goodness"
d "I need an"
d "You know how much I need"
b "of course"
show bourbon full at center
with dissolve
d "ah yess"

label mall:
scene bg mall
with wipeleft

"I'm not sure if there is ever a point to being here"
"maybe I'm wrong"
"there are worse malls"

label travelmenu:

menu:

    "Bar":
       d "Looking for clowns is hard, I should be true to myself and let steam off the healthy way"
       d "Social interaction!"
       jump bar
    "The Mall":
       jump mall
    "The park":
       jump park

label park:
scene bg park

"Well hey there"
"old park!"
return
