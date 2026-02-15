# Определение персонажей игры.

define e = Character(_('Белка'), color="#d5a771")

define c = Character(_('Кроккодиль'), color="#4e934f")

# Трансформации движения

transform move_left:
    xalign 0.5  # Начальная позиция (центр)
    yalign 1.0  # низ экрана.
    linear 0.25 xalign 0.0  # Плавное перемещение влево за 1 секунду

transform move_right_fast:    
    xalign 0.5  # Начальная позиция (центр)
    yalign 1.0  # низ экрана.
    linear 0.1 xalign 1.0  # Плавное перемещение влево за 1 секунду

transform move_right_fast_from_left:
    xalign 0.0  # Начальная позиция (центр)
    yalign 1.0  # низ экрана.
    linear 0.5 xalign 1.5  # Плавное перемещение влево за 1 секунду

transform move_center_from_right:
    xalign 1.0  # Начальная позиция (центр)
    yalign 1.0  # низ экрана.
    linear 0.5 xalign 0.5  # Плавное перемещение влево за 1 секунду


# Игра начинается здесь:
label start:

    scene bg forest
    play music "forest_music.mp3"
    show belka norm

    e "Ах, какой прекрасный дивный лес"
    e "Я вышла погрысть семечек и попрыгать по деревьям"
    e "У меня самая лучшая бельчачья жизнь"

    play music "danger_music.mp3"
    show croc attack at right
    show belka strah at move_left

    e "ААА ЧТО ЭТО?!"

    c "Рррр!ррррррррррррррррр!"
    c "Готовься мохнатка, сейчас ты станешь свидетелем моего пира..."

    show belka norm

    "ах что же мне делать..."

menu:
    
    "Сражаться":
        jump choice1_fight
    "Убежать":
        jump choice1_run

label choice1_fight:

    $ menu_flag = True

    show belka strah

    e "У меня самая лучшая бельчачья жизнь и у меня есть мечта..."
    e "Держись уродец!"

    c "Эй-эй, Мохнатка ты чего?!???"

    show belka strah at move_right_fast
    window hide

    pause 0.15

    show chorni
    hide belka
    hide croc
    stop music fadeout 1.00

    "Крокодилль умер. Белка одержала победу. Крокодилль не думал, что им полакомится белка."

    "П л о х а я  К о н ц о в к а"

    return

label choice1_run:

    $ menu_flag = False

    e "У меня самая лучшая бельчачья жизнь и у меня есть мечта..."

    show belka norm at move_right_fast_from_left

    e "Покаааааааааааааааа"

    show croc attack at move_center_from_right

    c "Эй-эй, Мохнатка подожди ты кудааааа!"

    hide belka
    hide croc
    stop music fadeout 2.00

    jump choice1_done

label choice1_done:

    scene bg lake
    play music "wind_music.mp3"

    pause 3.00

    show belka norm at move_center_from_right

    e "Фуууух, смогла убежать."
    e "Какое красивое озеро кстати..."
    e "Теперь я могу насладиться этими прекрасными видами..."

    show croc attack at right
    play music "danger_music.mp3"

    c "Привет"

    show belka strah at move_left

    e "ААААА опять ты"

    c "Постой, мохнатка, ты меня не так понимаешь. Не убегай"

    stop music fadeout 1.00

    e "?????"

    c "Я орешки принес давай вместе пожрем"

    play music "wind_music.mp3"

    e "О-орешки?? Мне? Я думал ты хочешь поесть мной!"

    c "Я просто бельчячий язык плохо знаю..."

    show croc happy

    c "Мир?" 

    e "......"

    show belka happy

    e "Мир!"

    "Они любовались мягким ветерком и теплом уходящего солнца..."
    "Они кушали орешки и наслаждались обществом друг друга"

    "Х о р о ш а я  К о н ц о в к а"

#Cука нах


    return